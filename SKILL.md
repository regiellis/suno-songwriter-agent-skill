---
name: suno-songwriter
license: MIT
description: "Use this skill when the user wants to write, revise, remix, translate, adapt, or prompt a song, lyric, hook, chorus, verse, rap, ballad, instrumental, Suno track, or AI-music prompt. Prioritize strong original lyrics: hook-first, singable, concrete, structured, and ready for Suno v5.5 Custom Mode. Also covers vocal Style and Excluded Styles, vocal/custom sliders, multilingual lyrics, lofi and OST cues, anime or TV themes, lyric remixes, artist-style/cadence fingerprints without copying lyrics, reusable personas, albums, Suno Sounds samples, cover art, and animated covers. Not for music theory, DAW mixing, or licensing."
---

# Suno Songs, Lyrics, And Instrumental Prompts

Use this skill to create release-quality AI song inputs. Target Suno v5.5 first (current as of 2026-07; if the platform's model has moved on, the field names and craft still apply: re-check version-specific limits), then keep the result portable enough for other AI music systems by separating style, lyrics, structure, and performance notes.

Highest priority for vocal requests: write a good song, not a feature-complete form. A useful Suno package with weak lyrics is a failed output. Default to Suno-native lyric phrasing: short, direct, emotional lines that sing easily.

Use references selectively:
- Read `references/templates.md` first only when you need the reference index.
- Read `references/output-templates.md` for complete output skeletons and quick invocation patterns.
- Read `references/suno-v55-controls.md` for vocal/custom Style, Excluded Styles, Weirdness, Style Influence, the Title field, Voices, Custom Models, My Taste, content filters, or Suno troubleshooting.
- Read `references/suno-meta-tags.md` for cues inside the lyrics body: instrumental moments, vocal delivery, multiple vocalists, ad-libs, sound effects, and `[End]` length control.
- Read `references/studio-and-iteration.md` for choosing between takes, Extend, Cover/Remix, Replace Section, Crop, stems, remaster, and the edit-vs-re-roll decision.
- Read `references/songwriting-craft.md` for lyric writing, revision, hooks, rhyme, meter, point of view, vivid detail, and reference-lyric transformation.
- Read `references/song-structure.md` when choosing or fixing verse/chorus order, pre-chorus use, bridge placement, section-tag descriptors, AABA/AAA forms, 12-bar blues, EDM/drop forms, rap forms, or instrumental cue forms.
- Read `references/rule-of-3.md` when improving memorability, repeated phrases, melodic/rhythmic motifs, chorus payoff, or arrangement focus.
- Read `references/eighty-twenty.md` when prioritizing the hook, identifying the highest-impact 20%, reducing over-polish, or balancing familiar genre signals with fresh ideas.
- Read `references/instrumental.md` for lofi, OST, game loops, ambient, trailer cues, idents, vocal chops, or other non-lyric tracks.
- Read `references/suno-sounds.md` when the user wants an individual audio sample rather than a song or track: a sound effect, foley hit, ambience bed, transition/whoosh, animal sound, or a musical one-shot / drum loop (Suno Sounds).
- Read `references/cover-art.md` when the user wants a cover image or an animated (looping video) cover for a track. Suno's Generate Cover Art / Animate tools: text-to-image, text-to-video, image-to-video.
- Read `references/screen-music.md` for anime openings/endings, TV theme songs, end-credit songs, trailer cuts, idents, game themes, and edit-length (TV-size/sting) guidance.
- Read `references/multilingual.md` for non-English lyrics, translation, bilingual writing, dialect, script, romanization, or pronunciation: including Korean lanes beyond K-pop.
- Read `references/style-selection.md` when genre, vocalist, instrumentation, or production palette is missing, generic, or over-reused.
- Read `references/genre-palettes.md` for a concrete BPM/instrument/production/vocal/structure menu per lane, used as a picker, not as defaults.
- Read `references/genre-fusion.md` when a request involves more than one genre: a fusion blend in one Style line, a mid-song genre switch, or the same song in several genre versions.
- Read `references/remix-and-style-match.md` when remixing or flipping an existing lyric, writing in the style/cadence of a named artist or song, or analyzing supplied lyrics for their style.
- Read `references/personas.md` when creating, updating, or using a reusable artist persona (a consistent singer, rapper, or band saved as a spec file).
- Read `references/albums.md` when planning, updating, or writing tracks for a cohesive album or EP saved as a spec file.
- Read `references/evals.md` when testing skill triggering, smoke-test coverage, regression behavior, or output quality.

## Core Workflow

1. Clarify the song goal from the user request: theme, genre, language/dialect, vocalist or instrumental mode, audience, emotional arc, and whether they need lyrics, arrangement notes, a style prompt, or all of them. If the user names a saved persona or album, read its spec file (`personas/<slug>.md` / `albums/<slug>.md`) first and treat it as a constraint (see `references/personas.md`, `references/albums.md`).
2. Build the song as a song, not just a prompt: title, central promise, hook phrase, section map, melodic phrasing assumptions, then final lyrics.
3. If the user provides existing lyrics, treat them as reference material for theme and direction unless they explicitly ask for a close edit, preservation, or line-by-line rewrite.
4. Choose the sound from the user's request. If genre, vocalist, or production style is missing, either ask a concise follow-up or infer a fitting direction from the theme and label it as an assumption. Do not default to one recurring palette.
5. Keep Suno fields clean:
   - Vocal Custom Mode: use `Style:` for concise positive direction; `Excluded Styles:` for negative sound direction; `Lyrics:` for section-tagged singable words.
   - Instrumental Mode: do not return `Style:`, `Excluded Styles:`, or slider suggestions because Suno's instrumental flow does not expose those inputs. Return `Instrumental Prompt:` plus `Arrangement:`.
   - `Arrangement:` is a section-tagged cue map when the track is instrumental or non-lyric.
6. Before output, do one silent lyric revision pass: strengthen the title/hook, simplify the line language, shorten any overlong line, verify point of view and tense, and make the chorus mechanically simpler than the verses.
7. When relevant, include short `Suno v5.5 Notes:` for Voices, Custom Models, My Taste, Studio, stems, remaster, or iteration strategy.
8. For vocal/custom Suno modes, include `Slider Suggestions:` when the user asks for prompt settings, troubleshooting, or a complete Suno-ready package. Do not include sliders for Instrumental Mode.
9. Add `Checks:` only when useful or requested. Keep checks compact and focused on structure, meter, hook clarity, cliche risk, and prompt-field separation.

## Lyric Quality Gate

For every vocal lyric, enforce these before returning the final text:

- The title or hook phrase appears in or near the chorus.
- The chorus is shorter, plainer, and more repeatable than the verses.
- Lines are compact and singable by default: usually 5-9 words, one clear image or claim per line.
- Verse and pre-chorus lines use natural end rhyme or vowel rhyme unless the genre calls for loose prose.
- Favor clean, memorable phrasing over clever metaphor or narrative explanation.
- Each section has a distinct job: setup, pressure, payoff, contrast, or resolution.
- Point of view and tense stay consistent unless the shift is deliberate and section-boundary clear.
- At least one concrete human detail anchors the song, but the chorus is not overloaded with detail.
- Stock abstractions are rewritten unless they are the user's deliberate aesthetic.
- Section lines are close enough in length to sing; rewrite obvious mouthfuls.
- The final chorus, bridge, or outro changes the meaning slightly rather than only repeating the same emotion.

## Suno-Native Lyric Shape

Unless the user asks for dense poetry, rap complexity, a literary style, or a groove-narrative form, write vocal lyrics in this shape:

- Use 4-line verses and 2-line pre-choruses by default.
- Use a 4-6 line chorus with one unmistakable hook phrase.
- Keep syntax plain: subject, verb, image. Avoid clauses stacked with `and`, `but`, or explanatory phrases.
- Let one strong image carry a section (`cherry blossoms`, `storm`, `train lights`, `packed bags`) instead of adding many small details.
- Use familiar, singable rhyme families: mind/behind, rain/pain/name, spring/everything, glow/know.
- Put performance descriptors in section tags when they help Suno deliver the song: `[Intimate female vocals]`, `[Layered harmonies, momentum building]`, `[Anthemic, soaring]`, `[Stripped back, vulnerable]`.
- Do not overcorrect every archetypal word. Words like `fire`, `storm`, `light`, `rise`, `shine`, and `heart` are acceptable when they serve a clear hook and genre.

## Groove-Narrative Vocal Mode

Use this mode for neo-soul, R&B storytelling, spoken-sung tracks, conscious rap, jazz-hop, city-life vignettes, bus/train/street songs, or any brief that feels like a groove with scenes passing by.

In this mode:
- Longer verses are allowed: 8, 12, or 16 lines can work when the groove stays steady.
- Keep couplets tight and rhythmic; each pair should feel like one bar-to-bar thought.
- Use internal rhythm, slant rhyme, and repeated phrase shapes more than simple pop brevity.
- Add arrangement and environment cues in brackets when they define the record: `[Intro - 8 bars, bus doors hiss, street ambience, Rhodes and bass groove]`, `[drums enter bar 7]`, `[Bridge - drums drop to kick and hi-hat, bass lead]`.
- Use vocalist labels when helpful: `(Male)`, `(Female - wordless hum)`, `(Both)`, `(Female - wordless "oooh" echo underneath)`.
- Spoken lines can sit in a bridge or outro when the track needs intimacy: `(Male - spoken, intimate)`.
- The chorus should still be simpler than the verses: 4 lines, repeatable, rhythmic, and easy to chant.
- Do not sanitize dialect or conversational grammar if it supports the pocket (`done changed`, `playin'`, `movin'`), but keep it intentional and consistent.

## Suno v5.5 Prompting

Use bracketed section tags. For vocal songs:
- `[Intro]` for a short setup
- `[Verse 1]` and later verses for story/detail
- `[Chorus]` for repeated hook lines
- `[Bridge]` for a contrast or twist before the final chorus
- `[Outro]` or `[Coda]` to close

You can add a short performance or energy descriptor inside a section tag to cue a dynamic change, for example `[Whispered Verse]`, `[Half-time Verse 2]`, `[Explosive Chorus, big guitars]`, `[Stripped Bridge, vocal and piano only]`, `[Double-time Outro]`. Keep these to a few words, use them only where the energy actually shifts, and keep persistent instrument/production direction in `Style:` for vocal/custom modes or `Instrumental Prompt:` for Instrumental Mode.

The lyrics body also accepts inline cues on their own line: instrumental moments (`[Guitar Solo]`, `[Instrumental Break]`, `[Beat Drop]`), vocal delivery (`[Spoken]`, `[Whispered]`, `[Harmonies]`), vocalist hand-offs (`[Male Voice]`, `[Female Voice]`, `[Duet]`), ad-libs in parens (`(yeah)`), sound effects (`[Applause]`), and ending control (`[End]`, `[Fade Out]`). Use them sparingly: too many get ignored or sung aloud. `[End]` after the final section is the reliable way to stop Suno inventing extra verses. See `references/suno-meta-tags.md`.

Suno can silently reject or blandly average a generation that trips a content/copyright filter: real-person names (in `Style:`, `Instrumental Prompt:`, and lyrics), brand names, heavy profanity, or graphic content. If a result comes back blank or oddly generic, suspect the filter before the sliders; soften or imply the offending material and note the change in `Suno v5.5 Notes:`.

For instrumentals:
- `[Intro]`, `[Theme A]`, `[Theme B]`, `[Breakdown]`, `[Build]`, `[Climax]`, `[Loop Point]`, `[Outro]`
- For lofi/background music, prefer loopable sections and subtle variation.
- For OST cues, describe scene function, motif, dynamics, instrumentation, and emotional turn.

For vocal/custom modes, Suno v5.5 responds well to clear, natural-language style prompts. Include the most important descriptors early:

```text
[Genre/subgenre], [mood], [tempo/BPM], [vocal style], [instruments and production], [theme/story], [optional exclusions]
```

Examples:
- `garage rock, restless and defiant, 132 BPM, raw group vocals, distorted guitars and live drums, punchy basement production`
- `afrobeats pop, joyful and romantic, 105 BPM, smooth lead vocal, syncopated percussion, bright guitars, polished dance mix`

For v5.5 personalization:
- **Voices:** If the user has a trained Voice selected, do not over-describe the voice. Use light phrasing like `in my trained voice` or trust the selected Voice.
- **Custom Models:** If the user has a Custom Model selected, prompt normally around song intent. Avoid fighting the model with too many contradictory genre tags.
- **My Taste:** Suggest using the Magic Wand in the Styles field for personalized ideas, then edit the result for clarity and specificity.
- **Studio/stems/remaster:** Mention only when the user is iterating, fixing mixes, or preparing a production workflow.

## Style Diversity

Do not let examples or previous songs lock the output into one sound. Every new task should choose a fresh sonic palette from the user's prompt, reference material, or explicit assumptions.

When genre is unspecified, pick one fitting lane and state it as an assumption, or offer 2-3 concise options when the choice materially changes the song:
- commercial pop, dance pop, synthpop, indie pop, hyperpop
- acoustic folk, modern country, Americana, singer-songwriter
- trap, drill, boom bap, melodic rap, phonk
- R&B, soul, gospel, funk, disco
- indie rock, punk, metalcore, grunge, shoegaze
- house, techno, UK garage, drum and bass, ambient
- Latin pop, reggaeton, afrobeats, K-pop inspired, jazz fusion
- orchestral, trailer score, musical theater, children's song, novelty

Vary vocal identity, tempo, instrumentation, structure, and production language to match the lane. Do not reuse `cinematic alt-R&B`, `gospel pads`, `warm male vocal`, `piano and strings`, or similar defaults unless requested or clearly justified by the brief.

When the request spans more than one genre (a hybrid blend, a mid-song genre switch, or the same song in several genre treatments) read `references/genre-fusion.md`: build blends as anchor + accent (never 50/50), state a switch in both `Style:` and a section tag, and give each genre version its own Style/Excluded Styles/sliders over the same lyric.

## Instrumental Mode

Use Instrumental Mode when the user asks for no vocals, lofi beats, study music, meditation, game music, film/TV score, trailer music, background music, underscore, ambience, OST, theme music, battle music, menu music, or a soundtrack cue.

In Instrumental Mode:
- Return `Instrumental Prompt:` instead of `Style:` / `Excluded Styles:`.
- Do not include `Slider Suggestions:`.
- Put `instrumental`, `no lead vocals`, or precise vocal texture instructions inside `Instrumental Prompt:` as plain language.
- Return `Arrangement:` instead of `Lyrics:` unless the user asks for vocal chops, chants, or non-lexical syllables.
- Write section tags as musical cue directions, not sung lyrics.
- Describe motif, texture, rhythm, dynamics, transitions, and loopability.
- Avoid lyric checks such as rhyme and chorus wording; check form, cue clarity, loopability, instrumentation, and excluded vocal consistency.

Instrumental prompt examples:
- lofi: `instrumental lofi chillhop study beat, relaxed 78 BPM, dusty drums, mellow Rhodes, soft upright bass, vinyl texture, loopable, no lead vocals`
- OST: `instrumental orchestral fantasy OST cue, 92 BPM, strings, harp, low brass, taiko swells, mysterious village-to-battle arc, cinematic dynamics`
- ambient: `instrumental dark ambient drone, slow 55 BPM pulse, evolving pads, bowed textures, distant bells, slow tension build, no drums, no lead vocals`

## Sound Samples (Suno Sounds)

When the user wants an individual audio *sample* (a sound effect, transition/whoosh, riser, impact, foley hit, ambience bed, animal sound, or a musical one-shot / drum loop), that is Suno's "Sounds" feature, not a song or instrumental track. Read `references/suno-sounds.md`. Return a `Sound:` prompt plus `Type:` (One Shot / Loop), `BPM:`, `Key:`, and `Variations:` instead of the song or instrumental contract; write the prompt with specific, recognizable vocabulary (`whoosh`, `glitch`, `rumble`, `808 kick`, `ambiance`...), state a duration when it matters, and set BPM/Key only for musical material. If the user actually wants a short *piece of music* (a sting, an ident, a melodic loop), treat it as an instrumental track instead (`references/instrumental.md`).

## Cover Art And Animated Covers

When the user wants visuals for a track, a still cover image or an animated looping-video cover via Suno's **Generate Cover Art** / **Animate** tools (text-to-image, text-to-video, image-to-video), read `references/cover-art.md`. This is artwork, not music: keep the song on its normal contract and return a separate `Cover Concept:` / `Image Prompt:` / `Motion Prompt:` / `Settings:` block (or append a `Cover Art:` block after a song package). Match the visual to the song's lane, era, mood, and key image; pick a deliberate medium and palette instead of an AI-art cliché; put no text, logos, or real artist/character names in the image prompt (same filter logic as `Style:`); compose for a 1:1 square crop; and write motion prompts that describe motion only and loop cleanly. A full multi-scene music video is beyond Suno's looping-cover tool: take the finished track into a dedicated video editor for that; **Suno Scenes** (camera → song) is the reverse direction and routes to the normal song contract.

## Multilingual Mode

Use Multilingual Mode when the user asks for non-English lyrics, bilingual lyrics, translation, localization, romanization, language-specific phrasing, or a song in a regional style tied to a spoken language.

First clarify or infer:
- target language and dialect/region, for example `Spanish (Mexico)`, `Portuguese (Brazil)`, `French (France)`, `Arabic (Levantine)`, `Japanese`, `Korean`
- whether the user wants original lyrics, a singable adaptation, a close translation, or bilingual code-switching
- script preference: native script, romanized text, or both
- whether pronunciation help is needed

Do not assume English pop structure, rhyme density, or line length transfers directly. Adapt structure to the language and genre:
- Romance languages often need more syllables for the same idea; simplify the thought rather than cramming long translated lines.
- Japanese and Korean pop often tolerate short repeated English hooks, compact phrases, and section labels like `[Pre-Chorus]` and `[Post-Chorus]`.
- Spanish and Portuguese hooks often benefit from open vowels, direct repetition, and natural stress over exact English rhyme.
- French lyrics often need smoother vowel flow and may use lighter end rhyme than English pop.
- Arabic, Hindi/Urdu, and many regional styles may use refrains, melisma-friendly vowel endings, and call-response differently from English verse/chorus defaults.

For translations, prioritize singability over literalness unless the user explicitly asks for literal translation. Preserve meaning, speaker, emotional arc, and hook function; rewrite syntax and imagery so it sounds native in the target language.

If unsure about grammar, idiom, dialect, or cultural nuance, say so briefly and offer a draft that may need native-speaker review. Avoid fake slang, stereotypes, or mixing dialects unintentionally.

## Creative Sliders

Suno's Custom Mode Creative Sliders shape how much the model explores and how strictly it follows the style input. Use ranges, not false precision. Do not return slider suggestions for Instrumental Mode.

v5.5 also has a **Duration** control: Auto by default, or a Custom slider from 0:10 to 6:00 in 5-second steps. Recommend Custom when the brief has a target length (TV-size cut, sting, loop) and leave Auto otherwise. The slider does not compress the lyric: write the structure to fit the time, set Duration slightly longer than the intended cut so the ending resolves, and Crop to the exact time (see `references/suno-v55-controls.md` § Duration).

- **Weirdness:** Safe to Chaos. Around 50% is Suno's normal expected result. Lower values are more conventional and stable; higher values add surprise, unusual transitions, and more risk.
- **Style Influence:** Loose to Strong. Higher values make Suno follow the Style field more closely; lower values let the model interpret more freely.

Default recommendations:

- Reliable genre song: Weirdness 20-35%, Style Influence 75-90%.
- Creative but listenable: Weirdness 35-50%, Style Influence 60-80%.
- Experimental but guided: Weirdness 50-70%, Style Influence 60-85%.
- Exploratory chaos: Weirdness 70-100%, Style Influence 20-60%.

Use high Style Influence when the Style line is carefully written or the user needs a specific genre, vocal, or production palette. Lower Style Influence when the lyrics and broad vibe matter more than exact instrumentation. Raise Weirdness for glitch, art pop, hyperpop, psychedelic, avant-garde, unusual fusions, and surprising arrangements. Lower Weirdness for ballads, country, worship, children's music, commercial pop, brand-safe tracks, and anything that needs emotional clarity.

Avoid pairing very high Weirdness with low Style Influence unless the user explicitly wants unpredictable results. When troubleshooting, adjust sliders in small moves of 5-10 percentage points and regenerate; do not rewrite the whole prompt at the same time.

## Excluded Styles

Use Suno's `Excluded Styles` input as a negative prompt field for vocal/custom modes. Instrumental Mode does not expose this field; put must-avoid traits in `Instrumental Prompt:` instead.

Good exclusions:
- unwanted genres: `country`, `EDM`, `metal`, `trap`
- unwanted instruments: `banjo`, `saxophone`, `distorted guitar`, `808 bass`
- unwanted vocal traits: `male vocal`, `female vocal`, `choir`, `rap vocals`, `spoken word`
- unwanted production or mood: `lo-fi`, `muddy mix`, `comedy`, `children's music`, `happy upbeat tone`

Keep it short and specific. Do not exclude the same thing the Style field asks for, and do not use exclusions to solve lyric problems. If a must-avoid item is critical, include it in `Excluded Styles` and optionally add one plain-language note in `Suno v5.5 Notes:`.

## Songwriting Craft

For deeper lyric craft guidance, read `references/songwriting-craft.md`. For structure decisions, read `references/song-structure.md`. For statement/repetition/twist patterns, read `references/rule-of-3.md`. For hook-first prioritization and fast revision decisions, read `references/eighty-twenty.md`.

Start with a clear central promise: what the singer wants, fears, realizes, or refuses. Every section should move that promise.

- **Verse:** concrete situation, character, memory, conflict, image, or setup.
- **Pre-Chorus:** rising pressure, question, turn, or emotional lift.
- **Chorus:** title/hook, simplest emotional truth, repeatable language, stronger vowels, fewer details.
- **Post-Chorus:** short chant, melodic tag, or repeated phrase when the genre expects it.
- **Bridge:** new angle, confession, contradiction, time jump, or final realization.
- **Outro:** resolve, echo the hook, or leave one memorable image.

Prefer one strong hook over many clever lines. The chorus should be understandable on first listen and worth repeating.

## Build Structure First

Keep each section to 4 lines or a multiple of 4 unless the genre or user request calls for a different form. Common forms:

- Pop: `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Verse 2]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Final Chorus]`
- Rap: `[Intro]`, `[Verse 1]`, `[Chorus]`, `[Verse 2]`, `[Chorus]`, `[Outro]`
- Ballad/folk: `[Verse 1]`, `[Chorus]`, `[Verse 2]`, `[Chorus]`, `[Bridge]`, `[Final Chorus]`
- EDM: `[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Drop]`, `[Verse 2]`, `[Build]`, `[Drop]`, `[Outro]`
- Lofi/instrumental loop: `[Intro]`, `[Theme A]`, `[Theme B]`, `[Breakdown]`, `[Theme A Variation]`, `[Loop Point]`
- OST cue: `[Intro]`, `[Theme A]`, `[Development]`, `[Climax]`, `[Resolution]`, `[Outro]`

## Keep Meter Stable

- Keep line lengths and syllable load close within each section.
- Rewrite outlier lines that are noticeably longer than neighbors.
- Keep chorus phrasing consistent across repeats.
- Use commas for short pauses and periods for clear stops.
- Use repeated vowels for sustain when needed, for example `Goo-o-o-odbye`.
- Use compact, singable syntax. Avoid cramming plot into one line.
- For rap, manage bar length and internal rhyme without making every line dense.
- For country, folk, and singer-songwriter forms, preserve conversational phrasing and clear scene details.
- For non-English lyrics, compare phrase length, natural stress, vowel endings, and breath points in the target language rather than forcing English syllable counts.

If pronunciation is likely to fail, provide phonetic spelling or romanization in-line only when useful. For multilingual outputs, consider a separate `Pronunciation Notes:` section instead of cluttering the lyrics.

## Enforce Anti-Generic Rules

- Avoid overused stock words when they are filler: `neon`, `fire`, `flames`, `shadows`, `echoes`, `broken`, `fading`, `forever`.
- Insert 1 to 3 vivid human details (objects, places, habits, memories).
- Prefer concrete imagery over abstract filler.
- Replace vague emotion labels with behavior, setting, sensory detail, or a sharper claim, but keep strong genre archetypes when they make the hook more singable.
- Avoid AI-default symmetry where every line says the same thing in different words.
- Do not name living artists, bands, or songs in `Style:` (`sounds like <artist>`). Suno's copyright filters can reject or blandly average it. Translate the reference into era, scene, and production traits instead, for example `early-2010s Toronto melodic rap, hazy nocturnal R&B production` rather than naming the artist. A vague request like `happy rock song` is a credit-waster for the same reason: it gives Suno nothing specific to lock onto.

## Separate Vocal Style Field From Lyrics

- Keep vocal/custom style guidance in a compact style line capped at 200 characters.
- Put negative instructions in `Excluded Styles:` when the target mode has that field.
- Keep narrative, section flow, and wording choices in the lyrics body.
- If style text is missing, propose one concise style line.
- Use positive production requests in `Style:`, such as `clean production`, `wide stereo`, `clear vocal upfront`.
- For Instrumental Mode, use `Instrumental Prompt:` instead of `Style:` and `Excluded Styles:`.

## Output Contract

When generating lyrics, return:
1. `Title:` one concise, evocative song title.
2. `Style:` one line, <= 200 characters.
3. `Excluded Styles:` one short line when useful; use `None` if no exclusions are needed.
4. `Lyrics:` section-tagged text ready to paste into Suno Custom Mode.
5. `Language Notes:` only for non-English, bilingual, translated, dialect, script, or pronunciation-sensitive requests.
6. `Suno v5.5 Notes:` only if useful for the request.
7. `Slider Suggestions:` only when useful or requested; include Weirdness and Style Influence ranges, plus a Duration setting (Auto, or a Custom time) when the request has a target length.
8. `Checks:` only when useful or requested; use a brief pass/fail checklist for:
   - 4-line (or multiple-of-4) section pattern
   - chorus repeat consistency
   - overly long lines
   - cliché-word usage
   - vivid detail count
   - style/lyrics separation
   - excluded styles consistency
   - language/dialect fit when applicable

For instrumental outputs, replace lyric-specific checks with:
- `Instrumental Prompt:` plain-language prompt text for Suno Instrumental Mode, not `Style:` or `Excluded Styles:`
- `Arrangement:` section-tagged cue map
- arrangement form
- motif clarity
- section contrast
- loopability or cue arc
- instrumentation consistency
- vocal-texture consistency

## Revision Mode

When revising user-provided lyrics:
1. Determine whether the user wants a close edit or a new song inspired by the reference.
2. Default to transformation, not preservation: keep the theme, emotional intent, perspective, and a few abstract motifs, but write new lines, new images, and a new hook.
3. Do not reuse distinctive lyric phrases, section wording, or repeated hook lines unless the user explicitly asks to keep them.
4. If the reference may be copyrighted or from an existing song, avoid close paraphrase and do not continue it in the same wording or structure. Use a high-level thematic brief instead.
5. Fix structure and line rhythm after the new lyric direction is clear.
6. Replace generic phrases with concrete details.
7. Improve the title and style prompt if they are weak, but label those changes clearly.

When transforming reference lyrics, briefly identify the extracted theme before the rewrite, for example: `Theme extracted: protective love, fear becoming anger, prayer for humility.`

## Remix And Style-Match Mode

When the user wants a **remix or flip** of an existing lyric, a song written **in the style of** a named artist or song, or an **analysis** of supplied lyrics' style, read `references/remix-and-style-match.md`. Key rules:

- Style, cadence, rhyme strategy, structure, and subject matter are fair to imitate; specific lyrics, hooks, and distinctive phrases are not. Output original expression that matches the *fingerprint* (cadence, rhyme density, line shape, diction register, themes): never reproduce or closely paraphrase source lines, and don't quote them back.
- Do not put the artist's name in `Style:` (see Excluded Styles / no-artist-names guidance); describe the sound via era, scene, and production instead. Add a `Style Reference:` line stating what was modeled and that all lyrics are original.
- Pick a fresh subject so the result is clearly its own song, not a re-skin of one track.
- If the harness has web/search, use it to sharpen the style fingerprint (era, themes, techniques), but never pull verbatim lyrics into the working notes or output. Without search, build from general knowledge and say so.
- For remixes of lyrics the user owns or public-domain/licensed material, close rework is fine: confirm ownership if unclear. If the user wants the actual lyrics of a copyrighted song or a near-verbatim continuation, decline and offer a style-match instead.

## Screen-Tied Songs And Cues

For anime openings/endings, TV theme songs, end-credit songs, trailer cuts, idents, and game themes, read `references/screen-music.md`. These are tied to picture and to an edit length. Route the output shape by format: anime OP/ED, end-credit songs, and sitcom themes with words are vocal songs (`Lyrics:`); trailer cuts, atmospheric main titles, idents, and game cues are instrumental (`Instrumental Prompt:` plus `Arrangement:`). State the edit length (full / TV-size ~90s / sting ~30-60s / ident ~3-15s) in `Suno v5.5 Notes:`, make the hook or motif land early, end non-looping cuts with `[End]`, and mark loopable themes with `[Loop Point]`.

## Personas And Albums

For a reusable artist identity (a consistent singer, rapper, or band across many songs), read `references/personas.md`. For a cohesive multi-track album or EP, read `references/albums.md`. Both work by writing a small Markdown spec file into the **user's working directory** that later requests load and follow:

- Personas live at `personas/<slug>.md`; albums at `albums/<slug>.md`. Create the directory if needed. Never overwrite an existing spec file without confirming. These files belong in the user's project, not in the skill repo.
- A persona can come from the user's own description or from a style-reference (a real artist or group). For style-references, decode the style, cadence, and vocal character into a fingerprint per `references/remix-and-style-match.md` and keep the real name out of the spec's operational sections and out of every prompt: the persona is a fictional act with a user-chosen name.
- An album may link a persona; if so, the persona's vocals, cadence, and lyrical fingerprint carry across every track, and the album adds a concept, a shared sonic palette, cohesion rules (what's constant vs what may vary: 80/20 over a tracklist), recurring elements, and a sequenced tracklist.
- When the user asks for a song "as <persona>" or "track N of <album>", read the spec file(s), build the song to match (the Style kernel + the specific song's mood/tempo/theme; consistent vocals, cadence, lyrical fingerprint; the album's cohesion rules), apply the spec's Suno defaults, then update the spec's Song Log / tracklist. Add a `Persona:` and/or `Album:` line to the output and the matching consistency items to `Checks:`.
- If a request conflicts with a saved persona or album (a ballad persona asked for a death-metal track), flag it and ask whether to bend the spec for one song or update the spec.

## Portability Beyond Suno

When the user wants prompts for other AI music tools, keep the same songwriter-first process but adapt labels:

- Use `Style Prompt` instead of `Style` if the tool has one freeform prompt field.
- Keep bracket tags unless the target tool discourages them.
- Avoid relying on Suno-only terms like `My Taste`, `Voices`, or `Custom Models` unless the user is using Suno.
- Keep tempo, vocal identity, instrumentation, mood, and structure explicit because those transfer well across tools.
