from __future__ import annotations

import copy
import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "update-stars.py"
SPEC = importlib.util.spec_from_file_location("update_stars", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load {MODULE_PATH}")
update_stars = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = update_stars
SPEC.loader.exec_module(update_stars)


def make_plugin(
    name: str = "Example Plugin",
    repo: str = "example/dsh-plugin",
    stars: int = 100,
) -> dict:
    slug = name.lower().replace(" ", "-")
    return {
        "name": name,
        "repo": repo,
        "package": slug,
        "category": "UI & Interfaces",
        "license": "MIT",
        "description": f"{name} adds a tested interface extension to DeepSeek Harness.",
        "install_command": f"dsh plugin --profile web add {slug}",
        "manifest_path": "package.json",
        "entrypoint": slug,
        "stars": stars,
        "stars_at_addition": max(stars, 100),
        "added_at": "2026-08-15",
        "verified_at": "2026-08-15",
    }


def make_data(*plugins: dict) -> dict:
    return {
        "last_updated": "2026-08-15",
        "minimum_stars": 100,
        "plugins": list(plugins),
    }


def metadata(repo: str, stars: int, **overrides: object) -> dict:
    result = {
        "full_name": repo,
        "stargazers_count": stars,
        "archived": False,
        "fork": False,
    }
    result.update(overrides)
    return result


class AdmissionTests(unittest.TestCase):
    def test_accepts_authentic_bundle_record(self) -> None:
        update_stars.validate_data(make_data(make_plugin()))

    def test_rejects_topic_only_record_without_manifest(self) -> None:
        plugin = make_plugin()
        del plugin["manifest_path"]
        with self.assertRaisesRegex(update_stars.ValidationError, "manifest_path"):
            update_stars.validate_data(make_data(plugin))

    def test_rejects_skill_only_category(self) -> None:
        plugin = make_plugin()
        plugin["category"] = "Skills"
        with self.assertRaisesRegex(update_stars.ValidationError, "category"):
            update_stars.validate_data(make_data(plugin))

    def test_rejects_99_star_admission(self) -> None:
        plugin = make_plugin(stars=99)
        plugin["stars_at_addition"] = 99
        with self.assertRaisesRegex(update_stars.ValidationError, "100-star threshold"):
            update_stars.validate_data(make_data(plugin))

    def test_accepts_100_star_admission(self) -> None:
        update_stars.validate_data(make_data(make_plugin(stars=100)))

    def test_accepts_missing_license_label(self) -> None:
        plugin = make_plugin()
        plugin["license"] = "No license detected"
        update_stars.validate_data(make_data(plugin))

    def test_rejects_duplicate_repository(self) -> None:
        first = make_plugin("Alpha", "example/project", 200)
        second = make_plugin("Beta", "EXAMPLE/project", 100)
        with self.assertRaisesRegex(update_stars.ValidationError, "duplicate repository"):
            update_stars.validate_data(make_data(first, second))

    def test_rejects_duplicate_package(self) -> None:
        first = make_plugin("Alpha", "example/alpha", 200)
        second = make_plugin("Beta", "example/beta", 100)
        second["package"] = first["package"].upper()
        with self.assertRaisesRegex(update_stars.ValidationError, "duplicate package"):
            update_stars.validate_data(make_data(first, second))


class RefreshTests(unittest.TestCase):
    def test_refresh_uses_exact_stars_and_name_tie_breaker(self) -> None:
        alpha = make_plugin("Alpha", "example/alpha", 200)
        beta = make_plugin("beta", "example/beta", 100)
        values = {
            "example/alpha": metadata("example/alpha", 500),
            "example/beta": metadata("example/beta", 500),
        }
        refreshed, warnings = update_stars.refresh_data(
            make_data(alpha, beta), values.__getitem__, "2026-08-16"
        )
        self.assertEqual([item["name"] for item in refreshed["plugins"]], ["Alpha", "beta"])
        self.assertEqual(refreshed["last_updated"], "2026-08-16")
        self.assertEqual(warnings, [])

    def test_partial_api_failure_does_not_mutate_data(self) -> None:
        alpha = make_plugin("Alpha", "example/alpha", 200)
        beta = make_plugin("Beta", "example/beta", 100)
        original = make_data(alpha, beta)
        before = copy.deepcopy(original)

        def failing_fetcher(repo: str) -> dict:
            if repo.endswith("beta"):
                raise update_stars.RefreshError("simulated failure")
            return metadata(repo, 300)

        with self.assertRaises(update_stars.RefreshError):
            update_stars.refresh_data(original, failing_fetcher, "2026-08-16")
        self.assertEqual(original, before)

    def test_archived_and_forked_projects_are_flagged(self) -> None:
        alpha = make_plugin("Alpha", "example/alpha", 200)
        beta = make_plugin("Beta", "example/beta", 100)
        values = {
            "example/alpha": metadata("example/alpha", 200, archived=True),
            "example/beta": metadata("example/beta", 100, fork=True),
        }
        warnings = update_stars.inspect_live_metadata(make_data(alpha, beta), values)
        self.assertIn("archived", warnings[0])
        self.assertIn("fork", warnings[1])

    def test_below_threshold_is_kept_and_flagged(self) -> None:
        plugin = make_plugin(stars=100)
        values = {plugin["repo"]: metadata(plugin["repo"], 99)}
        refreshed, warnings = update_stars.refresh_data(
            make_data(plugin), values.__getitem__, "2026-08-16"
        )
        self.assertEqual(refreshed["plugins"][0]["stars"], 99)
        self.assertIn("pending review", warnings[0])


class ReadmeTests(unittest.TestCase):
    def test_generation_is_idempotent(self) -> None:
        data = make_data(make_plugin(stars=100))
        template = (
            "# Title\n\n"
            "**Last verified:** 2026-01-01 | **Minimum at admission:** 100 stars | "
            "**Plugins:** 0\n\n"
            f"{update_stars.START_MARKER}\nold\n{update_stars.END_MARKER}\n"
        )
        first = update_stars.build_readme(template, data)
        second = update_stars.build_readme(first, data)
        self.assertEqual(first, second)
        self.assertIn("**Plugins:** 1", first)
        self.assertIn("https://github.com/example/dsh-plugin", first)
        self.assertIn("Install:", first)


if __name__ == "__main__":
    unittest.main()
