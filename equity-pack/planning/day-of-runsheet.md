# Day-of Runsheet

A hour-by-hour guide for event day. Customize the times to fit your schedule — the structure is what matters.

This template is for a **one-day event (9am–9pm)**. For 24-hour events, add an overnight block between Hacking (Evening) and Judging Morning.

> **Print this and carry it.** Don't rely on your phone. Paper doesn't lose battery.

---

## Before anyone arrives (T-2 hours)

**Who:** Organizing team only (2–3 people)

| Time | Task | Owner |
|------|------|-------|
| T-2h | Arrive at venue. Walk every room you'll use. | Lead organizer |
| T-2h | Test projector, microphone, and any AV equipment | AV lead |
| T-2h | Set up registration table: name tags, printed schedule, swag | Registration lead |
| T-2h | Confirm food arrival window with caterer/delivery | Food lead |
| T-2h | Post printed room signs (check-in, hacking room, bathroom, organizer HQ) | Any |
| T-1.5h | Set up power strips and extension cords throughout hacking space | Any |
| T-1.5h | Test the submission platform (Devpost/Devfolio) — submit a dummy project | Any |
| T-1h | Brief all volunteers: their role, who their point of contact is, where to be | Lead organizer |
| T-30m | Open venue doors for early arrivals | Registration lead |

---

## Check-in (T-30min to Opening)

**Who:** Registration lead + 1–2 volunteers

- Hand each participant: name tag, printed schedule, any swag
- Collect dietary restrictions if you haven't already
- Direct people to the hacking space and announce opening ceremony start time
- Keep a headcount — useful for food ratios later

**If someone shows up without a registration:**
Take their name and contact, add them if you have capacity. Don't turn anyone away at the door for a school event.

---

## Opening Ceremony (~20 minutes)

**Suggested structure:**

1. **Welcome** (2 min) — Who you are, what this event is, who helped make it happen
2. **Sponsor acknowledgements** (2 min) — Name each sponsor; show logos on screen
3. **Rules and logistics** (5 min):
   - Team size limits
   - What qualifies as "built during the event" (don't over-engineer this)
   - Submission deadline and platform
   - Where food will be, where organizers will be
4. **Judging criteria** (3 min) — Show the rubric. Tell participants what judges will look for.
5. **Resources** (3 min) — Any APIs, mentors, or tools available to teams
6. **Hacking starts** (1 min) — Make it a moment. Count down if you want.

**Time cap:** 20 minutes. Don't go over — participants are eager to start.

---

## Hacking — Morning Block

**Who:** 1 organizer circulating, 1 at organizer HQ

| Time | Task |
|------|------|
| H+0:30 | Walk the hacking space — are teams forming? Are any people isolated and struggling to find a team? Help them. |
| H+1:00 | Confirm food arrival ETA. Text the caterer if you haven't heard. |
| H+1:30 | Check in with any mentors. Are they circulating or sitting in one spot? |
| H+2:00 | Send a Slack/Discord/group chat message with a mid-morning encouragement + reminder of submission deadline |

**Team formation problems:**
If you see solo participants who haven't formed a team 30+ minutes in, gather them and do a quick round of introductions. Most will naturally group up.

---

## Lunch

| Time | Task |
|------|------|
| Lunch-30m | Confirm food is on-site or in transit |
| Lunch | Announce food is ready; direct people to the food area |
| Lunch | Eat something yourself. You need it. |
| Lunch+15m | Check that vegetarian/vegan/allergen options haven't run out |
| Lunch+30m | Send a reminder: X hours remaining until submission deadline |

---

## Hacking — Afternoon Block

| Time | Task |
|------|------|
| H+4:00 | Check in with teams — are they on track? Do any need unblocking? |
| H+5:00 | Send a reminder: "2 hours until submissions close. Your project doesn't have to be perfect — submit what you have." |
| H+5:30 | Brief judges: confirm arrival time, confirm they've reviewed the rubric |
| H+6:00 | Send final submission reminder. Start telling teams to wrap up and prepare their demo. |

---

## Submission Close

| Time | Task |
|------|------|
| Deadline-15m | Announce: "15 minutes to submission deadline" |
| Deadline | Lock submissions on your platform. (Devpost: set status to "closed") |
| Deadline+5m | Export submission list. Distribute projects to judges. |
| Deadline+10m | Announce judging schedule: which teams present when, where, how long |

**If a team misses the deadline by a few minutes:** Use your judgment. For a first-year event, grace is fine. Set a hard stop for larger events where fairness matters more.

---

## Judging

**Suggested format (adjust for your number of teams):**

- Each team gets **5 minutes demo + 2 minutes Q&A** = 7 minutes per team
- Judges rotate through teams expo-style, or teams present in sequence to a panel
- Expo style (teams at stations, judges walk around) works better for 8+ teams
- Panel style (teams present to seated judges one at a time) works better for <8 teams

| Task | Owner |
|------|-------|
| Brief judges before they start: rubric, timing, how to submit scores | Lead organizer |
| Keep time — use a visible timer or an audible signal | Timekeeper volunteer |
| Collect judge scoresheets as each round finishes | Organizer at judging HQ |
| Tabulate scores during judging — don't wait until it's over | Score lead |

**If judges are running behind:** Compress Q&A, not the demos. Teams earned their 5 minutes.

---

## Score Tabulation

While final judging finishes:

- [ ] Collect all scoresheets from judges
- [ ] Enter scores into your spreadsheet or run `python3 scripts/score_calc.py scores.csv`
- [ ] Identify top 3 (+ any category awards)
- [ ] Verify: did any judge skip a team? Check for blanks.
- [ ] Resolve ties (alphabetical tiebreak, or a quick judge vote)

This should take 10–20 minutes. Give yourself buffer — don't announce awards until you're certain.

---

## Awards Ceremony (~15–20 minutes)

1. **Thank everyone** — participants, sponsors, judges, volunteers, faculty advisor
2. **Highlight a few projects** (not just winners) — 2–3 interesting things you saw during judging
3. **Announce category awards first**, then 3rd, 2nd, 1st place
4. **Photos** — get everyone together for a group photo. Tag sponsors on social media.
5. **Closing** — what's next? Will you run this again? Where can people follow for updates?

---

## Cleanup

Divide and conquer:

| Task | Who |
|------|-----|
| Pack up registration table, leftover swag | Volunteer A |
| Break down food area, dispose of trash | Volunteer B |
| Collect extension cords, power strips, AV equipment | Volunteer C |
| Walk every room — leave it better than you found it | Lead organizer |
| Take a final photo of the empty-and-clean space (for admin good will) | Any |

Leave a clean venue. Your admin approved this space. Make it easy to say yes next year.

---

## Post-event (within 48 hours)

- [ ] Send thank-you emails to sponsors, judges, and volunteers
- [ ] Post event photos on social media — tag sponsors
- [ ] Send participants a 3-question feedback form
- [ ] Debrief with your organizing team while it's fresh

---

*Part of the [Equity Pack](../README.md). See also: [8-Week Checklist](./8-week-checklist.md)*
