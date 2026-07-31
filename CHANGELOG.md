# Changelog

## v1.2.1: 2026-07-31

### Changed

- Kiko prose sweep across `SKILL.md` and all of `references/`: removed 200+ em-dashes (rewritten as colons, commas, parentheticals, or sentence splits), unified numeric ranges and taught Suno tag syntax on plain hyphens, replaced `seamlessly` and `genuinely` filler, and converted bold list labels from period to colon form. Added `KIKO.md` recording the repo voice and carve-outs (Title Case headings, `underscore` as a musical term, semicolon-dense rule lists).

## v1.2.0: 2026-07-31

### Added

- MIT license: `LICENSE` filled in and `license: MIT` added to `SKILL.md` frontmatter (Claude Desktop displays it on upload).
- Release packaging: `suno-songwriter.zip` attached to GitHub releases, containing the skill folder at the zip root (the layout Claude Desktop's skill upload and Codex's `~/.codex/skills/` both expect). README and docs gained per-app install instructions for Claude Desktop, Codex (app and CLI), and Claude Code.
- `docs/`: GitHub Pages documentation site: a single self-contained static page covering the output contract, workflow, modes, Suno v5.5 controls, and the reference index. README gained a Documentation link and generic install paths; README cleaned with kiko (em-dash removed).
- `references/genre-fusion.md`: multi-genre handling: fusion blends built as anchor + accent, mid-song genre switches cued in both `Style:` and section tags, and same-song genre versions with per-version Style/sliders and singability re-checks. Routed from `SKILL.md`, `references/templates.md`, and `references/genre-palettes.md`; smoke tests V5/V6 added to `references/evals.md`.

### Fixed

- Documented v5.5's Duration control (user-verified in the UI: Auto, or a Custom slider 0:10-6:00 in 5-second steps): recommend Custom for target cuts, match the written structure to the set time, add 5-15s headroom so the ending resolves, Crop to exact length. Noted in `SKILL.md` § Creative Sliders and the output contract's `Slider Suggestions:`, `references/suno-v55-controls.md` § Duration, and `references/screen-music.md` § Edit-Length Guidance. Also added the missing cross-genre fusion row to the Slider Recipes table that `references/genre-fusion.md` points to.
- Refreshed the Suno v5.5 currency stamp (v5.5 still current as of 2026-07; no v6) in `SKILL.md`, and recorded the model version stamp in `CLAUDE.md`.

- Tightened `SKILL.md` around hook-first lyric quality so vocal requests prioritize a strong song over a complete form: clear title/hook, simpler chorus, stable POV/tense, concrete detail, and singable line lengths.
- Shortened the trigger description and OpenAI default prompt to reduce metadata bloat and avoid steering every request into optional notes, sliders, and checks.
- Synced `references/output-templates.md`, `references/screen-music.md`, `references/evals.md`, `README.md`, and `CLAUDE.md` with the optional-field contract and lyric quality gate.
- Corrected Instrumental Mode guidance: Suno instrumentals use `Instrumental Prompt:` plus `Arrangement:`, not `Style:`, `Excluded Styles:`, or slider suggestions.
- Added a Suno-native lyric default: compact 4-line sections, short singable lines, plain rhyme, strong hook repetition, and optional performance descriptors in section tags.
- Added groove-narrative vocal mode for neo-soul/R&B/jazz-hop/spoken-sung songs with longer rhythmic verses, environmental arrangement cues, vocalist labels, spoken bridges, and simple chanted choruses.

## v1.1.0: 2026-05-12

### Added

