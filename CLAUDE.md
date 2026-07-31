# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

This is an **agent skill** (no application code, no build system). It packages instructions and reference material that teach an agent harness how to produce Suno v5.5-ready song packages: hook-first vocal lyrics, instrumental prompts/arrangements, vocal `Style`/`Excluded Styles` prompts, vocal/custom slider suggestions, and multilingual adaptations. The skill is harness-agnostic — anything that can read `SKILL.md` and selectively load `references/` can use it.

The git repo is named `suno-songwriter-agent-skill`; the working directory and skill name are both `suno-songwriter`. The skill name in `SKILL.md`'s frontmatter is canonical.

## Architecture

Progressive disclosure is the core design constraint:

- **`SKILL.md`** — the always-loaded entry point. Contains the YAML frontmatter (`name`, `description`) used for trigger matching, the core workflow, the output contract, and a routing table pointing to `references/`. Keep this file concise; deeper guidance belongs in a reference file.
- **`references/templates.md`** — the routing index. Every other reference file must be listed here. When you add a reference file, update both `templates.md` and the routing list near the top of `SKILL.md`.
- **`references/*.md`** — focused, independently-loadable topic files (output skeletons, Suno controls, Suno meta-tags, Suno sounds/samples, cover art/animated covers, studio/iteration, songwriting craft, song structure, rule-of-3, 80/20, instrumental, screen music, multilingual, style selection, genre palettes, remix/style-match, personas, albums, evals). A harness loads only the ones relevant to a request. Prefer adding a new narrow file over growing an existing one. Note: `personas.md` and `albums.md` instruct the agent to write spec `.md` files into the *user's* working directory (`personas/<slug>.md`, `albums/<slug>.md`) — not into this repo.
- **`agents/openai.yaml`** — harness-specific metadata only. Portable behavior stays in `SKILL.md`/`references/`; product-specific config stays under `agents/`. Other harnesses get their own file (`agents/claude.yaml`, etc.) — do not put harness-specific behavior in `SKILL.md`.

The skill's output contract is defined in `SKILL.md` and mirrored in `references/output-templates.md` — vocal songs use Title / Style / Excluded Styles / Lyrics, while instrumentals use Title / Instrumental Prompt / Arrangement. Optional Language Notes / Suno v5.5 Notes / Slider Suggestions / Checks apply only when useful and supported by the mode.

## Validation

There is no test runner. Validate changes with:

```bash
# YAML frontmatter / metadata parse check
ruby -e 'require "yaml"; YAML.load_file("SKILL.md"); YAML.load_file("agents/openai.yaml"); puts "YAML OK"'

# Compare source against the installed copy
diff -rq SKILL.md /Users/rellis/.agents/skills/suno-songwriter/SKILL.md
diff -rq references /Users/rellis/.agents/skills/suno-songwriter/references
```

`references/evals.md` holds the manual smoke-test matrix (should-trigger queries, should-not-trigger queries, regression checks, output rubric). Run those by hand when changing trigger wording or the output contract.

## Installed Copy

This repo is the source. An active installed copy may live at `/Users/rellis/.agents/skills/suno-songwriter`. After editing source, sync it:

```bash
cp SKILL.md /Users/rellis/.agents/skills/suno-songwriter/SKILL.md
rm -rf /Users/rellis/.agents/skills/suno-songwriter/references
cp -R references /Users/rellis/.agents/skills/suno-songwriter/references
cp agents/openai.yaml /Users/rellis/.agents/skills/suno-songwriter/agents/openai.yaml
```

## Content Conventions (when editing the skill's guidance)

These are rules the skill itself enforces; keep them consistent across `SKILL.md` and `references/` so the guidance doesn't contradict itself:

- The `description:` frontmatter field in `SKILL.md` must be **≤ 1024 characters** and contain **no angle-bracket / XML-style tags** (e.g. `<artist>`). Some harnesses (Claude Desktop) reject the skill otherwise. Use plain prose for trigger examples ("making something sound like a given artist"), not `<placeholder>` syntax.
- `Style:` is a positive prompt capped at ~200 characters for vocal/custom modes; negative direction goes in `Excluded Styles:`, not as `no...` phrases crammed into `Style:`.
- Instrumental Mode does not expose Style, Excluded Styles, or sliders. Instrumental tracks return `Instrumental Prompt:` plus `Arrangement:` with cue-style tags (`[Theme A]`, `[Build]`, `[Loop Point]`, …) instead of `Lyrics:`.
- Sections are 4 lines or a multiple of 4 unless the genre/request says otherwise.
- Vocal lyrics must pass the quality gate before output: title/hook in or near the chorus, mechanically simpler chorus than verses, stable POV/tense, at least one concrete human detail, and no obvious mouthful lines.
- Sliders are expressed as ranges (Weirdness, Style Influence), never false-precise single values, and are not returned for Instrumental Mode.
- Style Diversity / anti-lock-in: examples must not converge on one recurring palette (the skill explicitly bans defaulting to things like `cinematic alt-R&B`, `gospel pads`, `warm male vocal`, `piano and strings`). New examples should span different genres.
- Anti-generic word list (`neon`, `fire`, `flames`, `shadows`, `echoes`, `broken`, `fading`, `forever`, …) is avoided in generated lyrics unless the user asks for them.
