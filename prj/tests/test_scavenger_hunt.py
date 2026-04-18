import re
from pathlib import Path


def read_bingo_card() -> str:
    path = Path(__file__).resolve().parents[1] / "TECH_LIFE_BINGO.md"
    return path.read_text(encoding="utf-8")


def test_scavenger_hunt_section_exists() -> None:
    content = read_bingo_card()
    assert "## Scavenger Hunt Mode" in content


def test_scavenger_hunt_has_24_checkboxes() -> None:
    content = read_bingo_card()
    items = re.findall(r"^- \[ \] .+$", content, flags=re.MULTILINE)
    assert len(items) == 24


def test_scavenger_hunt_progress_meter_present() -> None:
    content = read_bingo_card()
    assert "Completed: `0/24`" in content
    assert "Progress:" in content
    assert re.search(r"Progress: `\[[ \-#]*\] \d+%`", content)
