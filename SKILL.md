---
name: suno-lyrics
description: Use this skill when the user wants to write, revise, translate, adapt, or prompt an AI-generated song or instrumental track, especially for Suno v5.5 Custom Mode. Apply it for lyrics, hooks, multilingual songs, language/dialect choices, song structure, style prompts, instrumental arrangement notes, lofi beats, OST/soundtrack cues, genre/mood/BPM/vocal/instrument direction, Voices, Custom Models, My Taste, anti-generic rewrites, and portable prompts for other AI music tools. Trigger even if the user asks casually for a song, chorus, verse, rap, ballad, foreign-language lyric, translation, instrumental, background music, or "make this work in Suno." Do not use for unrelated music theory, audio engineering, DAW mixing, licensing, or factual questions about artists.
---

# Suno Songs, Lyrics, And Instrumental Prompts

Use this skill to create release-quality AI song inputs. Target Suno v5.5 first, then keep the result portable enough for other AI music systems by separating style, lyrics, structure, and performance notes.

Use references selectively:
- Read `references/templates.md` first only when you need the reference index.
- Read `references/output-templates.md` for complete output skeletons and quick invocation patterns.
- Read `references/suno-v55-controls.md` for Style, Excluded Styles, Weirdness, Style Influence, Voices, Custom Models, My Taste, or Suno troubleshooting.
- Read `references/songwriting-craft.md` for lyric writing, revision, hooks, rhyme, meter, vivid detail, and reference-lyric transformation.
- Read `references/song-structure.md` when choosing or fixing verse/chorus order, pre-chorus use, bridge placement, AABA/AAA forms, 12-bar blues, EDM/drop forms, rap forms, or instrumental cue forms.
- Read `references/rule-of-3.md` when improving memorability, repeated phrases, melodic/rhythmic motifs, chorus payoff, or arrangement focus.
- Read `references/eighty-twenty.md` when prioritizing the hook, identifying the highest-impact 20%, reducing over-polish, or balancing familiar genre signals with fresh ideas.
- Read `references/instrumental.md` for lofi, OST, game loops, ambient, trailer cues, or other non-lyric tracks.
- Read `references/multilingual.md` for non-English lyrics, translation, bilingual writing, dialect, script, romanization, or pronunciation.
- Read `references/style-selection.md` when genre, vocalist, instrumentation, or production palette is missing, generic, or over-reused.

## Core Workflow

1. Clarify the song goal from the user request: theme, genre, language/dialect, vocalist or instrumental mode, audience, emotional arc, and whether they need lyrics, arrangement notes, a style prompt, or all of them.
2. Build the song as a song, not just a prompt: title, core idea, hook, section map, melodic phrasing assumptions, then final lyrics.
3. If the user provides existing lyrics, treat them as reference material for theme and direction unless they explicitly ask for a close edit, preservation, or line-by-line rewrite.
4. Choose the sound from the user's request. If genre, vocalist, or production style is missing, either ask a concise follow-up or infer a fitting direction from the theme and label it as an assumption. Do not default to one recurring palette.
5. Keep Suno fields clean:
   - `Style:` concise positive direction: genre, mood, tempo, vocal style, instruments, and production. Keep it under 200 characters unless the user asks for a longer prompt.
   - `Excluded Styles:` concise negative direction: genres, instruments, vocal types, moods, or production traits to avoid.
   - `Lyrics:` section-tagged text only when vocals are wanted. Put story and singable words here, not production instructions.
   - `Arrangement:` section-tagged cue map when the track is instrumental or non-lyric.
6. When relevant, include short `Suno v5.5 Notes:` for Voices, Custom Models, My Taste, Studio, stems, remaster, or iteration strategy.
7. For Suno Custom Mode, include `Slider Suggestions:` when the user asks for prompt settings, troubleshooting, or a complete Suno-ready package.
8. Add a compact `Checks:` section covering structure, meter, hook clarity, cliche risk, and prompt-field separation.

## Suno v5.5 Prompting

Use bracketed section tags. For vocal songs:
- `[Intro]` for a short setup
- `[Verse 1]` and later verses for story/detail
- `[Chorus]` for repeated hook lines
- `[Bridge]` for a contrast or twist before the final chorus
- `[Outro]` or `[Coda]` to close

