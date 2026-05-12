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
- `references/screen-music.md` — anime openings (TV-size form) and endings, TV theme songs / main titles / idents / stings / bumpers, end-credit / needle-drop songs, trailer cuts (three-beat structure), video-game themes, edit-length guidance (full / TV-size / sting / ident), and which formats are vocal songs vs instrumental cues.
- `references/remix-and-style-match.md` — the style-yes/expression-no copyright rule; lyric remix/flip mode; style-match ("in the style of X") mode with style-fingerprint extraction, safe use of web/search, and original-work generation; lyric-style analysis output; `Style Reference:` / `Remix Notes:` output additions and extra checks.

### Changed

- `references/suno-v55-controls.md` — added a Title-field note, a Content-Filters section (real names, brands, profanity, graphic content can block or flatten a generation), an Iteration pointer, and new troubleshooting entries (blank/generic generation, mumbled vocals, model-invented verses, chorus-vs-verse contrast, pronunciation/accent drift).
- `references/songwriting-craft.md` — added "Point Of View And Tense" guidance, a note that the chorus must be mechanically (not just emotionally) plainer than the verses, and matching revision-checklist items.
- `references/instrumental.md` — added "Vocal Chops And Non-Lexical Vocals" (don't blanket-exclude vocals when wordless vocals are wanted), a "Stems And Handoff" note, an "Idents / Stings / Bumpers" micro-cue section, and cross-links to `references/screen-music.md`.
- `references/multilingual.md` — expanded Pronunciation (AI mispronunciation reality, in-line phonetic respelling, `Pronunciation Notes:` usage); broadened the Korean entry to cover ballad, K-hip hop / K-R&B, Korean indie/folk, OST, and trot beyond K-pop; cross-links to studio workflow and screen music.
- `references/genre-palettes.md` — added Korean ballad, K-hip hop / K-R&B, Korean indie/folk, trot, city pop, anime OP (J-rock/J-pop), anime ED, and TV theme / sitcom theme rows; added reminders that "Korean music" is broader than K-pop and that screen formats need `references/screen-music.md`.
- `references/style-selection.md` — added a "screen-tied song" row to the style-selection matrix and broadened the multilingual row (city pop, Korean ballad, K-hip hop, Korean indie, trot) with cross-links.
- `references/song-structure.md` — added a "Screen-Tied Forms" section (anime OP TV-size, anime ED / needle-drop, TV theme / sting, trailer cut).
- `SKILL.md` — expanded the frontmatter `description` (remix, Korean lanes beyond K-pop, anime OP/ED, TV themes, trailers, idents, game themes, lyric remix/flip, style-match, lyric-style analysis; clarified that writing in an artist's style is in scope but reproducing their lyrics is not); added "Remix And Style-Match Mode" and "Screen-Tied Songs And Cues" sections; added routing entries for the two new reference files.
- `references/evals.md` — new smoke-test rows (meta-tags, artist-reference rewrite, section descriptors, iteration/Replace-Section, genre-palette, anime OP, TV theme, Korean ballad, lyric remix, style-match, lyric-style analysis), new should-trigger queries, and new regression checks.
- `references/templates.md`, `README.md`, `CLAUDE.md` — routing/index entries for all five new reference files; `SKILL.md` also gained an inline-meta-tags pointer, a content-filter caution, and a version/date anchor.

## Earlier

- Renamed skill to `suno-songwriter`.
- Added skill smoke-test reference (`references/evals.md`).
- Added song structure reference.
- Added 80/20 songwriting reference.
- Initial Suno lyrics agent skill.
