# Reference Index

Use this file as the routing map. Load only the reference file needed for the current request.

## Output Templates

Read `references/output-templates.md` when the task needs a complete output contract, reusable skeleton, or copy-paste-ready prompt pattern.

Covers:
- vocal song output
- instrumental output
- multilingual output
- quick invocation patterns

## Suno v5.5 Controls

Read `references/suno-v55-controls.md` when the task needs Suno-specific settings or troubleshooting.

Covers:
- `Style`
- `Excluded Styles`
- Weirdness
- Style Influence
- Voices
- Custom Models
- My Taste
- prompt troubleshooting

## Suno Meta-Tags

Read `references/suno-meta-tags.md` when the lyrics need cues beyond plain section headers: instrumental moments, vocal delivery, multiple vocalists, ad-libs, sound effects, or ending control.

Covers:
- section headers vs inline cues
- `[Guitar Solo]`, `[Instrumental Break]`, `[Beat Drop]`
- `[Spoken]`, `[Whispered]`, `[Harmonies]`
- `[Male Voice]` / `[Female Voice]` / `[Duet]`
- ad-libs and backing phrases
- sound-effect tags
- `[End]` / `[Fade Out]` length control
- failure modes (tags sung aloud, too many tags ignored)

## Studio And Iteration

Read `references/studio-and-iteration.md` when the user is iterating on a generation or preparing a production: choosing between takes, Extend, Cover/Remix, Replace Section, Crop, stems, remaster, and the edit-vs-re-roll decision.

Covers:
- two clips per run
- Extend
- Cover / Remix / restyle
- Replace Section / Edit / inpainting
- Crop / trim
- stems and DAW handoff
- remaster
- edit-vs-re-roll decision table

## Songwriting Craft

Read `references/songwriting-craft.md` when writing or revising lyrics, hooks, verses, choruses, bridges, or rhyme/meter.

Covers:
- hook strength
- section jobs
- lyric transformation
- anti-generic edits
- meter and rhyme
- vivid detail
- genre-specific lyric handling

## Song Structure

Read `references/song-structure.md` when choosing or fixing verse/chorus order, pre-chorus use, bridge placement, AABA/AAA forms, 12-bar blues, EDM/drop forms, rap forms, or instrumental cue forms.

Covers:
- section jobs
- ABAB and ABABCB
- AABA and AAA
- pre-chorus and bridge decisions
- instrumental and game loop forms
- structure troubleshooting

## Rule Of 3

Read `references/rule-of-3.md` when the song needs a stronger hook, more memorable phrasing, better chorus payoff, cleaner arrangement focus, or a more satisfying repeated motif.

Covers:
- statement, repetition, variation/twist
- lyrical Rule of 3
- melodic and rhythmic Rule of 3
- arrangement focus
- when to break the rule

## 80/20 Songwriting

Read `references/eighty-twenty.md` when the song needs stronger impact, clearer hook priority, faster revision decisions, or better balance between familiar genre signals and fresh ideas.

Covers:
- hook-first revision
- high-impact song elements
- 80% familiar / 20% fresh
- fast finish rule
- instrumental and multilingual 80/20 use

## Instrumental And Score

Read `references/instrumental.md` when the task is non-lyric or mostly non-lyric.

Covers:
- lofi beats
- study/focus music
- OST/soundtrack cues
- game loops
- ambient and trailer cues
- loop points and cue arcs

## Screen Music

Read `references/screen-music.md` when the music is tied to picture and an edit length: anime openings/endings, TV theme songs, end-credit songs, trailer cuts, idents, and game themes.

Covers:
- anime OP (TV-size form, fast anthemic J-rock/J-pop)
- anime ED (mellow, reflective)
- TV theme songs, main titles, idents, stings, bumpers
- end-credit / needle-drop songs
- trailer cuts (three-beat structure, teaser vs full)
- video-game themes
- edit-length guidance (full / TV-size / sting / ident) and `[End]` vs `[Loop Point]`
- which formats are vocal songs vs instrumental cues

## Multilingual Songs

Read `references/multilingual.md` when the user asks for non-English lyrics, translation, bilingual writing, dialect, script, romanization, or pronunciation notes.

Covers:
- translation vs singable adaptation
- dialect/region handling
- script and romanization
- language-specific phrasing (including Korean lanes beyond K-pop)
- AI mispronunciation and phonetic respelling
- native-speaker review caveats

## Style Selection

Read `references/style-selection.md` when genre, vocalist, instrumentation, or production palette is missing, too generic, or at risk of repeating a previous sound.

Covers:
- style selection matrix
- anti-lock-in rule
- genre examples
- style prompt examples

## Genre Palettes

Read `references/genre-palettes.md` when you need a concrete BPM band, signature instruments, production textures, vocal identities, or typical structure for a lane — used as a picker to fill gaps and avoid lock-in, not as a set of defaults.

Covers:
- palette table across pop, rock, hip hop, electronic, folk/country, soul/gospel, world/regional (incl. Korean ballad, K-hip hop, Korean indie, trot, city pop), screen (anime OP/ED, TV theme), score, and niche lanes
- how to pick from the table without locking in
- BPM bands, instrument menus, production vocabulary, vocal identities, default structures

## Remix And Style Match

Read `references/remix-and-style-match.md` when the user wants a remix/flip of an existing lyric, a song written in the style/cadence of a named artist or song, or an analysis of supplied lyrics' style.

Covers:
- the style-yes / expression-no copyright rule
- lyric remix / flip mode (Revision Mode turned up)
- style-match mode: building a style fingerprint, using search safely, generating original work
- lyric-style analysis output
- `Style Reference:` and `Remix Notes:` output additions, plus extra checks

## Evals And Smoke Tests

Read `references/evals.md` when testing whether the skill triggers correctly or produces the expected output shape across vocal, instrumental, multilingual, Suno controls, reference-lyrics transformation, structure, and style-selection tasks.

Covers:
- smoke test matrix
- should-trigger queries
- should-not-trigger queries
- regression checks
- output quality rubric