- `references/cover-art.md`. Suno's **Generate Cover Art** / **Animate** tools: the three paths (text-to-image, text-to-video, image-to-video), controls and limits (Quality Mode, 5s/10s length, 1:1 square-only, ~800-char prompt fields, motion prompt, ~2 variants, ~5-min generation), matching the visual to the song's lane/era/mood/key image (and to a persona/album visual identity), image-prompt craft (subject/composition → medium/style → palette → lighting → mood; no text, logos, or real artist/character names; same filter logic as `Style:`), motion-prompt craft (motion only, loop-friendly, no morphing faces/hands or hard cuts), the `Cover Concept:` / `Image Prompt:` / `Motion Prompt:` / `Settings:` output shape plus the `Cover Art:` block appended to a song package, anti-AI-art-cliché guidance, and where it stops (full multi-scene music videos → external editor; Suno Scenes camera→song → normal song contract).
- `SKILL.md`: new "Cover Art And Animated Covers" section; routing entry; expanded frontmatter description (cover art / animated covers, plus a `cover art` casual trigger), trimmed elsewhere to stay ≤ 1024 chars.
- Wiring: `references/templates.md`, `README.md` (What It Covers, Files, Reference Loading Guide), `CLAUDE.md` (architecture reference list); `references/evals.md` smoke-test rows (CV1, CV2), should-trigger queries, and a regression check; synced to installed copy.

## v1.0.1: 2026-05-12

### Fixed

- `SKILL.md` `description:` frontmatter rewritten to **1019 characters** (was ~1900) and stripped of the `<artist>` angle-bracket token, so harnesses that validate the field (Claude Desktop) accept the skill. Trigger coverage preserved in plain prose. Documented the ≤ 1024-char / no-XML-tags constraint in `CLAUDE.md`.

## v1.0.0: 2026-05-12

First tagged release. Full surface: write / revise / remix lyrics; instrumentals; screen music (anime OP/ED, TV themes, trailers, idents, game themes); multilingual (incl. Korean lanes beyond K-pop); Suno controls, meta-tags, sliders, content filters, and Studio/iteration workflow; style-match ("in the style of X"); reusable artist personas; cohesive albums/EPs; and Suno Sounds (custom audio samples). Progressive-disclosure architecture: concise `SKILL.md` + 19 independently-loadable `references/*.md` files.

### Added

- Performance/energy descriptors inside section tags (e.g. `[Whispered Verse]`, `[Explosive Chorus, big guitars]`, `[Double-time Outro]`), documented in `SKILL.md` and expanded in `references/song-structure.md` with intensity / arrangement / delivery descriptor lists and usage rules.
- "No artist names" guidance: do not pass `sounds like <artist>` into `Style:`; translate the reference into era, scene, rhythm section, signature sound, and production character. Added to `SKILL.md` anti-generic rules, `references/suno-v55-controls.md` (new subsection plus a troubleshooting line), and `references/style-selection.md` (new "Translating Reference Artists" subsection).
- Three-anchor quick frame for the Style field (core genre / vibe-texture / lead or signature sound, then tempo, vocal, production) in `references/suno-v55-controls.md`.
- `CLAUDE.md` with repo overview, progressive-disclosure architecture notes, validation/sync commands, and content conventions.
- `references/suno-meta-tags.md`: inline lyric cues beyond section headers: instrumental moments (`[Guitar Solo]`, `[Beat Drop]`), vocal delivery (`[Spoken]`, `[Whispered]`, `[Harmonies]`), multiple vocalists (`[Male Voice]`, `[Female Voice]`, `[Duet]`), ad-libs, sound effects, `[End]`/`[Fade Out]` length control, and failure modes.
- `references/genre-palettes.md`: per-lane menu of BPM bands, signature instruments, production textures, vocal identities, and typical structures across pop, rock, hip hop, electronic, folk/country, soul/gospel, world/regional, score, and niche lanes; framed as a picker, not a set of defaults.
- `references/studio-and-iteration.md`: two-clips-per-run, Extend, Cover/Remix, Replace Section / Edit / inpainting, Crop, stems, remaster, and an edit-vs-re-roll decision table.
- `references/screen-music.md`: anime openings (TV-size form) and endings, TV theme songs / main titles / idents / stings / bumpers, end-credit / needle-drop songs, trailer cuts (three-beat structure), video-game themes, edit-length guidance (full / TV-size / sting / ident), and which formats are vocal songs vs instrumental cues.
- `references/remix-and-style-match.md`: the style-yes/expression-no copyright rule; lyric remix/flip mode; style-match ("in the style of X") mode with style-fingerprint extraction, safe use of web/search, and original-work generation; lyric-style analysis output; `Style Reference:` / `Remix Notes:` output additions and extra checks.
- `references/personas.md`: reusable artist personas: custom vs style-reference (no real names in prompts), the `personas/<slug>.md` spec-file schema (identity, vocals, cadence, lyrical fingerprint, sonic palette / Style kernel, excluded styles, Suno defaults, basis, song log), creating a persona, using one to write a song, output-contract additions, and the no-overwrite rule.
- `references/albums.md`: cohesive albums/EPs: the `albums/<slug>.md` spec-file schema (concept, shared sonic palette / Style kernel, cohesion rules, recurring elements, sequenced tracklist with roles, sequencing notes, excluded styles, Suno defaults, changelog), optional persona link, creating an album, writing a track for one, output-contract additions, and the no-overwrite rule.
- `references/suno-sounds.md`. Suno Sounds (custom audio samples): One Shot vs Loop, BPM, Key; sound categories (SFX & transitions, ambient/background, foley & action, animal, musical samples / drum kits) with example prompts; prompt-writing guidance (recognizable vocabulary, duration, material/space/motion/size); the `Sound:` / `Type:` / `BPM` / `Key` / `Variations` output shape; and the sample-vs-short-piece-of-music routing rule. Based on Suno help article 10625537.

