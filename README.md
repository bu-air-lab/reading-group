# AIR Lab Reading Group

The record of every paper our lab's reading group has read since 2019, plus the next meeting.

**Website:** https://bu-air-lab.github.io/reading-group/

## How it works

- `data/sessions.csv` holds the sessions, one row per meeting. **It is the only file you edit week to week.**
- `index.html` reads that file and builds the page. It sorts meetings into tables by semester, shows the next meeting at the top, and adds a search box.
- `data/info.json` holds the group details shown at the top of the page (meeting time, room, organizer). Update it when the time or the organizer changes.

There is no build step. Once you commit a change, GitHub Pages shows it within about a minute.

## Add a session (about 2 minutes)

1. On GitHub, open `data/sessions.csv` and click the pencil icon (**Edit**).
2. Add one line at the bottom, for example:
   ```
   2026-12-04,2-3 pm,"N09, EB",Xiaopeng,SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model,"Qiayuan Liao, Yiyang Shao, et al.",CoRL 2026,https://arxiv.org/pdf/2610.28480,
   ```
3. Click **Commit changes**.

Rules for the CSV:
- `date` must be `YYYY-MM-DD`. The page uses it to pick the semester and to decide whether a meeting is past or upcoming.
- Put any field that contains a comma in double quotes, such as `"N09, EB"` or an author list.
- Use the leader's full name the way it already appears in the file (for example `Austine Oloo`, not `Austin`), so every person is spelled one way.
- `notes` is optional. Use it for things like "Moved from 3/27" or "On Zoom".
- If a meeting is canceled, delete its row. If it moves, change the date.

If you add a future meeting, it appears at the top as **Next meeting**. Once the date passes, it moves into its semester's table on its own.

Semesters are worked out from the date: Spring is Jan–May, Summer is Jun–Jul, and Fall is Aug–Dec.

**Check your edit (optional):** `python3 tools/check_sessions.py` catches bad dates, missing titles, and unquoted commas.

## Weekly routine for the organizer

1. Find a leader and a paper (members email suggestions to the organizer).
2. Add the row to `data/sessions.csv`.
3. Send the announcement to `reading-group-air-lab@googlegroups.com`, using `templates/announcement.txt`.

## Handing the group over

When the organizer leaves the lab:

1. Add the new organizer to the lab's GitHub organization with write access to this repo.
2. Make them an owner or manager of the Google Group `reading-group-air-lab@googlegroups.com`.
3. Update `organizer` and `organizer_email` in `data/info.json`.
4. Update the lines below.

| Period | Organizer |
|---|---|
| 2019 – Aug 2023 | *(to fill in)* |
| Sep 2023 – Sep 2025 | Yohei Hayamizu |
| Oct 2025 – present | Zainab Altaweel |

## Preview locally

```
python3 -m http.server
```
Then open http://localhost:8000. (Opening `index.html` directly will not load the CSV, because browsers block that.)

## Where the history came from

- **2019 – Aug 2023:** the original page (https://yding25.com/ReadingGroup/index.html), via the archive at https://github.com/yoheihayamizu/hrs-reading-group.
- **Sep 2023 onward:** the announcement emails sent to the mailing list, cross-checked against the archive above. Where the two disagreed, the emails won.
