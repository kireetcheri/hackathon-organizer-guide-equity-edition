"""
Tests for scripts/score_calc.py

Run with: python3 -m pytest tests/
"""

import csv
import os
import sys
import tempfile
import pytest

# Make scripts/ importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from score_calc import parse_scores, rank_teams, REQUIRED_CATEGORIES


def write_csv(rows, fieldnames=None, tmpdir=None):
    """Write a list of dicts to a temp CSV file. Returns the file path."""
    if fieldnames is None:
        fieldnames = ["team_name", "judge_name"] + REQUIRED_CATEGORIES
    f = tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False,
        dir=tmpdir, newline=""
    )
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
    f.close()
    return f.name


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------

def test_happy_path(tmp_path):
    rows = [
        {"team_name": "Team A", "judge_name": "Alice", "technical": 8, "innovation": 7, "impact": 6, "presentation": 8},
        {"team_name": "Team A", "judge_name": "Bob",   "technical": 7, "innovation": 8, "impact": 7, "presentation": 7},
        {"team_name": "Team B", "judge_name": "Alice", "technical": 5, "innovation": 5, "impact": 5, "presentation": 5},
    ]
    path = write_csv(rows, tmpdir=str(tmp_path))
    scores = parse_scores(path, REQUIRED_CATEGORIES)

    assert "Team A" in scores
    assert "Team B" in scores

    ranked = rank_teams(scores)
    assert ranked[0][0] == "Team A"
    assert ranked[1][0] == "Team B"


# ---------------------------------------------------------------------------
# Tied scores: alphabetical tiebreak
# ---------------------------------------------------------------------------

def test_tied_scores(tmp_path):
    rows = [
        {"team_name": "Zebra", "judge_name": "Alice", "technical": 8, "innovation": 8, "impact": 8, "presentation": 8},
        {"team_name": "Alpha", "judge_name": "Alice", "technical": 8, "innovation": 8, "impact": 8, "presentation": 8},
    ]
    path = write_csv(rows, tmpdir=str(tmp_path))
    scores = parse_scores(path, REQUIRED_CATEGORIES)
    ranked = rank_teams(scores)

    assert ranked[0][0] == "Alpha"
    assert ranked[1][0] == "Zebra"
    assert ranked[0][1] == ranked[1][1]  # same avg


# ---------------------------------------------------------------------------
# Missing judge scores: other judges' rows still count; warning emitted
# ---------------------------------------------------------------------------

def test_missing_judge_scores_warns(tmp_path, capsys):
    rows = [
        {"team_name": "Team A", "judge_name": "Alice", "technical": 8, "innovation": 8, "impact": 8, "presentation": 8},
        {"team_name": "Team A", "judge_name": "Bob",   "technical": "",  "innovation": 8, "impact": 8, "presentation": 8},
    ]
    path = write_csv(rows, tmpdir=str(tmp_path))
    scores = parse_scores(path, REQUIRED_CATEGORIES)

    captured = capsys.readouterr()
    assert "WARNING" in captured.err
    assert "Team A" in scores
    assert len(scores["Team A"]) == 1  # only Alice's row counted


# ---------------------------------------------------------------------------
# Zero scores: treated as valid, not skipped
# ---------------------------------------------------------------------------

def test_zero_scores(tmp_path):
    rows = [
        {"team_name": "Last Place", "judge_name": "Alice", "technical": 0, "innovation": 0, "impact": 0, "presentation": 0},
        {"team_name": "Winner",     "judge_name": "Alice", "technical": 9, "innovation": 9, "impact": 9, "presentation": 9},
    ]
    path = write_csv(rows, tmpdir=str(tmp_path))
    scores = parse_scores(path, REQUIRED_CATEGORIES)
    ranked = rank_teams(scores)

    assert ranked[0][0] == "Winner"
    assert ranked[1][0] == "Last Place"
    assert ranked[1][1] == 0.0


# ---------------------------------------------------------------------------
# Bad input format: non-numeric score
# ---------------------------------------------------------------------------

def test_bad_input_format(tmp_path):
    rows = [
        {"team_name": "Team A", "judge_name": "Alice", "technical": "great", "innovation": 8, "impact": 8, "presentation": 8},
    ]
    path = write_csv(rows, tmpdir=str(tmp_path))
    with pytest.raises(ValueError, match="not a number"):
        parse_scores(path, REQUIRED_CATEGORIES)


# ---------------------------------------------------------------------------
# Empty input
# ---------------------------------------------------------------------------

def test_empty_input(tmp_path):
    # CSV with header only, no rows
    f = tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False, dir=str(tmp_path), newline=""
    )
    f.write("team_name,judge_name,technical,innovation,impact,presentation\n")
    f.close()

    with pytest.raises(ValueError, match="No scores to process"):
        parse_scores(f.name, REQUIRED_CATEGORIES)


# ---------------------------------------------------------------------------
# Missing required column
# ---------------------------------------------------------------------------

def test_missing_required_column(tmp_path):
    rows = [{"team_name": "Team A", "judge_name": "Alice", "technical": 8}]
    path = write_csv(rows, fieldnames=["team_name", "judge_name", "technical"], tmpdir=str(tmp_path))
    with pytest.raises(ValueError, match="missing required columns"):
        parse_scores(path, REQUIRED_CATEGORIES)


# ---------------------------------------------------------------------------
# Single judge: works fine
# ---------------------------------------------------------------------------

def test_single_judge(tmp_path):
    rows = [
        {"team_name": "Solo Team", "judge_name": "Alice", "technical": 7, "innovation": 7, "impact": 7, "presentation": 7},
    ]
    path = write_csv(rows, tmpdir=str(tmp_path))
    scores = parse_scores(path, REQUIRED_CATEGORIES)
    ranked = rank_teams(scores)

    assert len(ranked) == 1
    assert ranked[0][0] == "Solo Team"
    assert ranked[0][2] == 1  # judge count


# ---------------------------------------------------------------------------
# File not found
# ---------------------------------------------------------------------------

def test_file_not_found():
    with pytest.raises(ValueError, match="File not found"):
        parse_scores("/nonexistent/path/scores.csv", REQUIRED_CATEGORIES)