### Changed

- `references/suno-v55-controls.md`: added a Title-field note, a Content-Filters section (real names, brands, profanity, graphic content can block or flatten a generation), an Iteration pointer, and new troubleshooting entries (blank/generic generation, mumbled vocals, model-invented verses, chorus-vs-verse contrast, pronunciation/accent drift).
- `references/songwriting-craft.md`: added "Point Of View And Tense" guidance, a note that the chorus must be mechanically (not just emotionally) plainer than the verses, and matching revision-checklist items.
- `references/instrumental.md`: added "Vocal Chops And Non-Lexical Vocals" (don't blanket-exclude vocals when wordless vocals are wanted), a "Stems And Handoff" note, an "Idents / Stings / Bumpers" micro-cue section, and cross-links to `references/screen-music.md`.
- `references/multilingual.md`: expanded Pronunciation (AI mispronunciation reality, in-line phonetic respelling, `Pronunciation Notes:` usage); broadened the Korean entry to cover ballad, K-hip hop / K-R&B, Korean indie/folk, OST, and trot beyond K-pop; cross-links to studio workflow and screen music.
- `references/genre-palettes.md`: added Korean ballad, K-hip hop / K-R&B, Korean indie/folk, trot, city pop, anime OP (J-rock/J-pop), anime ED, and TV theme / sitcom theme rows; added reminders that "Korean music" is broader than K-pop and that screen formats need `references/screen-music.md`.
- `references/style-selection.md`: added a "screen-tied song" row to the style-selection matrix and broadened the multilingual row (city pop, Korean ballad, K-hip hop, Korean indie, trot) with cross-links.
- `references/song-structure.md`: added a "Screen-Tied Forms" section (anime OP TV-size, anime ED / needle-drop, TV theme / sting, trailer cut).
- `SKILL.md`: expanded the frontmatter `description` (remix, Korean lanes beyond K-pop, anime OP/ED, TV themes, trailers, idents, game themes, lyric remix/flip, style-match, lyric-style analysis, reusable personas, cohesive albums/EPs, Suno Sounds samples; clarified that writing in an artist's style is in scope but reproducing their lyrics is not); added "Remix And Style-Match Mode", "Screen-Tied Songs And Cues", "Personas And Albums", and "Sound Samples (Suno Sounds)" sections; added a Core-Workflow note to load a named persona/album spec first; added routing entries for the new reference files.
- `references/evals.md`: new smoke-test rows (meta-tags, artist-reference rewrite, section descriptors, iteration/Replace-Section, genre-palette, anime OP, TV theme, Korean ballad, lyric remix, style-match, lyric-style analysis, persona custom/style-reference/use, album plan/track, Suno Sounds), new should-trigger queries, and new regression checks.
- `references/templates.md`, `README.md`, `CLAUDE.md`: routing/index entries for all eight new reference files; `SKILL.md` also gained an inline-meta-tags pointer, a content-filter caution, and a version/date anchor.

## Pre-1.0

- Renamed skill to `suno-songwriter`.
- Added skill smoke-test reference (`references/evals.md`).
- Added song structure reference.
- Added 80/20 songwriting reference.
- Initial Suno lyrics agent skill.
