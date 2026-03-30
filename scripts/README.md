# Scripts

## You probably don't need this

If you have fewer than 20 teams or fewer than 5 judges, use the [MLH Judging Example Sheet](https://docs.google.com/spreadsheets/d/1eyfZmUMA63oG_89l6n6zpHj_o5V2xwS-gyndmTl5Z24/edit) instead. It's a Google Sheet you can copy in one click and requires no technical setup.

This script is useful if you have many teams and want to automate score aggregation from a CSV export.

---

## score_calc.py

Aggregates judge scores from a CSV file and produces a ranked list of teams.

**Requirements:** Python 3.6+ (no external dependencies — uses only the standard library)

**Usage:**

```bash
# macOS / Linux
python3 scripts/score_calc.py scores.csv

# Windows
python scripts/score_calc.py scores.csv
```

**Input format:** A CSV file where each row is one judge's scores for one team. See `schemas/score-input.json` for the full schema.

Minimum required columns:
```
team_name,judge_name,technical,innovation,impact,presentation
```

Example `scores.csv`:
```csv
team_name,judge_name,technical,innovation,impact,presentation
Team Rocket,Alice,8,7,6,8
Team Rocket,Bob,7,8,7,7
Byte Bandits,Alice,9,9,8,9
Byte Bandits,Bob,8,8,9,8
```

**Output:**
```
=== HACKATHON RESULTS ===
1. Byte Bandits     avg: 35.3 / 40   (judges: 2)
2. Team Rocket      avg: 32.5 / 40   (judges: 2)
```

**Edge cases handled:**
- Tied scores: teams with equal averages are listed alphabetically
- Missing judge scores: averages are computed from judges who did submit scores; a warning is printed
- Zero scores: treated as valid scores (not skipped)
- Single judge: works fine

---

## Adding the required field check

If you customize the rubric (see `equity-pack/judging/rubric.md`) and remove a required category, update the `REQUIRED_CATEGORIES` constant at the top of `score_calc.py` to match your rubric.
