# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-12 21:24
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `6a157eb5-6506-42cb-9b3d-c0353c02ae5d` | human | 0.335 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `67ce506d-15be-45c7-bcac-ea5d718f1a43` | unsure | 0.514 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `f80a750c-16a9-43a7-ac99-cd6411885b3e` | unsure | 0.499 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `b47759d4-698e-4e2a-bf19-f59d3b01f811` | unsure | 0.649 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `f30e1edf-eea9-4a9e-b4e2-ac8a880b13a9` | human | 0.331 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c2f7edbd-71ee-40d4-8653-8eec6818bd4d` | unsure | 0.523 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `833105fe-e6b5-4a65-bd01-7eeca008bc3e` | unsure | 0.543 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `8e01a4ee-3347-4b76-ab87-dbdde7c7ad0a` | unsure | 0.373 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `b11fb720-4b6d-4817-aa7d-9a5d5c0bb602` | unsure | 0.369 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `dc8c15ca-10a6-4504-a7ad-653f32be4f15` | ai | 0.858 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `1dbe0ff2-bec7-4a50-aee8-b9cc86a975a4` | unsure | 0.457 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `edd05358-6f52-4188-b86d-56151340894d` | ai | 0.743 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `f0bab6be-8dce-468a-8f91-a5e213892441` | unsure | 0.501 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `4584b417-5a00-43b7-910f-4fe81190f452` | ai | 0.729 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `58b7e08d-9ef3-4c38-b68e-ac02d7e15859` | ai | 0.778 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `d303dd4d-b479-468b-bed5-bc1a729e3e1c` | unsure | 0.466 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `17d049e4-8f07-490e-afd0-8c9ec5de161e` | unsure | 0.474 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `72c1ad9b-fba3-4955-b463-d25e2d716ab3` | unsure | 0.411 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `b41a5f1b-c184-466d-849f-b7c50bca91a1` | unsure | 0.456 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `ebecb9ce-44ad-43d3-a76f-7f95be9e58de` | human | 0.305 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `69ebf62c-91db-4158-8bd6-d4035ae39f9b` | unsure | 0.526 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `0beb887e-d53a-4056-81c5-02427bf94bf0` | unsure | 0.360 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `bce3cb37-b431-4ef0-9bae-76add5b09bab` | human | 0.313 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `941289b9-317c-48e6-af46-4fced21ff69b` | unsure | 0.433 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `7cc288ea-7826-483b-b3ea-ac37cc18ffc5` | human | 0.150 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `44f597a7-d533-4ea2-880d-9efd1bf749b0` | human | 0.156 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `66c00904-9b6f-40b0-b38f-94659300f3e4` | unsure | 0.649 | HELD |
| MF06 | malformed | text is emoji only | 200 | `54cef2cc-c41c-4b5d-9ba4-f5f378c4ceda` | unsure | 0.648 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `55684921-9a84-485c-b569-84cd7d053c67` | unsure | 0.603 | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9fb5a5ae-66a2-4105-88fe-2f65a0addb09` | human | 0.164 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e08d4e20-c839-42bd-af06-88bea022d1a3` | human | 0.164 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `be7a0b45-a419-4e7c-916a-19ceb4fe5d8a` | human | 0.164 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a699bd5f-0614-49d7-8338-9ae37ef74081` | human | 0.164 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ed8e1593-dc13-4280-afe2-2a065290a903` | human | 0.164 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5eea64e0-1f82-437e-a272-96be75aaf54c` | human | 0.164 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5dd0aac2-4ef0-40a0-b7ad-3235ab12985d` | human | 0.164 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0648c073-c172-46c5-a1b8-960ceb71b423` | human | 0.164 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f4b1f791-1628-4eb8-b9b4-d5d16174dced` | human | 0.164 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ab431ce4-3d53-4c8f-bb93-ac137f36b138` | human | 0.164 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "6a157eb5-6506-42cb-9b3d-c0353c02ae5d",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3351,
  "model_score": 0.1635,
  "style_score": 0.7068,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "67ce506d-15be-45c7-bcac-ea5d718f1a43",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5144,
  "model_score": 0.5943,
  "style_score": 0.4344,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "f80a750c-16a9-43a7-ac99-cd6411885b3e",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.499,
  "model_score": 0.6662,
  "style_score": 0.3317,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "b47759d4-698e-4e2a-bf19-f59d3b01f811",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6489,
  "model_score": 0.6114,
  "style_score": 0.6864,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "f30e1edf-eea9-4a9e-b4e2-ac8a880b13a9",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.331,
  "model_score": 0.3212,
  "style_score": 0.3408,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c2f7edbd-71ee-40d4-8653-8eec6818bd4d",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5232,
  "model_score": 0.5727,
  "style_score": 0.4736,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "833105fe-e6b5-4a65-bd01-7eeca008bc3e",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5431,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "8e01a4ee-3347-4b76-ab87-dbdde7c7ad0a",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3726,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "b11fb720-4b6d-4817-aa7d-9a5d5c0bb602",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.369,
  "model_score": 0.7042,
  "style_score": 0.2339,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "dc8c15ca-10a6-4504-a7ad-653f32be4f15",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8583,
  "model_score": 0.9792,
  "style_score": 0.7374,
  "label": "This looks like it may have been written with AI. We could be wrong. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "1dbe0ff2-bec7-4a50-aee8-b9cc86a975a4",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4574,
  "model_score": 0.6175,
  "style_score": 0.2973,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "edd05358-6f52-4188-b86d-56151340894d",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7432,
  "model_score": 0.7387,
  "style_score": 0.7477,
  "label": "This looks like it may have been written with AI. We could be wrong. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "f0bab6be-8dce-468a-8f91-a5e213892441",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.5014,
  "model_score": 0.8051,
  "style_score": 0.3976,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "4584b417-5a00-43b7-910f-4fe81190f452",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7289,
  "model_score": 0.8329,
  "style_score": 0.625,
  "label": "This looks like it may have been written with AI. We could be wrong. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "58b7e08d-9ef3-4c38-b68e-ac02d7e15859",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7776,
  "model_score": 0.8005,
  "style_score": 0.7547,
  "label": "This looks like it may have been written with AI. We could be wrong. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "d303dd4d-b479-468b-bed5-bc1a729e3e1c",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.4659,
  "model_score": 0.8814,
  "style_score": 0.2504,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "17d049e4-8f07-490e-afd0-8c9ec5de161e",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.4738,
  "model_score": 0.8816,
  "style_score": 0.2661,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "72c1ad9b-fba3-4955-b463-d25e2d716ab3",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4112,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "b41a5f1b-c184-466d-849f-b7c50bca91a1",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4563,
  "model_score": 0.4625,
  "style_score": 0.45,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "ebecb9ce-44ad-43d3-a76f-7f95be9e58de",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.305,
  "model_score": 0.2044,
  "style_score": 0.4056,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "69ebf62c-91db-4158-8bd6-d4035ae39f9b",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.526,
  "model_score": 0.5943,
  "style_score": 0.4577,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "0beb887e-d53a-4056-81c5-02427bf94bf0",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.3604,
  "model_score": 0.4998,
  "style_score": 0.2211,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "bce3cb37-b431-4ef0-9bae-76add5b09bab",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.3129,
  "model_score": 0.6401,
  "style_score": 0.1857,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "941289b9-317c-48e6-af46-4fced21ff69b",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4329,
  "model_score": 0.5583,
  "style_score": 0.3074,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "7cc288ea-7826-483b-b3ea-ac37cc18ffc5",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.15,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "44f597a7-d533-4ea2-880d-9efd1bf749b0",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.1556,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "66c00904-9b6f-40b0-b38f-94659300f3e4",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.6488,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "54cef2cc-c41c-4b5d-9ba4-f5f378c4ceda",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.6485,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "55684921-9a84-485c-b569-84cd7d053c67",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.6032,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "9fb5a5ae-66a2-4105-88fe-2f65a0addb09",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "e08d4e20-c839-42bd-af06-88bea022d1a3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "be7a0b45-a419-4e7c-916a-19ceb4fe5d8a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "a699bd5f-0614-49d7-8338-9ae37ef74081",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "ed8e1593-dc13-4280-afe2-2a065290a903",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "5eea64e0-1f82-437e-a272-96be75aaf54c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "5dd0aac2-4ef0-40a0-b7ad-3235ab12985d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "0648c073-c172-46c5-a1b8-960ceb71b423",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "f4b1f791-1628-4eb8-b9b4-d5d16174dced",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "ab431ce4-3d53-4c8f-bb93-ac137f36b138",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
