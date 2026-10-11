# Song Structure

Use this reference when choosing, fixing, or explaining a song form: verse/chorus order, bridge placement, pre-chorus use, instrumental cue form, or genre-specific structures.

## Core Idea

Song structure organizes listener attention. It decides when the song:

- introduces the world
- repeats the hook
- raises anticipation
- contrasts the main idea
- resolves or intensifies

Structure is a tool, not a law. Choose the song's engine first: narrative, refrain, cadence, riff, groove, character action, improvisation, or texture. See `genre-songwriting.md` for lane-specific decisions. Use the form that best serves the hook, story, genre, and energy arc.

## Common Sections

### Intro

Sets tone, groove, key image, or motif.

Use when:
- the genre benefits from atmosphere
- the hook needs setup
- Suno needs a clear starting texture

Keep it short unless the genre expects long build, such as ambient, EDM, or score.

### Verse

Develops story, scene, character, or argument.

Usually:
- same melody each time
- new lyrics each time
- more detail than chorus
- lower energy than chorus

Verse 1 should orient the listener. Verse 2 should add new information, not repeat Verse 1.

### Pre-Chorus

Builds anticipation between verse and chorus.

Use when:
- verse and chorus feel disconnected
- the chorus needs a lift
- pop/dance/K-pop structure is desired
- emotional pressure should rise before the hook

Avoid when:
- the song needs blunt simplicity
- folk/blues form should stay direct
- the chorus already lands naturally

### Chorus

Carries the main message, title, and hook.

Usually:
- repeated lyrics
- repeated melody
- simpler language
- higher emotional clarity
- strongest title placement

The chorus is often the highest-impact 20% of the song. If the chorus is weak, fix it before polishing verses.

### Post-Chorus

Short repeated tag after the chorus.

Use for:
- dance pop
- K-pop
- EDM
- chant hooks
- wordless or vowel hooks

Keep it simple and memorable.

### Bridge

Provides contrast or a turn.

Bridge functions:
- reveal something new
- change perspective
- create musical contrast
- relieve repetition
- set up final chorus payoff

Avoid a bridge when the song is already short, direct, or genre-simple. Some pop, punk, blues, and dance tracks work better without one.

### Outro / Coda

Closes the song.

Can:
- repeat the hook
- reduce to a final image
- fade a motif
- resolve the story
- leave an unresolved question

## Section Tag Descriptors

A section tag can carry a short performance or energy cue, not just a label. Cues such as `[Verse - whispered]` or `[Chorus - explosive]` request section behavior, but may be ignored or sung.

Useful descriptors:
- intensity: `[Quiet Verse]`, `[Half-time Verse 2]`, `[Building Pre-Chorus]`, `[Explosive Chorus]`, `[Double-time Outro]`
- arrangement: `[Bridge - stripped to vocal and piano]`, `[A Cappella Intro]`, `[Drums-only Breakdown]`, `[Full Band Final Chorus]`
- delivery: `[Spoken Verse]`, `[Shouted Chorus]`, `[Harmonized Bridge]`, `[Ad-lib Outro]`

Rules:
- Keep the descriptor to a few words. Long descriptions inside a tag get unreliable.
- Use a descriptor only where the energy or texture actually changes; tagging every section "explosive" flattens the dynamics.
- Keep persistent genre, instrument, and production direction in `Style:` for vocal and Advanced modes. For Instrumental Mode, keep it in `Instrumental Prompt:`.
- For instrumental tracks, cue tags handle moment-to-moment changes: `[Sparse Theme A]`, `[Layered Build]`, `[Climax - full orchestra]`, `[Fade Loop Point]`.

## Common Forms

### ABAB

```text
[Verse 1]
[Chorus]
[Verse 2]
[Chorus]
```

Best for:
- simple pop
- rock
- punk
- children's songs
- short direct songs

Risk: can feel too short unless the hook is strong.

### ABABCB

```text
[Verse 1]
[Chorus]
[Verse 2]
[Chorus]
[Bridge]
[Final Chorus]
```

Best for:
- standard pop
- country
- rock
- singer-songwriter
- emotional ballads

The bridge should earn its contrast through meaning, harmony, rhythm, or texture. It need not rewrite the story.

### Verse / Pre-Chorus / Chorus Pop Form

```text
[Intro]
[Verse 1]
[Pre-Chorus]
[Chorus]
[Verse 2]
[Pre-Chorus]
[Chorus]
[Bridge]
[Final Chorus]
[Outro]
```

Best for:
- modern pop
- dance pop
- K-pop
- R&B-pop
- big emotional builds

Use if the chorus needs anticipation or the production needs a lift.

### AABA / 32-Bar Inspired

```text
[A Section]
[A Section]
[Bridge]
[A Section]
```

Best for:
- jazz standards
- classic pop
- musical theater
- crooner-style songs

Focuses on melodic statement and bridge contrast rather than a modern chorus.

### AAA / Strophic

```text
[Verse 1]
[Verse 2]
[Verse 3]
[Outro]
```

Best for:
- folk
- hymns
- traditional songs
- story songs
- protest songs

Same melody repeats with new lyrics. The story progression must create the interest.

### 12-Bar Blues

```text
[Verse 1]
[Verse 2]
[Solo]
[Verse 3]
[Outro]
```

