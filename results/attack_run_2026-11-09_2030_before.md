# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 20:30
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `ea6acead-7b74-4383-925a-6159c13ca082` | human | 0.335 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `69356467-0b30-4c3b-80bf-bdce025dfb5b` | unsure | 0.514 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `ce137806-9fca-403c-9fe3-5477432f3137` | unsure | 0.499 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `112221ed-8272-4c47-8195-385d25d33073` | unsure | 0.649 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `6723475a-5d99-4cf5-a442-2130a909b6fd` | human | 0.331 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `9765336b-f1b9-458f-8796-e498a167bb80` | unsure | 0.523 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `b7167ee9-7a07-42a9-a9b4-7c6cf8eb972e` | unsure | 0.543 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `a029f775-fc75-4e73-8753-73a6adb5b41a` | unsure | 0.373 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `b94be5aa-a456-44f1-aab2-8e632bda306e` | unsure | 0.369 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `64a4c5a5-d43c-4a6a-9307-d2239aceb797` | ai | 0.858 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `419e2573-6c16-4334-8671-bc3d7cc3c849` | unsure | 0.457 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `8d2f9430-f220-4b8f-80b5-16ac9dbe4f30` | ai | 0.743 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `9b9ec54b-8551-4170-8c39-05d1ff438bbb` | unsure | 0.501 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `175a2e8d-31e8-48e7-b837-a53aa28be1b1` | ai | 0.729 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `7440a999-a16d-4eb5-9e27-b573f997b796` | ai | 0.778 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `5a48e91a-84ca-4ef5-b042-73d567fc52fd` | unsure | 0.466 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `f5dfb10c-ddac-4c0b-a03e-514d32d4aee4` | unsure | 0.474 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `d9a0b10d-0d11-4a26-a1c0-dbded512d892` | unsure | 0.411 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `56e5d502-2b48-40ec-b3f0-9bdcbbfcf989` | unsure | 0.456 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `048e5ce5-f5fa-4b76-a583-116876cd75c1` | human | 0.305 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `fefe0fe8-3d46-49ca-97f0-42d50631fcbf` | unsure | 0.526 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `f1b1d7dc-d7ba-46db-938c-dcceded94ed1` | unsure | 0.360 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `8c3b65a0-5493-4423-b63c-1a3f498fd5d9` | human | 0.313 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `ae558eb4-78ef-424f-bdf9-fce66b897a22` | unsure | 0.433 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `6a361329-0fb6-48d8-8de7-5e82f6a77a71` | human | 0.150 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `71c4c6bf-2bda-415f-816f-cc0846d22bdf` | human | 0.156 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `a38bc78b-f6da-48f3-9cd2-d7c70836fd33` | unsure | 0.649 | HELD |
| MF06 | malformed | text is emoji only | 200 | `2bdd1bdf-0979-4db2-a37e-fefc1acd1d2f` | unsure | 0.648 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `a333f2fb-309f-45c2-ac32-3be46fe67152` | unsure | 0.603 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | `4cbc0e65-49b7-4a5b-8abe-65779475ba02` | unsure | 0.591 | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9c2145fd-ba2b-40a2-a356-0bf1961d3405` | human | 0.164 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a66ef286-4b7e-4130-a305-02437a86dbb6` | human | 0.164 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `02516728-163a-434f-9f44-d9ffac7d110d` | human | 0.164 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a7e80c00-362a-4f2b-9e09-82b10ab0aa3b` | human | 0.164 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3e7374c1-3edf-4165-b7ea-d195ca8d198c` | human | 0.164 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9ae341a9-8c24-4534-92d7-cb19befd7e64` | human | 0.164 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7d90d861-d3cf-4aa3-821b-13345b872836` | human | 0.164 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6dfc9c61-4d30-4c72-b84a-1d4f67e66ab7` | human | 0.164 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1b225aca-4dfd-4d75-986f-8024f8e23c4a` | human | 0.164 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dcd3c259-8d61-49af-a170-02886dff11db` | human | 0.164 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
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
  "content_id": "ea6acead-7b74-4383-925a-6159c13ca082",
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
  "content_id": "69356467-0b30-4c3b-80bf-bdce025dfb5b",
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
  "content_id": "ce137806-9fca-403c-9fe3-5477432f3137",
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
  "content_id": "112221ed-8272-4c47-8195-385d25d33073",
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
  "content_id": "6723475a-5d99-4cf5-a442-2130a909b6fd",
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
  "content_id": "9765336b-f1b9-458f-8796-e498a167bb80",
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
  "content_id": "b7167ee9-7a07-42a9-a9b4-7c6cf8eb972e",
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
  "content_id": "a029f775-fc75-4e73-8753-73a6adb5b41a",
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
  "content_id": "b94be5aa-a456-44f1-aab2-8e632bda306e",
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
  "content_id": "64a4c5a5-d43c-4a6a-9307-d2239aceb797",
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
  "content_id": "419e2573-6c16-4334-8671-bc3d7cc3c849",
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
  "content_id": "8d2f9430-f220-4b8f-80b5-16ac9dbe4f30",
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
  "content_id": "9b9ec54b-8551-4170-8c39-05d1ff438bbb",
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
  "content_id": "175a2e8d-31e8-48e7-b837-a53aa28be1b1",
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
  "content_id": "7440a999-a16d-4eb5-9e27-b573f997b796",
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
  "content_id": "5a48e91a-84ca-4ef5-b042-73d567fc52fd",
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
  "content_id": "f5dfb10c-ddac-4c0b-a03e-514d32d4aee4",
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
  "content_id": "d9a0b10d-0d11-4a26-a1c0-dbded512d892",
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
  "content_id": "56e5d502-2b48-40ec-b3f0-9bdcbbfcf989",
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
  "content_id": "048e5ce5-f5fa-4b76-a583-116876cd75c1",
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
  "content_id": "fefe0fe8-3d46-49ca-97f0-42d50631fcbf",
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
  "content_id": "f1b1d7dc-d7ba-46db-938c-dcceded94ed1",
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
  "content_id": "8c3b65a0-5493-4423-b63c-1a3f498fd5d9",
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
  "content_id": "ae558eb4-78ef-424f-bdf9-fce66b897a22",
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
  "content_id": "6a361329-0fb6-48d8-8de7-5e82f6a77a71",
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
  "content_id": "71c4c6bf-2bda-415f-816f-cc0846d22bdf",
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
  "content_id": "a38bc78b-f6da-48f3-9cd2-d7c70836fd33",
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
  "content_id": "2bdd1bdf-0979-4db2-a37e-fefc1acd1d2f",
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
  "content_id": "a333f2fb-309f-45c2-ac32-3be46fe67152",
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
  "status": 200,
  "content_id": "4cbc0e65-49b7-4a5b-8abe-65779475ba02",
  "creator_id": "attacker_MF08",
  "guess": "unsure",
  "confidence": 0.5914,
  "model_score": 0.9876,
  "style_score": 0.3951,
  "label": "We can't tell for sure whether this was written by a person or by AI.",
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
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
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
  "content_id": "9c2145fd-ba2b-40a2-a356-0bf1961d3405",
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
  "content_id": "a66ef286-4b7e-4130-a305-02437a86dbb6",
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
  "content_id": "02516728-163a-434f-9f44-d9ffac7d110d",
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
  "content_id": "a7e80c00-362a-4f2b-9e09-82b10ab0aa3b",
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
  "content_id": "3e7374c1-3edf-4165-b7ea-d195ca8d198c",
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
  "content_id": "9ae341a9-8c24-4534-92d7-cb19befd7e64",
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
  "content_id": "7d90d861-d3cf-4aa3-821b-13345b872836",
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
  "content_id": "6dfc9c61-4d30-4c72-b84a-1d4f67e66ab7",
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
  "content_id": "1b225aca-4dfd-4d75-986f-8024f8e23c4a",
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
  "content_id": "dcd3c259-8d61-49af-a170-02886dff11db",
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
