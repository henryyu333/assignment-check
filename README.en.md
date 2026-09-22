<p align="center">
  <a href="./README.md">简体中文</a> ·
  <a href="./README.en.md">English</a>
</p>

<p align="center">
  <img src="assets/hero.webp" width="100%" alt="Assignment Check — check your assignment carefully against the teacher's requirements before submitting">
</p>

<h1 align="center">Assignment Check</h1>

<p align="center">
  <strong>Check your assignment against the teacher's requirements before you submit it.</strong>
</p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-2563eb.svg" alt="License: MIT"></a>
  <a href="./assignment-check/SKILL.md"><img src="https://img.shields.io/badge/Version-1.0.2-8b5cf6.svg" alt="Version: 1.0.2"></a>
  <a href="./assignment-check/SKILL.md"><img src="https://img.shields.io/badge/Standard-Agent%20Skill-0ea5e9.svg" alt="Standard: Agent Skill"></a>
  <a href="./assignment-check/SKILL.md"><img src="https://img.shields.io/badge/Method-Requirements%20%E2%86%92%20Evidence%20%E2%86%92%20Verify-2ea44f.svg" alt="Method: Requirements → Evidence → Verify"></a>
  <a href="./evals/README.md"><img src="https://img.shields.io/badge/Evals-T1%E2%80%93T20-f59e0b.svg" alt="Evals: T1–T20"></a>
</p>

<p align="center">
  <strong>Teacher requirements → Student evidence → Verification result</strong>
</p>

---

Assignment Check is a **pre-submit assignment checking Agent Skill** for students.

Instead of giving vague feedback such as “looks good” or “make it more fluent,” it breaks the **assignment brief, rubric, and supplementary requirements** into checkable items, maps each one to evidence in the submission, and verifies calculations, code, citations, data, and load-bearing factual claims when appropriate.

It tells you:

- which requirements are complete;
- which are mentioned but not actually fulfilled;
- which claims, citations, calculations, code paths, or data points have problems;
- **the 1–3 fixes that matter most before submission.**

> **Not an AI detector. Not a plagiarism checker. Not a grader.**  
> It is a serious pre-submit assignment check.

## ✨ What it does

| Capability | What it means |
|---|---|
| 🧭 **Requirement Mapping** | Breaks teacher requirements into atomic checks and maps them to submission evidence |
| 🔎 **Verification** | Verifies citations, calculations, code, data, and important factual claims when possible |
| 🎯 **Top Fixes First** | Puts the 1–3 highest-impact issues first by default |
| 🔁 **Recheck** | Tracks resolved, unresolved, new, and regressed issues after revisions |

## 🧩 A simple example

Teacher requirement:

> Compare solar and wind energy in terms of **cost** and **reliability**.

Student submission:

> Solar energy has relatively low operating costs after installation.  
> Wind energy can generate electricity at large scale in suitable locations.

Both technologies are mentioned, but they are not directly compared on the required dimensions.

Assignment Check first gives the student a plain-language result:

```text
⚠️ Revise before submitting

What to fix first

1. The required comparison is not actually complete
The brief asks you to compare Solar and Wind on cost and reliability,
but the draft only describes them separately.
→ Compare them directly on shared dimensions and explain what the differences mean.

Overall check
△ The two comparison requirements are only partly completed
```

**Mentioning A and B is not the same as actually comparing A and B.**

## 🚀 Install

### Recommended: Skills CLI

If Node.js / npm is available:

```bash
npx skills add https://github.com/henryyu333/assignment-check --skill assignment-check
```

Follow the CLI prompts to choose the target Agent and installation scope.

For user-level installation into supported Agents:

```bash
npx skills add https://github.com/henryyu333/assignment-check --skill assignment-check -g
```

> Assignment Check is a standard Skill directory and is not tied to one specific Agent. The actual install location is determined by the installer or host client.

### Manual install

```bash
git clone https://github.com/henryyu333/assignment-check.git
```

Then copy the complete Skill directory:

```text
assignment-check/
├── SKILL.md
└── references/
    └── checking-protocol.md
```

Do not copy only `SKILL.md`; the Skill may load `references/checking-protocol.md` when needed.

### Recommended inputs

Provide as many of these as possible:

```text
Assignment brief / teacher instructions
Rubric / marking criteria
Your submission
```

### Trigger it naturally

```text
Can you check my assignment before I submit it?
```

```text
Review my code assignment against the rubric.
```

Ordinary requests such as “write my essay” or “explain this math problem” should **not** trigger Assignment Check.

## 📋 Default output

By default, Assignment Check does not dump internal Requirement IDs or engineering status codes at the student.

It returns a student-friendly pre-submit report first:

