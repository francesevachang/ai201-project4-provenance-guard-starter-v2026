# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives

Of 7 pieces I wrote myself, at most 1 is labeled high-confidence AI, in each of the three trials.

**Why this target:** On a writing site a wrong accusation costs more than a missed detection, so the limit is strict. Not higher: 2 in 7 (~29%) would accuse too many real writers. Not 0: detection is imperfect and the model signal varies between trials, so 0 in all three trials is unrealistic.



---

## 2. Score spread

Across 5 clearly-AI and 5 clearly-human samples, the average AI score is at least 0.4 higher than the average human score, in all three trials.

**Why this target:** Not lower: the unsure band is 0.30 wide (thresholds 0.35 and 0.65), so a gap under 0.3 means typical AI and human text can't land in opposite labels; 0.4 adds margin. Not higher: 0.5+ would need roughly human 0.2 and AI 0.7, which is too ambitious for a noisy detector.



---

## 3. Label coverage

Across 12 test samples, each of the 3 labels (human, unsure, AI) appears at least 2 times, in all three trials.

**Why this target:** 2 shows each label is reliably reachable, not accidental, without being too strict



---

## 4. Appeal path

Of 10 appeals, all 10 change the item's status and appear in the log.

**Why this target:** Appeals are plain code with no model noise, so any miss is a bug, and a lost appeal means a wrongly accused writer is ignored.



---

## 5. Bad input

For each of 3 bad inputs (missing `text`, empty `text`, a 100,000-character `text`), `/submit` returns a 4xx error with a clear message, never a 500 or a crash, in 3 of 3 attempts each.

**Why this target:** Not lower, because bad input is plain validation code with no model noise, so any 500 is a bug.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
