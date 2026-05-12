# Output Templates

Use these templates as starting points. Keep final outputs focused on the user's request rather than dumping every field when it is not needed.

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

Language Notes: <target language, dialect/region, script, translation/adaptation mode, pronunciation guidance if useful>

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

[Outro]
...

Suno v5.5 Notes:
- <only include if useful>

Slider Suggestions:
- Weirdness: <range and reason>
- Style Influence: <range and reason>

Checks:
- Structure:
- Chorus consistency:
- Long lines:
- Cliche risk:
- Vivid details:
- Field separation:
- Excluded styles consistency:
- Language/dialect fit:
```

## Instrumental Output Skeleton

```text
Title: <short title>

Style: <instrumental genre, mood, BPM, instruments, production, cue function, no vocals; <=200 chars>

Excluded Styles: <vocals, unwanted genres, unwanted instruments, unwanted moods, or production traits; use None if not needed>

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

Slider Suggestions:
- Weirdness: <range and reason>
- Style Influence: <range and reason>

Checks:
- Arrangement form:
- Motif clarity:
- Section contrast:
- Loopability or cue arc:
- Instrumentation consistency:
- Excluded vocal consistency:
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
- Weirdness: <range and reason>
- Style Influence: <range and reason>

Checks:
- Structure:
- Singable phrase length:
- Hook clarity:
- Language/dialect fit:
- Natural stress and vowel flow:
- Field separation:
- Excluded styles consistency:
```

## Quick Vocal Prompt Pattern

```text
Use $suno-lyrics to write a <genre> song about <theme>.
Mood: <mood>.
Vocal: <vocal identity or trained Voice>.
Language: <language, dialect/region, script preference>.
Include these details: <detail 1>, <detail 2>.
Avoid in lyrics: <words or themes>.
Exclude from sound: <genres, instruments, vocal traits, moods, or production choices>.
Return title, Suno v5.5 style line, excluded styles, Custom Mode lyrics, notes, slider suggestions, and checks.
```

## Quick Instrumental Prompt Pattern

```text
Use $suno-lyrics to create a Suno v5.5 instrumental <lofi beat / OST cue / ambient track / game loop>.
Mood: <mood>.
Use: <instruments, tempo, production texture>.
Scene or use case: <study loop, boss battle, title screen, sad film cue, menu music>.
Exclude from sound: <vocals, genres, instruments, moods, or production choices>.
Return title, style line, excluded styles, arrangement, notes, slider suggestions, and checks.
```
