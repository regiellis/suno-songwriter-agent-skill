# Songwriting And Fusion Evaluation

This benchmark tests whether the skill makes useful songwriting decisions across forms and genre blends. It uses 16 self-contained briefs with synthetic original lyrics where needed. It needs no real song drafts, Suno recordings, or observed before/after pairs.

Status: authored, not run. Dataset validation is not a behavioral pass. No evaluation scores or model comparisons have been collected for this suite.

## Files And Scope

- `cases.json`: prompts, required constraints, quality targets, and failure signals.
- `rubric.json`: shared score definitions and the result format.
- `../../references/evals.md`: broader manual smoke tests; this benchmark focuses on writing quality and fusion.

The evaluation measures text decisions: preserving voice and constraints, developing material, distinguishing forms, combining styles, and handling evidence. It does not measure rendered melody, groove, mix quality, pronunciation, or actual musical originality across the world's repertoire. It also does not test automatic skill discovery; the generation run explicitly receives the skill.

Keep the benchmark outside the installable skill ZIP. The agent answering a case must not receive grading targets, examples from evaluation reports, other candidates' outputs, or prior results.

## Run A Case

1. Snapshot the candidate's `SKILL.md` and runtime references. Record the revision or hashes; a dirty working tree needs hashes or an immutable copy, not only a Git commit identifier.
2. Start a fresh generation session with the candidate skill available. Use the same model, tool access, and generation settings for every candidate being compared. Do not carry earlier case responses into the next case.
3. Give the agent only the setup below and the case's `prompt` value. Read access to the skill's relevant music references is allowed. Evaluation files and `references/evals.md` are excluded from the generation context.
4. Save the entire response without editorial cleanup. Preserve punctuation, added notes, and any refusals or questions because they are part of the behavior being tested.
5. Grade in a separate session using the judging instructions below. Save the judge's structured result alongside the untouched response and run metadata.

Generation setup, with the path substituted for the current candidate:

```text
Use the suno-songwriter skill at PATH_TO_CANDIDATE/SKILL.md to answer
this request. You may read its relevant music references. Do not read
evaluation datasets, evaluation reports, or references/evals.md.
Do not generate audio, browse, or modify files. All task inputs are
in the request. Answer using the available information; distinguish
text-level judgments from audio verification.
```

Then append only the case's prompt. Do not append `must`, `quality_targets`, `failure_signals`, or this protocol. Those are for the judge.

No executable runner or provider adapter is included. A harness can load `cases.json` and follow this protocol with its own session API; a person can run the same steps manually. Do not claim an independent run when the author simply reviews their own drafted response.

## Judge Independently

Give a fresh judge the following:

- The original user prompt.
- The unedited candidate response under an anonymous label.
- The global requirements, that case's `must`, `quality_targets`, and `failure_signals`.
- The shared rubric from `rubric.json`.

Do not give it the candidate identity, skill revision, baseline label, intended winning answer, or editing history. The judge does not need the candidate's skill instructions to decide whether the delivered answer works.

Judge instruction:

```text
Evaluate the response to the supplied songwriting request using the
provided constraints and rubric. Assess the delivered text, not what
an audio model might produce. Cite short passages or precise omissions
for each score. Do not reward length, jargon, genre-tag count, or an
explanation when the user requested only lyrics. Multiple musical
solutions can be valid; the quality targets are not a gold answer.

Evaluate every must-have constraint separately. Mark uncertainty when
a judgment needs audio, missing context, or specialist knowledge.
Do not convert an unsupported specialist judgment into a failure.
Return the result format defined in rubric.json. Do not repair the
candidate's answer before grading it.
```

Use a separate session at minimum. A different judge model or qualified human reviewer adds perspective, but neither is an automatic ground truth. For specialist language or musical-system questions, escalate uncertainty for knowledgeable review rather than forcing a confident score.

## Scoring

Score each dimension from 0 to 4 using the anchored definitions in `rubric.json`:

- Song craft and development.
- Musical identity and integration.
- Phrasing and feasibility.
- Deliverable usefulness and scope.

Evaluate constraints independently of the numeric scores. Exact-content violations, prohibited sections, unsupported audio claims, or long-dash output must not be hidden by a high average. `must` entries are required; quality targets describe useful evidence and permit alternate valid solutions. A failure signal is a diagnostic cue, not automatically a failure if the user's intent is still met.

A provisional case pass requires all constraints to pass, every dimension to score at least 3, and no unresolved grading uncertainty. Mark ambiguous cases `needs_review`. These thresholds are an initial convention, not a calibrated predictor of musical quality.

A requested artifact without explanation can earn full scores when its musical decisions are visible in the artifact. For an instrumental plan, score motif and arrangement development instead of lyric imagery. Do not penalize a chorus-free form for lacking a chorus or reward a dense lyric merely for using complex rhyme.

## Deterministic Checks

Every response can be scanned for U+2014 and U+2013. Some cases also include `required_text` or `exact_occurrence_count` checks. These check strings only; they do not verify section position, absence of unrelated rewrites, musical quality, or semantic constraints.

For SW01, required-text presence is not enough: the judge must verify that the response changed only lyric line 2. For SW02, three occurrences of the refrain must also be the final lines of three four-line stanzas. For MX03, compare both returned lyric blocks with the supplied words, excluding section labels and explanatory prose. Do not count a quotation in an explanation as successful preservation of the lyric.

The X02 input intentionally contains em/en dashes. The output must normalize them. They are escaped in JSON source so the authored prompt and the output policy can be distinguished.

## Compare Revisions

For a first check, run all 16 cases once. For a stronger comparison, use three fresh attempts per case and revision with matched settings. Record the chosen run count before seeing outputs; do not keep only the strongest takes.

Compare a baseline and a candidate using the same prompts and environments. Anonymous pairwise review can supplement absolute scores: randomize A/B display order and permit ties. Reversing order on a sample helps detect presentation bias. A no-skill baseline measures a different question from an older-skill baseline; label them separately.

Report:

- Attempt count and completeness, including failures and missing responses.
- Constraint-pass rate and per-dimension score distributions.
- Outcomes by form and task, not only one aggregate number.
- Regressions where the baseline met a constraint and the candidate failed it.
- `needs_review` and judge disagreements separately from passes and failures.

Do not declare improvement from one attractive example. Calibrate the rubric against human review as responses accumulate. Keep a few new, unpublished briefs for a later holdout pass so repeated editing against this public suite does not become the only test.

## Run Record

Store raw responses and judgments in a separate results directory chosen by the operator. Record suite version, case ID, attempt, candidate snapshot, generation model/settings, judge model/settings, tool access, and errors. Record unavailable settings as unknown rather than inventing values. Preserve reports even when a run fails.

A report must distinguish dataset checks, self-review, independent text evaluation, and listening evidence. Only update the evaluation record with results that were actually collected.