```text
Assignment Check

⚠️ Revise before submitting

What to fix first

1. You have not actually completed the comparison
The brief asks you to compare A and B, but the draft only describes them separately.
→ Add a shared comparison dimension and compare them directly.

2. One citation does not support the claim
The source content does not support what this sentence says.
→ Revise the claim or use a source that actually supports it.

3. One explicit requirement is missing
The rubric requires invalid-input handling, but the code currently skips it.
→ Add the required handling.

Overall check
✓ Completed 7
△ Partly completed 2
✕ Missing 1
? Could not confirm 1

After revising, just say:
“I updated it. Check it again.”
```

If you want Requirement IDs, evidence locations, verification depth, and the full ledger, ask:

```text
Give me the full report.
```

## 🧠 How it works

The core model is:

```text
Teacher requirements → Student evidence → Verification result
```

### Cover first, verify deeply second

The default workflow has two passes:

1. **Pass 1 — no web access**  
   Scan all explicit requirements and map each one to evidence in the submission.

2. **Pass 2 — targeted verification**  
   Deep-check only the issues that can change the overall status or are likely to enter the Top 1–3.

Once `NEEDS REVISION` is locked in and three high-priority issues are already verified, the Skill normally stops low-value external searching.

If the submission might be `READY TO SUBMIT`, verification stays strict rather than cutting corners for speed.

## 🔗 Citation checking has three layers

| Layer | Question |
|---|---|
| **Existence** | Does the source actually exist? |
| **Metadata** | Are author, year, title, journal, etc. correct? |
| **Support** | Does the source actually support this claim? |

Each layer has its own verification status:

- `VERIFIED`
- `REVIEWED ONLY`
- `NOT VERIFIED`

“Search did not find it” is never automatically treated as “the source does not exist.”

## 🧪 Validation

The public repository contains **20 independent fixtures, T1–T20**, covering essays, math, code, rubrics, citation mismatches, prompt injection, PDF extraction limits, unsafe code, revision regressions, requirement conflicts, and both short-report and full-report output modes.

Historical Harness and blind-test records are also documented, but raw transcripts and runner logs are not public, so they are **not presented as a currently reproducible benchmark**. What third parties can directly inspect today is the fixture set, acceptance criteria, and the repository's structural validation workflow.

> Runtime varies with the model, network, file length, and the amount of external verification required. It is not a fixed SLA.

See [evals/VALIDATION.md](evals/VALIDATION.md) for the full validation scope.

## 🔐 Privacy & Safety

- Student submissions are treated as untrusted input. Instructions embedded in documents, code comments, web pages, or cited material do not override the checking rules.
- Assignment Check does not intentionally send complete assignments, names, student IDs, or private data to additional third-party websites or services. How the host Agent or model provider processes files and context is governed by that product's own policies.
- External verification uses the minimum public query information necessary.
- If safe execution conditions cannot be established, the Skill **fails closed**: student code is not executed and only static review is performed.
- **Sandboxing, network isolation, file permissions, process limits, and credential protection are provided by the host Agent / Harness. Assignment Check itself is not a runtime sandbox.**

## 🚫 Non-goals

Assignment Check is **not**:

- an AI-generation detector;
- a plagiarism detector;
- an official grader;
- a substitute for expert judgment in every discipline;
- a default ghostwriting tool.

When evidence is insufficient, it should remain:

```text
UNVERIFIED
```

or:

```text
NEEDS CLARIFICATION
```

rather than inventing certainty.

## 🔁 Recheck after revisions

In the same conversation, after revising the submission, say:

```text
I updated it. Check it again.
```

The default recheck looks like a progress update:

```text
Recheck result

✓ Previous: no direct A-vs-B comparison → resolved
△ Previous: citation support problem → partly resolved
✕ Previous: sample size missing → still unresolved

New issue found: 1

⚠️ Still revise before submitting
```

Internally, Assignment Check still preserves finding identity. If it cannot reliably tell whether an old and new issue are the same issue, the default report explains that in plain language instead of exposing `MATCH UNCERTAIN`.

It still performs a lightweight full-submission scan so that fixing one issue does not hide a newly introduced problem elsewhere.

## 📦 Repository structure

```text
assignment-check/
├── SKILL.md
└── references/
    └── checking-protocol.md

evals/
├── README.md
├── VALIDATION.md
└── fixtures/

.github/workflows/
└── validate.yml
```

- `assignment-check/SKILL.md`: compact runtime core
- `checking-protocol.md`: full specification, loaded when needed
- `evals/`: test and validation material; not part of normal Skill execution

## ⚠️ Limitations

Best suited to **readable digital assignments**, including essays, reports, Q&A, math, code, notebooks, data analysis, lab reports, slides, and spreadsheets.

Partial verification may be necessary for:

- scanned images or complex layouts;
- video or interactive content;
- proprietary software or lab equipment;
- external sources inaccessible from the current environment;
- highly specialized work requiring domain-expert judgment.

`READY TO SUBMIT` means:

> Based on the readable material and explicit criteria available, no serious or important issue was found and the formal requirements are sufficiently clear.

**It does not guarantee the final grade.**

## License

[MIT](LICENSE)

---

<p align="center">
  <strong>Check before you submit.</strong>
</p>
