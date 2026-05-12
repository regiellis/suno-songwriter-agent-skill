# Changelog

## 2026-05-12

### Added

- Performance/energy descriptors inside section tags (e.g. `[Whispered Verse]`, `[Explosive Chorus, big guitars]`, `[Double-time Outro]`), documented in `SKILL.md` and expanded in `references/song-structure.md` with intensity / arrangement / delivery descriptor lists and usage rules.
- "No artist names" guidance: do not pass `sounds like <artist>` into `Style:`; translate the reference into era, scene, rhythm section, signature sound, and production character. Added to `SKILL.md` anti-generic rules, `references/suno-v55-controls.md` (new subsection plus a troubleshooting line), and `references/style-selection.md` (new "Translating Reference Artists" subsection).
- Three-anchor quick frame for the Style field (core genre / vibe-texture / lead or signature sound, then tempo, vocal, production) in `references/suno-v55-controls.md`.
- `CLAUDE.md` with repo overview, progressive-disclosure architecture notes, validation/sync commands, and content conventions.
- `references/suno-meta-tags.md` — inline lyric cues beyond section headers: instrumental moments (`[Guitar Solo]`, `[Beat Drop]`), vocal delivery (`[Spoken]`, `[Whispered]`, `[Harmonies]`), multiple vocalists (`[Male Voice]`, `[Female Voice]`, `[Duet]`), ad-libs, sound effects, `[End]`/`[Fade Out]` length control, and failure modes.
- `references/genre-palettes.md` — per-lane menu of BPM bands, signature instruments, production textures, vocal identities, and typical structures across pop, rock, hip hop, electronic, folk/country, soul/gospel, world/regional, score, and niche lanes; framed as a picker, not a set of defaults.
- `references/studio-and-iteration.md` — two-clips-per-run, Extend, Cover/Remix, Replace Section / Edit / inpainting, Crop, stems, remaster, and an edit-vs-re-roll decision table.

### Changed

- `references/suno-v55-controls.md` — added a Title-field note, a Content-Filters section (real names, brands, profanity, graphic content can block or flatten a generation), an Iteration pointer, and new troubleshooting entries (blank/generic generation, mumbled vocals, model-invented verses, chorus-vs-verse contrast, pronunciation/accent drift).
- `references/songwriting-craft.md` — added "Point Of View And Tense" guidance, a note that the chorus must be mechanically (not just emotionally) plainer than the verses, and matching revision-checklist items.
- `references/instrumental.md` — added "Vocal Chops And Non-Lexical Vocals" (don't blanket-exclude vocals when wordless vocals are wanted) and a "Stems And Handoff" note.
- `references/multilingual.md` — expanded Pronunciation: AI mispronunciation reality, in-line phonetic respelling, and `Pronunciation Notes:` usage; cross-link to the studio workflow.
- `references/evals.md` — new smoke-test rows (meta-tags, artist-reference rewrite, section descriptors, iteration/Replace-Section, genre-palette), new should-trigger queries, and new regression checks.
- `references/templates.md`, `README.md`, `CLAUDE.md`, `SKILL.md` — routing/index entries for the three new reference files; `SKILL.md` also gained an inline-meta-tags pointer, a content-filter caution, and a version/date anchor.

## Earlier

- Renamed skill to `suno-songwriter`.
- Added skill smoke-test reference (`references/evals.md`).
- Added song structure reference.
- Added 80/20 songwriting reference.
- Initial Suno lyrics agent skill.