For instrumentals:
- `[Intro]`, `[Theme A]`, `[Theme B]`, `[Breakdown]`, `[Build]`, `[Climax]`, `[Loop Point]`, `[Outro]`
- For lofi/background music, prefer loopable sections and subtle variation.
- For OST cues, describe scene function, motif, dynamics, instrumentation, and emotional turn.

Suno v5.5 responds well to clear, natural-language style prompts. Include the most important descriptors early:

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

## Instrumental Mode

Use Instrumental Mode when the user asks for no vocals, lofi beats, study music, meditation, game music, film/TV score, trailer music, background music, underscore, ambience, OST, theme music, battle music, menu music, or a soundtrack cue.

In Instrumental Mode:
- Put `no vocals` or a precise vocal exclusion in `Style:` and/or `Excluded Styles:`.
- Return `Arrangement:` instead of `Lyrics:` unless the user asks for vocal chops, chants, or non-lexical syllables.
- Write section tags as musical cue directions, not sung lyrics.
- Describe motif, texture, rhythm, dynamics, transitions, and loopability.
- Avoid lyric checks such as rhyme and chorus wording; check form, cue clarity, loopability, instrumentation, and excluded vocal consistency.

Instrumental examples:
- lofi: `lofi chillhop, relaxed 78 BPM, dusty drums, mellow Rhodes, soft upright bass, vinyl texture, loopable study beat, no vocals`
- OST: `orchestral fantasy OST cue, 92 BPM, strings, harp, low brass, taiko swells, mysterious village-to-battle arc, cinematic dynamics, no vocals`
- ambient: `dark ambient drone, 55 BPM pulse, evolving pads, bowed textures, distant bells, slow tension build, no drums, no vocals`

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

Suno's Custom Mode Creative Sliders shape how much the model explores and how strictly it follows the style input. Use ranges, not false precision.

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

Use Suno's `Excluded Styles` input as a negative prompt field. Put unwanted sound traits there instead of crowding the positive Style field with many `no...` phrases.

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

- Avoid overused stock words unless the user asks for them explicitly: `neon`, `fire`, `flames`, `shadows`, `echoes`, `broken`, `fading`, `forever`.
- Insert 1 to 3 vivid human details (objects, places, habits, memories).
- Prefer concrete imagery over abstract filler.
- Replace vague emotion labels with behavior, setting, sensory detail, or a sharper claim.
- Avoid AI-default symmetry where every line says the same thing in different words.

## Separate Style Field From Lyrics

- Keep style guidance in a compact style line capped at 200 characters.
- Put negative instructions in `Excluded Styles:` when the target tool has that field.
- Keep narrative, section flow, and wording choices in the lyrics body.
- If style text is missing, propose one concise style line.
- Use positive production requests in `Style:`, such as `clean production`, `wide stereo`, `clear vocal upfront`.

## Output Contract

When generating lyrics, return:
1. `Title:` one concise, evocative song title.
2. `Style:` one line, <= 200 characters.
3. `Excluded Styles:` one short line when useful; use `None` if no exclusions are needed.
4. `Lyrics:` section-tagged text ready to paste into Suno Custom Mode, or `Arrangement:` for instrumental/non-lyric tracks.
5. `Language Notes:` target language, dialect, script, translation/adaptation choices, and pronunciation notes when useful.
6. `Suno v5.5 Notes:` only if useful for the request.
7. `Slider Suggestions:` include Weirdness and Style Influence ranges when useful.
8. `Checks:` a brief pass/fail checklist for:
   - 4-line (or multiple-of-4) section pattern
   - chorus repeat consistency
   - overly long lines
   - cliché-word usage
   - vivid detail count
   - style/lyrics separation
   - excluded styles consistency
   - language/dialect fit when applicable

For instrumental outputs, replace lyric-specific checks with:
- arrangement form
- motif clarity
- section contrast
- loopability or cue arc
- instrumentation consistency
- excluded vocal consistency

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

## Portability Beyond Suno

When the user wants prompts for other AI music tools, keep the same songwriter-first process but adapt labels:

- Use `Style Prompt` instead of `Style` if the tool has one freeform prompt field.
- Keep bracket tags unless the target tool discourages them.
- Avoid relying on Suno-only terms like `My Taste`, `Voices`, or `Custom Models` unless the user is using Suno.
- Keep tempo, vocal identity, instrumentation, mood, and structure explicit because those transfer well across tools.
