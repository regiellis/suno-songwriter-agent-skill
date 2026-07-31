# Output Templates

Use these templates as starting points. Keep final outputs focused on the user's request rather than dumping every field when it is not needed.

For vocal songs, do not let the template outrank the lyric. Draft around the title, hook phrase, section movement, and singability first; then fill only the fields that help the user paste or iterate the song. Default to short, Suno-native lines, not polished prose.

## Core Suno v5.5 Style Template

```text
[genre/subgenre], [mood], [tempo or BPM], [vocal style or no vocals], [instruments], [production feel], [theme or cue function]
```

Example:

```text
<chosen genre/subgenre>, <specific mood>, <BPM>, <vocal identity or no vocals>, <2-4 key instruments>, <production feel>, <song theme or cue function>
```

## Vocal Song Output Skeleton

```text
Title: <short title>

Style: <genre, mood, BPM, vocal style, instruments, production, theme; <=200 chars>

Excluded Styles: <unwanted genres, instruments, vocal traits, moods, or production traits; use None if not needed>

Language Notes: <include only for non-English, bilingual, translated, dialect, script, or pronunciation-sensitive requests>

Lyrics:
[Intro, <short delivery/texture descriptor>]
...

[Verse 1, <delivery descriptor if useful>]
...

[Pre-Chorus, <build descriptor if useful>]
...

[Chorus, <energy descriptor if useful>]
...

[Verse 2]
...

[Bridge, <contrast descriptor if useful>]
...

[Final Chorus]
...

[Outro]
...

Suno v5.5 Notes:
- <only include if useful>

Slider Suggestions:
- <include only when useful or requested; Weirdness and Style Influence ranges>

Checks:
- <include only when useful or requested; keep compact>
```

## Groove-Narrative Vocal Skeleton

Use this when the song is carried by R&B/neo-soul/jazz-hop pocket, spoken-sung storytelling, city-life vignettes, or environmental sound design.

```text
Title: <short title>

Style: <genre, groove, BPM, vocal setup, instruments, production, scene/theme; <=200 chars>

Excluded Styles: <unwanted genres, vocal traits, instruments, production traits; use None if not needed>

Lyrics:
[Intro - <bars/texture/environment/groove cue>]
<optional non-lyrical cue>
(<vocalist cue if useful>)

[Verse 1]
(<vocalist>)
<8-16 lines; couplet-driven, rhythmic, concrete scene movement>

[Chorus - <delivery/energy cue>]
(<vocalist>)
<4 simple, repeatable lines>
(<backing vocal cue if useful>)

[Verse 2]
...

[Bridge - <arrangement drop/build cue>]
(<spoken or sung cue>)
...

[Final Chorus - <fuller instrumentation cue>]
...

[Outro - <fade/spoken/environment cue>]
...

[End or Fade Out]
```

## Instrumental Output Skeleton

```text
Title: <short title>

Instrumental Prompt: <paste-ready natural-language prompt; genre/mood/BPM/instruments/production/cue function/vocal texture; no Style field or sliders>

Arrangement:
[Intro]
<texture, motif, or groove entrance>
<instrumentation and dynamics>

[Theme A]
<main motif or loop material>
<rhythm, harmony, and lead texture>

[Theme B]
<contrast, counter-melody, or new layer>
<energy change>

[Breakdown]
<reduced texture or transition>
<space for loop or scene change>

[Climax or Loop Point]
<highest energy moment or clean loop return>
<ending/resolution instruction>

Suno v5.5 Notes:
- <only include if useful>

Checks:
- <include only when useful or requested; instrumental prompt, arrangement form, motif clarity, section contrast, loopability or cue arc, instrumentation consistency, vocal-texture consistency>
```

## Multilingual Output Skeleton

```text
Title: <title in target language, with English gloss if helpful>

Style: <genre, target-language vocal, mood, BPM, instruments, production, theme; <=200 chars>

Excluded Styles: <unwanted language drift, vocal traits, genres, instruments, or production traits>

Language Notes: <language, dialect/region, native script vs romanization, adaptation choices, pronunciation notes>

Lyrics:
[Intro]
...

[Verse 1]
...

[Pre-Chorus]
...

[Chorus]
...

[Verse 2]
...

[Bridge]
...

[Final Chorus]
...

Suno v5.5 Notes:
- <only include if useful>

Slider Suggestions:
- <include only when useful or requested; Weirdness and Style Influence ranges>

Checks:
- <include only when useful or requested; structure, singable phrase length, hook clarity, language/dialect fit, natural stress and vowel flow, field separation>
```

## Quick Vocal Prompt Pattern

```text
Use $suno-songwriter to write a <genre> song about <theme>.
Mood: <mood>.
Vocal: <vocal identity or trained Voice>.
Language: <language, dialect/region, script preference>.
Include these details: <detail 1>, <detail 2>.
Avoid in lyrics: <words or themes>.
Exclude from sound: <genres, instruments, vocal traits, moods, or production choices>.
Return title, Suno v5.5 style line, excluded styles, Custom Mode lyrics, and any useful notes, slider suggestions, or checks.
```

## Quick Instrumental Prompt Pattern

```text
Use $suno-songwriter to create a Suno v5.5 instrumental <lofi beat / OST cue / ambient track / game loop>.
Mood: <mood>.
Use: <instruments, tempo, production texture>.
Scene or use case: <study loop, boss battle, title screen, sad film cue, menu music>.
Exclude from sound: <vocals, genres, instruments, moods, or production choices>.
Return title, instrumental prompt, arrangement, and any useful notes or checks.
```
