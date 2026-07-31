---
name: suno-songwriter
description: Voice spec for the suno-songwriter skill's prose (SKILL.md, references, README, docs).
voice: technical
context: docs
register:
  first_person: false
  em_dash: forbid
allow:
  - underscore
---

# Project voice

How prose in this repo should sound: instruction files an agent executes (`SKILL.md`, `references/`), plus reader-facing docs (`README.md`, `docs/`, release notes).

## Voice

Direct, imperative, and dense. Short declarative rules over explanations. Every claim is operational: a reader should be able to act on the sentence. Example: "Set Custom 5-15s longer than the intended cut so the ending resolves, then Crop to the exact time."

## Audience

Agents executing the skill, and the musicians who install it. Both want the rule and the reason in one pass, no warm-up.

## Vocabulary

- **Allow `underscore`**: in this repo it is the musical term for background scoring, not the Tier-1 filler verb.
- Suno UI terms are proper nouns and keep their casing: Style, Excluded Styles, Weirdness, Style Influence, Duration, Extend, Crop, Replace Section, Voices, Custom Models, My Taste.
- No Tier-1 filler (seamless, robust, leverage, comprehensive, delve). Say the concrete thing.

## Punctuation and formatting

- No em-dash or en-dash anywhere, including code blocks, example prompts, and taught Suno tag syntax; section-tag descriptors use a plain hyphen: `[Chorus - double-time house flip]`. Numeric ranges use a plain hyphen: `86-96 BPM`.
- Semicolon-dense rule lists are this repo's native cadence for instruction files; the detector's "semicolons at dash cadence" flag is accepted here, not a defect to fix.
- Title Case headings are the repo convention in every doc; the sentence-case default is waived.
- Bold list labels end with a colon, not a period: `- **Label:** rule.`

## Do's and don'ts

- Do write rules an agent can execute verbatim; prefer exact field names and commands.
- Do keep examples genre-diverse; never let one palette recur (see the skill's own anti-lock-in rule).
- Don't add hedges, throat-clearing, or "it is worth noting."
- Don't rewrite quoted Suno syntax or field names to satisfy a style rule; the platform's spelling wins.
