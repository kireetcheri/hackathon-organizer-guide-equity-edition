# Judging Rubric

A ready-to-use rubric for hackathon judges. Copy this into your judging spreadsheet.

> **Required fields** (marked ⚠️) must stay in the rubric for the score calculator to work correctly. Customizable fields (marked ✏️) can be renamed, adjusted, or removed — but update your scoring spreadsheet accordingly.

---

## Standard Rubric (4 categories, 10 points each, 40 points total)

| Category | ⚠️/✏️ | Score (0–10) | What judges should look for |
|----------|--------|-------------|----------------------------|
| **Technical Achievement** | ⚠️ | /10 | Is this technically impressive for the time given? Does it actually work? Partial credit for ambitious projects that didn't fully come together. |
| **Innovation / Creativity** | ⚠️ | /10 | Is the idea novel? Does it approach a problem in an unexpected way? Not the same as "is it polished." |
| **Impact / Usefulness** | ✏️ | /10 | Does this solve a real problem? Would someone actually use this? It's fine if the answer is "no" — this is a hackathon, not a startup. Score based on potential. |
| **Presentation** | ✏️ | /10 | Can the team clearly explain what they built and why? Is the demo functional? Communication matters. |
| **Total** | — | /40 | Sum of above |

---

## Scoring guidelines for judges

**0–3:** Did not meet the basic bar. Project doesn't function, or the team can't explain it.

**4–6:** Meets expectations for a hackathon project. Works at the demo level; idea is clear.

**7–8:** Above average. Shows technical depth or genuine creativity beyond what's expected.

**9–10:** Outstanding. Would be a finalist at a larger event. Use sparingly.

**Important:** Scores should reflect the hackathon context. A team that learned a new framework and built something functional in 12 hours deserves a 7–8 even if the code is messy. A team that copied a tutorial and presented it as original work deserves a 2–3 regardless of polish.

---

## Optional add-on categories ✏️

Include any of these if relevant to your event's theme:

| Category | Score (0–10) | What judges should look for |
|----------|-------------|----------------------------|
| **Accessibility** | /10 | Did the team consider users with disabilities? Screen reader support, color contrast, keyboard navigation, etc. |
| **Use of [SPONSOR] API** | /10 | [CUSTOMIZE: replace with specific sponsor tech track] |
| **Social Impact** | /10 | Does the project address a community need or social issue? |
| **Best Hardware Hack** | /10 | For hardware tracks: quality of physical build, safety, functionality |
| **Best First Hack** | /10 | For first-time hackers: did they learn something new? Did they complete something? |

---

## Judge instructions (give this to every judge before judging starts)

> **Before you start:**
> - You will evaluate [NUMBER] projects
> - Each project gets [TIME] minutes: [TIME - 1] for the demo, 1 minute for your scores
> - Score each project independently — don't adjust scores after you see later projects
> - Focus on learning over business potential. Most winning hackathon projects are not startups.
>
> **Required fields** in your scoring sheet cannot be left blank. If a team didn't demo a category, score it 0 — don't skip it.
>
> **If you suspect cheating** (project was built before the event, code was copied without attribution): flag it to the organizing team immediately. Do not confront the team yourself.
>
> Questions? Go to [ORGANIZER STATION LOCATION].

---

## Score aggregation

Use the [MLH Judging Example Sheet](https://docs.google.com/spreadsheets/d/1eyfZmUMA63oG_89l6n6zpHj_o5V2xwS-gyndmTl5Z24/edit) for full judge allocation and stack ranking.

For simple events (<10 teams, 1–3 judges), you can use the Python score calculator in this repo:

```bash
python3 scripts/score_calc.py scores.csv
```

See `scripts/README.md` for input format. You don't need the script — the spreadsheet approach works for any size event.

---

*Part of the [Equity Pack](../README.md).*
