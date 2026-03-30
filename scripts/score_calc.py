"""
Hackathon score aggregator.
Reads judge scores from a CSV, averages per team, and prints a ranked list.

No external dependencies — uses only Python standard library.
Requires Python 3.6+.

Usage:
    python3 scripts/score_calc.py scores.csv
    python3 scripts/score_calc.py scores.csv --categories technical innovation  # custom categories

See scripts/README.md for input format.
"""

import csv
import sys
import argparse
from collections import defaultdict
from statistics import mean

# Required columns in the input CSV.
# Update this list if you customize the judging rubric.
REQUIRED_CATEGORIES = ["technical", "innovation", "impact", "presentation"]
REQUIRED_COLUMNS = ["team_name", "judge_name"] + REQUIRED_CATEGORIES


def parse_scores(filepath, categories):
    """
    Parse CSV file into a dict of {team_name: [list of total scores per judge]}.
    Warns on missing judge scores; skips rows that are entirely malformed.
    Raises ValueError on bad input format.
    """
    required = ["team_name", "judge_name"] + categories

    try:
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            if reader.fieldnames is None:
                raise ValueError("CSV file appears to be empty.")

            missing_cols = [c for c in required if c not in reader.fieldnames]
            if missing_cols:
                raise ValueError(
                    f"CSV is missing required columns: {missing_cols}\n"
                    f"Found columns: {list(reader.fieldnames)}\n"
                    f"See scripts/README.md for the expected format."
                )

            team_scores = defaultdict(list)  # {team_name: [score_per_judge_row]}
            warnings = []

            for i, row in enumerate(reader, start=2):  # row 1 is header
                team = row.get("team_name", "").strip()
                judge = row.get("judge_name", "").strip()

                if not team or not judge:
                    warnings.append(f"Row {i}: missing team_name or judge_name — skipped.")
                    continue

                scores_for_row = []
                for cat in categories:
                    raw = row.get(cat, "").strip()
                    if raw == "":
                        warnings.append(
                            f"Row {i} ({team}, judge {judge}): missing score for '{cat}' — "
                            f"this judge's row excluded from average."
                        )
                        scores_for_row = None
                        break
                    try:
                        val = float(raw)
                    except ValueError:
                        raise ValueError(
                            f"Row {i} ({team}, judge {judge}): score for '{cat}' "
                            f"is not a number: '{raw}'"
                        )
                    scores_for_row.append(val)

                if scores_for_row is not None:
                    team_scores[team].append(sum(scores_for_row))

    except FileNotFoundError:
        raise ValueError(f"File not found: {filepath}")

    if not team_scores:
        raise ValueError("No scores to process. Check your CSV file.")

    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)

    return dict(team_scores)


def rank_teams(team_scores):
    """
    Return list of (team_name, avg_score, judge_count) sorted by avg descending,
    then alphabetically by name for ties.
    """
    ranked = []
    for team, scores in team_scores.items():
        avg = mean(scores) if scores else 0.0
        ranked.append((team, avg, len(scores)))

    ranked.sort(key=lambda x: (-x[1], x[0]))
    return ranked


def main():
    parser = argparse.ArgumentParser(
        description="Aggregate hackathon judge scores from a CSV file."
    )
    parser.add_argument("filepath", help="Path to scores CSV file")
    parser.add_argument(
        "--categories",
        nargs="+",
        default=REQUIRED_CATEGORIES,
        help=f"Score categories to sum (default: {REQUIRED_CATEGORIES})",
    )
    args = parser.parse_args()

    try:
        team_scores = parse_scores(args.filepath, args.categories)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    ranked = rank_teams(team_scores)
    max_score = len(args.categories) * 10

    print(f"\n=== HACKATHON RESULTS ===")
    print(f"{'Rank':<6} {'Team':<30} {'Avg Score':<15} {'Judges'}")
    print("-" * 60)
    for i, (team, avg, count) in enumerate(ranked, start=1):
        print(f"{i:<6} {team:<30} {avg:.1f} / {max_score:<8} ({count} judge{'s' if count != 1 else ''})")

    print(f"\nTotal teams: {len(ranked)}")


if __name__ == "__main__":
    main()
