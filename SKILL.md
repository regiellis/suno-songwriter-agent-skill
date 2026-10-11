---
name: suno-songwriter
license: MIT
description: "Write, revise, plan, or adapt songs, lyrics, hooks, and AI music prompts. Use for Suno vocal or instrumental packages, song matrices, multilingual adaptation, genre treatments, reusable artist personas, album plans, Suno settings and iteration, sound samples, and cover-art prompts. Supports original style-inspired writing without copying lyrics. Not for standalone music theory, general DAW mixing, or licensing advice."
---

# Suno Songwriter

Create songs and prompts around a clear hook, musical identity, and playable structure. Target Suno v6; v6 model and FAQ guidance rechecked 2026-09-24 against the official sources in `references/suno-v6-controls.md`. Suno retired every pre-v6 model on 2026-09-09, so `v6`, `v6-wild`, and `v6-mini` are the only models that generate new material. This is a target version, not a promise that every account exposes the same UI. Re-check controls when the user's model or interface differs.

## Workflow

1. Identify the requested deliverable: full vocal song, focused lyric edit, instrumental cue, settings, sample, artwork, persona, or album. Return only what the user needs. A chorus rewrite does not need a full song package.
2. Preserve the user's theme, language, supplied wording they want kept, and musical constraints. Infer minor gaps and label material assumptions; ask only when a missing choice changes the work substantially.
3. Choose a song promise and hook or motif. For a full song, map section jobs and contrast before drafting. Use `references/song-matrix.md` when the brief needs a plan, alternatives, a duration budget, or stronger section movement. Keep the matrix internal unless requested or useful to review.
4. Draft for the chosen genre and delivery. Use `references/genre-songwriting.md` to select relevant family guidance; for mixed styles, use `references/genre-fusion.md` to allocate groove, phrasing, harmony, form, and timbre across influences. When the brief needs musical detail, choose harmonic motion, melodic contour, groove, and instrumental roles using the relevant references; translate them into a few audible directions rather than adding theory to every output. Revise the hook, natural stress, breath space, and section movement before formatting. A shorter chorus can lift through space, register, rhythm, or harmony; it need not always get louder.
5. Separate sung words, production direction, and operational notes. Match settings to the user's actual Suno surface. Treat tags, BPM, key, duration, and slider recipes as guidance, not guarantees of rendered audio.
6. Return the requested artifact. Explain important assumptions or edits briefly. Do not claim to have generated, heard, tested, uploaded, or saved anything unless that action occurred.

## Output Contract

Do not output em dashes (U+2014) or en dashes (U+2013) anywhere in the response, including lyrics, prompts, titles, notes, explanations, and code blocks. Use commas, periods, colons, or parentheses as the sentence requires. Use the ASCII hyphen (`-`) for section descriptors and numeric ranges. Normalize these dashes in supplied text when returning it.

| Request | Return |
| --- | --- |
| Full vocal song | `Title`, `Style`, `Excluded Styles` (use `None` if unnecessary), `Lyrics` |
| Instrumental cue | `Title`, `Instrumental Prompt`, `Arrangement` |
| Focused edit or analysis | The requested passage, revision, or analysis; preserve unrelated material |
| Settings only | Relevant prompt fields and available controls; no invented lyrics |
| Song plan or matrix | A compact section/decision table; lyrics only if requested |
| Individual sample | `Sound`, `Type`; `BPM` and `Key` for musical material; variations when useful |
| Artwork | `Cover Concept`, `Image Prompt`, optional `Motion Prompt`, `Settings`; append to a song if both were requested |
| Persona or album | The spec and path described in the relevant reference |

Add `Language Notes` for language, adaptation, dialect, script, or pronunciation decisions. Add `Suno v6 Notes`, `Slider Suggestions`, and `Checks` only when useful or requested. Settings are starting points; checks distinguish text review from listening tests.

`Instrumental Prompt` and `Arrangement` are this skill's portable labels, not literal Suno field names. For Advanced with Instrumental enabled, map the sound brief to Styles and use Exclude or sliders when exposed and relevant. The arrangement is a planning map; summarize essential changes in an available prompt field rather than pasting prose into a hidden or absent Lyrics field. For a simple description-only surface, keep the portable package and omit unavailable controls.

Default to a compact Style line, roughly 200 characters when sufficient. Expand when a meaningful arrangement or genre transition needs it; obey the user's visible field counter. The compact target is not a platform limit. Keep positive sound direction in Style and negative sound direction in Excluded Styles when available.

See `references/output-templates.md` for skeletons. Optional sections and example forms are not mandatory output.

## Pre-Output Check

Read the finished fields against each other before returning them. The drafting rules above do not enforce themselves, and these faults are invisible while writing because each field looks correct alone.

- Scan the complete response for U+2014 and U+2013 before sending; replace either character with suitable punctuation. This check covers every field and surrounding prose.
- Style carries positive direction only: no `exclude:` list, no `no ...` phrase, no slider value, no square brackets.
- Every token in Style is deliberate. Delete a stray or leftover word; Suno reads it as a genre request, not a typo.
- Check section and language promises against Lyrics; place instrumental, harmony, and vocal-layer changes in the intended sections. Conflicting fields can produce unwanted results, but no instruction guarantees rendering.
- Style does not contradict itself. Reconcile a hushed intimate mix against massed layers by placing the change, not by listing both.
- Parentheses hold sung words only. Production direction belongs in the section tag.
- Section tags use a plain hyphen before a descriptor: `[Verse 2 - layered vocals]`.
- The last sung line has a section after it whenever the cut must not clip it.
- `Language Notes` appear whenever the lyric changes language.