Best for:
- blues
- blues rock
- roots music

Lyric structure often uses statement, repeated statement, and payoff (AAB). The letters describe lyric relationships, not bar counts. One common musical cycle is four bars centered on I, two on IV, two on I, then V / IV / I / I or V; many variants exist. Allocate vocal phrases and instrumental responses within the chosen cycle. Three lyric lines do not mean three bars.

### EDM / Drop Form

```text
[Intro]
[Verse]
[Pre-Chorus]
[Build]
[Drop]
[Breakdown]
[Build]
[Final Drop]
[Outro]
```

Best for:
- house
- future bass
- techno-pop
- festival tracks

Lyrics can be sparse. The drop functions like the hook.

### Rap Form

```text
[Intro]
[Verse 1]
[Chorus]
[Verse 2]
[Chorus]
[Bridge or Breakdown]
[Final Chorus]
[Outro]
```

Best for:
- hip-hop
- trap
- drill
- pop rap

Verses can carry density; a hook may reset the listener through fewer words or a contrasting cadence. Hookless forms can develop through argument, flow, or beat structure.

## Instrumental Forms

### Lofi Loop

```text
[Intro]
[Theme A]
[Theme B]
[Breakdown]
[Theme A Variation]
[Loop Point]
```

The form should feel repeatable, not final.

### OST Cue

```text
[Intro]
[Theme A]
[Development]
[Climax]
[Resolution]
[Outro]
```

The form follows scene function, not lyric hook logic.

### Game Loop

```text
[Intro]
[Loop A]
[Loop B]
[Intensity Layer]
[Breakdown]
[Loop Return]
```

Make the loop return explicit.

## Screen-Tied Forms

These are tied to picture and to an edit length: see `references/screen-music.md` for the full guidance.

### Anime OP (TV size, ~90s)

```text
[Intro Riff]
[Verse]
[Pre-Chorus]
[Chorus]
[Outro Tag]
[End]
```

Vocal song, fast and anthemic; the instrumental riff bookends it; the hook lands inside 30s. Full version adds a second verse/chorus and often a bridge or solo.

### Anime ED / Needle-Drop Song

Standard pop/ballad form, lower energy than the OP, often just one verse/chorus in a TV cut. End-credit songs deliver payoff and leave the world rather than introduce it.

### TV Theme / Sting (~30-60s)

```text
[Intro Hook]
[Chorus or Single Statement]
[Button]
[End]
```

Hook-first, almost no build. May be a tiny complete song or an instrumental sting.

### Trailer Cut

```text
[Atmospheric Setup]
[Turn / Impact]
[Action Build]
[Climax]
[Button]
```

Instrumental cue (`Arrangement:`), not a song. Teaser cuts compress this; full trailers run two builds. See `references/instrumental.md` § Trailer / Epic Cue.

## Forms Beyond A Pop Section Chain

| Form | Development Mechanism | What To Plan |
| --- | --- | --- |
| Verse with recurring refrain | New events change a fixed line's meaning | Where the refrain belongs inside each verse |
| Riff-led form | Instrumental identity returns between contrasting passages | Vocal gaps, riff variations, and instrumental handoffs |
| Call-and-response / vamp | Fixed response supports changing lead or arrangement | Space for each voice and a deliberate exit |
| Head / improvisation / return | A melody frames exploration | Form length, solo space, and recognizable return |
| Through-composed | New music follows dramatic or textual change | Recurring motives or other continuity without forced choruses |
| Gradual dance development | Parts enter, withdraw, and change over a stable pulse | Phrase-scale events and useful mix-in/mix-out space when requested |
| Suite or sectional hybrid | Distinct sections share or transform material | Transition mechanics and what stays recognizable |
| Texture-led arc | Timbre, register, density, or harmonic field evolves | Listening trajectory without compulsory plot or climax |

AABB in a dance tune names repeated musical strains; AAB in a blues verse can name a lyric pattern. State what letters refer to rather than assuming they always mean verse and chorus.

## Choosing A Structure

Ask:
- Is the hook strong enough to repeat early?
- Does the story need multiple verses?
- Does the chorus need a pre-chorus lift?
- Would a bridge add contrast or slow the song down?
- Is the genre expecting a drop, chant, solo, or loop?
- Is the song lyric-driven or groove-driven?

## Common Fixes

- Chorus arrives too late: shorten Verse 1 or remove Intro.
- Chorus feels weak: diagnose hook landing, phrase contrast, or harmony; add a pre-chorus only if anticipation is missing.
- Song feels repetitive: decide whether repetition is serving groove or recognition; vary the relevant part or add contrast only if needed.
- Song feels cluttered: remove Pre-Chorus or Bridge.
- Verse 2 repeats Verse 1: add new detail, consequence, or time shift.
- Bridge feels pointless: make it reveal, confess, contradict, or reframe.
- Final chorus feels flat: change one line, add harmony, or use Rule of 3 variation.

## Structure Checklist

- Form matches genre and energy goal.
- Chorus or main motif appears early enough.
- Each repeated section earns its repeat.
- Verse 2 adds new information.
- Bridge or contrast section changes meaning or energy.
- Final chorus/drop/motif has a payoff.
- Instrumental forms include loop point or cue resolution when needed.
