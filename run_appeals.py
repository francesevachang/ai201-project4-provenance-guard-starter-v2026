#!/usr/bin/env python3
"""
Test criterion 4 (the appeal path) three times.  <- UNIT 8, MILESTONE 3

    python app.py                                # in one terminal
    python run_appeals.py --label before         # in another

run_eval.py only sends text, and an appeal needs a content_id from a real
submission first. So for each trial this:

  1. submits 10 pieces of text to POST /submit
  2. appeals each content_id that came back via POST /appeal
  3. reads GET /log and checks, for each one, that an appeal entry exists
     with status "under_review"

Criterion 4: of 10 appeals, all 10 change the item's status and appear in the
log, in each of the three trials.

Writes results/appeals_<date>_<label>.md.
"""

import argparse
import datetime as dt
import json
import sys

import config

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"
APPEALS_PER_TRIAL = 10

# Any text long enough to score works — the appeal path doesn't depend on the
# label. A number in each makes the ten submissions distinct.
TEXT = ("I wrote this paragraph myself for the appeal test, number {n}. It is long "
        "enough to be scored, and the point is not the label it gets but whether "
        "the appeal that follows it is recorded and changes the item's status. "
        "Each trial sends ten of these and appeals every one.")


def run_trial(requests, url, trial):
    results = []
    for n in range(1, APPEALS_PER_TRIAL + 1):
        # One creator per piece, so ten submissions stay under the rate limit.
        creator = f"eval_appeal_t{trial}_{n}"
        sub = requests.post(f"{url}/submit", timeout=90,
                            json={"text": TEXT.format(n=n), "creator_id": creator})
        sub_body = sub.json() if sub.content else {}
        content_id = sub_body.get("content_id")

        result = {"n": n, "submit_status": sub.status_code, "content_id": content_id,
                  "original_status": None, "appeal_status": None,
                  "response_status": None, "logged_status": None}
        if content_id:
            app = requests.post(f"{url}/appeal", timeout=30, json={
                "content_id": content_id,
                "reasoning": "I wrote this myself.",
            })
            app_body = app.json() if app.content else {}
            result["appeal_status"] = app.status_code
            result["response_status"] = app_body.get("status")
        results.append(result)

    # Read the log once, after all ten, and check each item's history.
    log = requests.get(f"{url}/log", timeout=30).json()["entries"]
    for result in results:
        history = [e for e in log if e.get("content_id") == result["content_id"]]
        original = next((e for e in history if e.get("event") != "appeal"), None)
        appeal = next((e for e in history if e.get("event") == "appeal"), None)
        result["original_status"] = original.get("status") if original else None
        result["logged_status"] = appeal.get("status") if appeal else None
        result["passed"] = (
            result["appeal_status"] == 200
            and result["original_status"] == "decided"
            and result["logged_status"] == "under_review"
        )
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    args = parser.parse_args()

    import requests

    try:
        requests.get(f"{args.url}/health", timeout=5)
    except Exception:  # noqa: BLE001
        print(f"Nothing answering at {args.url}. Start it:  python app.py", file=sys.stderr)
        sys.exit(1)

    trials = []
    for trial in range(1, args.trials + 1):
        results = run_trial(requests, args.url, trial)
        passed = sum(r["passed"] for r in results)
        print(f"  trial {trial}: {passed}/{len(results)} appeals changed status and were logged")
        trials.append(results)

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"appeals_{stamp}{label}.md"
    lines = [f"# Appeal path (criterion 4){f' — {args.label}' if args.label else ''}", "",
             "- Produced by: `run_appeals.py::run_trial`",
             "- Service: `app.py::submit`, `app.py::appeal`, `app.py::get_log`", "",
             "| Trial | Passed |", "|---|---|"]
    for i, results in enumerate(trials, 1):
        lines.append(f"| {i} | {sum(r['passed'] for r in results)}/{len(results)} |")
    for i, results in enumerate(trials, 1):
        lines += ["", f"## Trial {i}", "", "```json", json.dumps(results, indent=2), "```"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