## Song Quality

- Give vocal songs an intentional center: a claim, story, groove, character, or image pattern, with a recognizable hook or organizing idea. In chorus forms, place the title or hook in or near the chorus and make its phrasing easier to remember than the verses. Refrain, strophic, rap, and through-composed forms can work differently.
- Let sections develop the situation: new evidence, consequence, perspective, or emotional turn. Repetition can establish identity, participation, hypnosis, or changed meaning; gradual and texture-led forms need not advance a plot.
- Use concrete human detail where it carries emotion. Stock words are a revision signal, not a blacklist; keep an archetypal word that earns its place.
- Keep POV, tense, dialect, and vocal identity intentional. Preserve conversational grammar when it serves the character and rhythm.
- Check stressed syllables, phrase lengths, breath points, and hook vowels. Four-line verses and short choruses are useful starting shapes, not required counts; lines are not bars. Denser rap or spoken-sung verses need rhythmic space, not a pop word-count cap.
- Choose genre, groove, voice, instruments, and production from the brief. Let the genre affect cadence, hook mechanism, and form as well as timbre; for hybrids resolve pulse and foreground conflicts before adding genre labels. Do not inherit the previous song's palette. Genre menus and BPM bands suggest options; the user's deliberate choices win.
- Use short bracketed section cues where helpful. Put only words intended to be sung in parentheses. Tags may be ignored or sung; `[End]` requests closure but cannot enforce an exact ending. Give the last lyric a section to land after it when the cut must not clip a sung line.
- Match the deliverable to the user's model and plan. Suggest `v6` for a defined brief, `v6-wild` only for deliberate exploration, and paid-only controls only when the user has them. Hold Variety at 0 whenever the exact Style text must survive between takes.
- Adapt supplied original lyrics at the requested level of change. For third-party song references, extract broad traits and write fresh expression rather than copying distinctive lines or hooks. Translate artist references into musical traits for Suno prompt fields.
- For multilingual songs, preserve meaning and hook function with natural target-language stress. Follow a request for literal translation when given; do not silently substitute adaptation.
- For instrumentals, review motif, cue arc, instrumentation, and vocal-texture constraints. A no-voice brief excludes choir and chops too; requested wordless vocals need a compatible vocal-enabled workflow.

## Reference Routing

Load only files that change a decision for this request. `references/templates.md` is the complete routing index.

| Need | Reference |
| --- | --- |
| Output skeletons | `references/output-templates.md` |
| Section matrix, hook options, energy, bar/time budgets | `references/song-matrix.md` |
| Lyric angles, section development, hooks, prosody, rhyme, revision | `references/songwriting-craft.md` |
| Chords, modes, harmonic motion, melodic contour, vocal range | `references/harmony-and-melody.md` |
| Meter, subdivision, pocket, instrumental roles, section contrast | `references/rhythm-and-arrangement.md` |
| Forms and section jobs | `references/song-structure.md` |
| Repetition and payoff | `references/rule-of-3.md` |
| Hook priorities and economical revision | `references/eighty-twenty.md` |
| Model choice, Styles, Exclude, sliders, Max Mode, personalization, platform sources | `references/suno-v6-controls.md` |
| Production direction, instrument activity, verse energy, ending buffers | `references/v6-production-direction.md` |
| Section cues, delivery, duets, ad-libs, endings | `references/suno-meta-tags.md` |
| Take comparison, editing, Studio, stems, remaster | `references/studio-and-iteration.md` |
| Non-lyric tracks, game loops, score | `references/instrumental.md` |
| Anime OP/ED, TV themes, trailers, edit lengths | `references/screen-music.md` |
| Sound effects and individual samples | `references/suno-sounds.md` |
| Cover images and animated covers | `references/cover-art.md` |
| Translation, adaptation, dialect, script | `references/multilingual.md` |
| Choosing a palette without repeating defaults | `references/style-selection.md` |
| Genre writing decisions, coverage, and research boundaries | `references/genre-songwriting.md` |
| Pop, roots, country, folk, blues, soul, gospel, funk, disco writing | `references/genre-pop-and-roots.md` |
| Rap cadence, rock riffs, punk, metal, progressive forms | `references/genre-rap-rock-and-heavy.md` |
| Dance hooks, electronic forms, ambient and experimental development | `references/genre-electronic-and-experimental.md` |
| Caribbean, Latin American, Brazilian, African, and regional writing | `references/genre-regional-and-diasporic.md` |
| Jazz forms, theater, chanson, Asian screen/pop, modal-system boundaries | `references/genre-jazz-stage-and-screen.md` |
| Genre-specific instrument, tempo, and production menus | `references/genre-palettes.md` |
| Fusion, genre switches, multiple treatments | `references/genre-fusion.md` |
| Lyric remix and reference-style analysis | `references/remix-and-style-match.md` |
| Reusable artist identity | `references/personas.md` |
| Cohesive album or EP | `references/albums.md` |
| Smoke tests and output rubric | `references/evals.md` |

## Saved Projects And Portability

Persona specs live in the user's `personas/<slug>.md`; album specs in `albums/<slug>.md`. Read an existing spec before writing its songs, then update its song log or tracklist as part of the requested work. Preserve existing content; confirm replacement before overwriting a spec. A Markdown persona is a creative brief, not a trained Suno Voice or a guarantee of the same rendered singer.

For other music tools, retain the song plan and musical direction but map fields to that tool. Omit Suno-only controls. This skill prepares text and project specs; audio generation, image generation, uploads, and paid operations require an available tool and authorization for that action.
