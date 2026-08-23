#!/usr/bin/env python3
"""Validate plugin data, refresh GitHub metadata, and generate README entries."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import os
import re
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "plugins.json"
README_PATH = ROOT / "README.md"
START_MARKER = "<!-- BEGIN GENERATED RANKING -->"
END_MARKER = "<!-- END GENERATED RANKING -->"
CATEGORY_START_MARKER = "<!-- BEGIN GENERATED CATEGORY INDEX -->"
CATEGORY_END_MARKER = "<!-- END GENERATED CATEGORY INDEX -->"
ALLOWED_CATEGORIES = {
    "Files & Runtime",
    "Input & Navigation",
    "Memory & Knowledge",
    "Themes & Appearance",
    "UI & Interfaces",
    "Vision",
    "Workflow & Automation",
}
CATEGORY_ORDER = (
    "Files & Runtime",
    "Input & Navigation",
    "Memory & Knowledge",
    "Themes & Appearance",
    "UI & Interfaces",
    "Vision",
    "Workflow & Automation",
)
REPO_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SUMMARY_PATTERN = re.compile(
    r"\*\*Last verified:\*\* \d{4}-\d{2}-\d{2} \| "
    r"\*\*Minimum at admission:\*\* \d[\d,]* stars \| "
    r"\*\*Plugins:\*\* \d+"
)


class ValidationError(ValueError):
    """Raised when repository data or generated content is invalid."""


class RefreshError(RuntimeError):
    """Raised when live GitHub metadata cannot be fetched safely."""


def parse_date(value: str, field: str) -> None:
    if not isinstance(value, str) or not DATE_PATTERN.fullmatch(value):
        raise ValidationError(f"{field} must use YYYY-MM-DD format")
    try:
        dt.date.fromisoformat(value)
    except ValueError as error:
        raise ValidationError(f"{field} is not a valid calendar date") from error


def sort_key(plugin: dict[str, Any]) -> tuple[int, str, str]:
    return (-plugin["stars"], plugin["name"].casefold(), plugin["repo"].casefold())


def sort_plugins(plugins: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(plugins, key=sort_key)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and value == value.strip()


def validate_data(data: dict[str, Any]) -> None:
    if not isinstance(data, dict):
        raise ValidationError("data must be a JSON object")
    parse_date(data.get("last_updated"), "last_updated")
    minimum = data.get("minimum_stars")
    if not isinstance(minimum, int) or isinstance(minimum, bool) or minimum < 1:
        raise ValidationError("minimum_stars must be a positive integer")

    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        raise ValidationError("plugins must be a non-empty array")

    required = {
        "name", "repo", "package", "category", "license", "description",
        "install_command", "manifest_path", "entrypoint", "stars",
        "stars_at_addition", "added_at", "verified_at",
    }
    seen_names: set[str] = set()
    seen_repos: set[str] = set()
    seen_packages: set[str] = set()

    for index, plugin in enumerate(plugins, start=1):
        if not isinstance(plugin, dict):
            raise ValidationError(f"plugin {index} must be an object")
        missing = required - plugin.keys()
        if missing:
            raise ValidationError(
                f"plugin {index} is missing: {', '.join(sorted(missing))}"
            )

        for field in (
            "name", "package", "license", "install_command", "manifest_path", "entrypoint"
        ):
            if not _nonempty(plugin[field]):
                raise ValidationError(f"plugin {index} has an invalid {field}")

        name_key = plugin["name"].casefold()
        if name_key in seen_names:
            raise ValidationError(f"duplicate plugin name: {plugin['name']}")
        seen_names.add(name_key)

        repo = plugin["repo"]
        if not isinstance(repo, str) or not REPO_PATTERN.fullmatch(repo):
            raise ValidationError(f"{plugin['name']} has an invalid repository")
        repo_key = repo.casefold()
        if repo_key in seen_repos:
            raise ValidationError(f"duplicate repository: {repo}")
        seen_repos.add(repo_key)

        package_key = plugin["package"].casefold()
        if package_key in seen_packages:
            raise ValidationError(f"duplicate package: {plugin['package']}")
        seen_packages.add(package_key)

        if plugin["category"] not in ALLOWED_CATEGORIES:
            raise ValidationError(f"{plugin['name']} has an invalid category")
        description = plugin["description"]
        if (
            not isinstance(description, str)
            or len(description) < 30
            or "\n" in description
            or not description.endswith(".")
        ):
            raise ValidationError(
                f"{plugin['name']} must have a one-line factual description"
            )
        if not plugin["manifest_path"].endswith("package.json"):
            raise ValidationError(f"{plugin['name']} manifest_path must name package.json")
        if "dsh plugin" not in plugin["install_command"] and "install.sh" not in plugin["install_command"]:
            raise ValidationError(f"{plugin['name']} lacks a DSH installation path")

        stars = plugin["stars"]
        if not isinstance(stars, int) or isinstance(stars, bool) or stars < 0:
            raise ValidationError(f"{plugin['name']} has an invalid star count")
        admitted = plugin["stars_at_addition"]
        if not isinstance(admitted, int) or isinstance(admitted, bool) or admitted < minimum:
            raise ValidationError(
                f"{plugin['name']} did not meet the {minimum}-star threshold"
            )
        parse_date(plugin["added_at"], f"{plugin['name']}.added_at")
        parse_date(plugin["verified_at"], f"{plugin['name']}.verified_at")

    if plugins != sort_plugins(plugins):
        raise ValidationError(
            "plugins must be sorted by exact stars descending, then by name"
        )


def format_stars(count: int) -> str:
    if count >= 100_000:
        return f"{round(count / 1000):d}k"
    if count >= 1_000:
        value = f"{count / 1000:.1f}"
        return f"{value[:-2] if value.endswith('.0') else value}k"
    return str(count)


def render_category_index(data: dict[str, Any]) -> str:
    grouped = {category: [] for category in CATEGORY_ORDER}
    for plugin in data["plugins"]:
        grouped[plugin["category"]].append(plugin)

    lines: list[str] = []
    for category in CATEGORY_ORDER:
        plugins = sorted(grouped[category], key=sort_key)
        entries = ", ".join(
            f"{plugin['name']} ({format_stars(plugin['stars'])} stars)"
            for plugin in plugins
        )
        lines.extend(
            [
                f"**{category} ({len(plugins)})**",
                entries,
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def render_ranking(data: dict[str, Any]) -> str:
    lines: list[str] = []
    for plugin in data["plugins"]:
        lines.extend(
            [
                f"- [{plugin['name']}](https://github.com/{plugin['repo']}) - "
                f"**{format_stars(plugin['stars'])} stars** | "
                f"`{plugin['category']}` | "
                f"`{plugin['license']}`. "
                f"{plugin['description']}",
                f"  - Install: `{plugin['install_command']}`",
            ]
        )
    return "\n".join(lines)


def build_readme(template: str, data: dict[str, Any]) -> str:
    markers = (
        (CATEGORY_START_MARKER, CATEGORY_END_MARKER, "category index"),
        (START_MARKER, END_MARKER, "ranking"),
    )
    for start_marker, end_marker, label in markers:
        if template.count(start_marker) != 1 or template.count(end_marker) != 1:
            raise ValidationError(f"README must contain one generated {label} block")

    category_start = template.index(CATEGORY_START_MARKER)
    category_end = template.index(CATEGORY_END_MARKER)
    start = template.index(START_MARKER)
    end = template.index(END_MARKER)
    if category_start >= category_end or start >= end:
        raise ValidationError("README generated markers are out of order")
    if category_end > start:
        raise ValidationError("README category index must appear before the ranking")

    generated = (
        template[: category_start + len(CATEGORY_START_MARKER)]
        + "\n"
        + render_category_index(data)
        + "\n"
        + template[category_end:]
    )
    start = generated.index(START_MARKER)
    end = generated.index(END_MARKER)
    generated = (
        generated[: start + len(START_MARKER)]
        + "\n"
        + render_ranking(data)
        + "\n"
        + generated[end:]
    )
    summary = (
        f"**Last verified:** {data['last_updated']} | "
        f"**Minimum at admission:** {data['minimum_stars']:,} stars | "
        f"**Plugins:** {len(data['plugins'])}"
    )
    generated, replacements = SUMMARY_PATTERN.subn(summary, generated, count=1)
    if replacements != 1:
        raise ValidationError("README verification summary is missing or invalid")
    return generated.rstrip() + "\n"


def load_data(path: Path = DATA_PATH) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValidationError(f"cannot read {path}: {error}") from error


def github_headers(token: str | None = None) -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-dsh-plugins-star-updater",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch_github_repo(repo: str, token: str | None = None) -> dict[str, Any]:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}", headers=github_headers(token)
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as error:
        raise RefreshError(f"{repo}: GitHub returned HTTP {error.code}") from error
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
        raise RefreshError(f"{repo}: {error}") from error
    required = {"full_name", "stargazers_count", "archived", "fork"}
    if not required.issubset(payload):
        raise RefreshError(f"{repo}: GitHub returned incomplete metadata")
    return payload


def fetch_all(
    plugins: list[dict[str, Any]], fetcher: Callable[[str], dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    metadata: dict[str, dict[str, Any]] = {}
    errors: list[str] = []
    for plugin in plugins:
        repo = plugin["repo"]
        try:
            metadata[repo] = fetcher(repo)
        except Exception as error:
            errors.append(str(error))
    if errors:
        raise RefreshError("GitHub refresh failed:\n- " + "\n- ".join(errors))
    return metadata


def inspect_live_metadata(
    data: dict[str, Any], metadata: dict[str, dict[str, Any]]
) -> list[str]:
    warnings: list[str] = []
    for plugin in data["plugins"]:
        repo = plugin["repo"]
        current = metadata[repo]
        if current["full_name"].casefold() != repo.casefold():
            raise RefreshError(
                f"{repo} resolves to {current['full_name']}; update the canonical record"
            )
        if current["archived"]:
            warnings.append(f"{repo} is archived and needs maintainer review")
        if current["fork"]:
            warnings.append(f"{repo} is a fork and needs maintainer review")
        if current["stargazers_count"] < data["minimum_stars"]:
            warnings.append(
                f"{repo} has {current['stargazers_count']} stars; keep it pending review"
            )
    return warnings


def refresh_data(
    data: dict[str, Any],
    fetcher: Callable[[str], dict[str, Any]],
    today: str,
) -> tuple[dict[str, Any], list[str]]:
    metadata = fetch_all(data["plugins"], fetcher)
    warnings = inspect_live_metadata(data, metadata)
    refreshed = copy.deepcopy(data)
    for plugin in refreshed["plugins"]:
        plugin["stars"] = metadata[plugin["repo"]]["stargazers_count"]
        plugin["verified_at"] = today
    refreshed["plugins"] = sort_plugins(refreshed["plugins"])
    refreshed["last_updated"] = today
    validate_data(refreshed)
    return refreshed, warnings


def json_text(data: dict[str, Any]) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", newline="\n", dir=path.parent,
            prefix=f".{path.name}.", suffix=".tmp", delete=False,
        ) as temp:
            temp.write(content)
            temp.flush()
            os.fsync(temp.fileno())
            temp_name = temp.name
        os.replace(temp_name, path)
        temp_name = None
    finally:
        if temp_name:
            Path(temp_name).unlink(missing_ok=True)


def write_outputs(data: dict[str, Any], readme_template: str) -> None:
    atomic_write(DATA_PATH, json_text(data))
    atomic_write(README_PATH, build_readme(readme_template, data))


def check_repository(data: dict[str, Any], readme: str) -> None:
    validate_data(data)
    if build_readme(readme, data) != readme:
        raise ValidationError(
            "README is out of sync; run python scripts/update-stars.py --generate"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--generate", action="store_true")
    mode.add_argument("--verify-live", action="store_true")
    mode.add_argument("--refresh", action="store_true")
    args = parser.parse_args(argv)

    try:
        data = load_data()
        readme = README_PATH.read_text(encoding="utf-8")
        validate_data(data)
        if args.check:
            check_repository(data, readme)
            print(f"Validated {len(data['plugins'])} plugins.")
            return 0
        if args.generate:
            atomic_write(README_PATH, build_readme(readme, data))
            print(f"Generated README for {len(data['plugins'])} plugins.")
            return 0

        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        fetcher = lambda repo: fetch_github_repo(repo, token)  # noqa: E731
        if args.verify_live:
            metadata = fetch_all(data["plugins"], fetcher)
            warnings = inspect_live_metadata(data, metadata)
            for warning in warnings:
                print(f"WARNING: {warning}", file=sys.stderr)
            print(f"Verified {len(data['plugins'])} live repositories.")
            return 0

        today = dt.datetime.now(dt.timezone.utc).date().isoformat()
        refreshed, warnings = refresh_data(data, fetcher, today)
        for warning in warnings:
            print(f"WARNING: {warning}", file=sys.stderr)
        write_outputs(refreshed, readme)
        print(f"Refreshed {len(refreshed['plugins'])} plugins.")
        return 0
    except (OSError, ValidationError, RefreshError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
