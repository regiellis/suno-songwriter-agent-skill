# Suno Meta-Tags

Use this reference for bracketed and parenthetical cues inside the `Lyrics:` body, beyond plain section headers. These are prompting conventions, not a documented command language: any cue may be ignored or sung. The tags below are examples of each convention, not a closed vocabulary; write the cue the song needs in the same shape.

## Where Direction Goes

One rule covers every cue in this file:

- **Style** holds persistent genre, instrument, and mix direction. For an instrumental package that is the `Instrumental Prompt`, which maps to Styles in Advanced with Instrumental enabled (see `suno-v6-controls.md`).
- **A tag** carries a change that happens at that moment: a section starts, a voice hands off, the band drops out, the song ends.
- **Parentheses** hold only words meant to be sung.

## Section Headers vs Inline Cues

Two different things:

- **Section headers** start a section: `[Verse 1]`, `[Chorus]`, `[Bridge]`, `[Theme A]`. Always on their own line.
- **Inline cues** sit between lyric lines and tell Suno to change delivery, hand off vocals, drop in an instrumental moment, add an effect, or end the song.

A section header can carry a short descriptor after a plain hyphen: the section name, ` - `, then a few lowercase words. `[Verse - whispered]`, `[Chorus - explosive]`, `[Verse 2 - half-time]`. See `song-structure.md` § Section Tag Descriptors. Standalone cues that are not a section plus descriptor keep their own form: `[Guitar Solo]`, `[Instrumental Break]`, `[End]`.

## Instrumental Moments

Put these on their own line where the band should take over:

```text
[Guitar Solo]
[Instrumental Break]
[Drum Break]
[Piano Interlude]
[Saxophone Solo]
[Beat Drop]
[Build]
[Breakdown]
```

These work in vocal songs and as structural markers in instrumentals. Keep them sparse: one or two per song. A long stack of solo tags usually produces a muddy jam, not a clean arrangement.

## Vocal Delivery

Cue how a passage is sung:

```text
[Spoken]
[Whispered]
[Shouted]
[Belted]
[Falsetto]
[Soft]
[Aggressive]
[Vocoder]
[Layered Vocals]
[Harmonies]
[Call and Response]
```

Place the cue on its own line directly above the lines it affects, or fold it into the section header as a descriptor: `[Verse 2 - whispered]`. Mid-line cues are the likeliest to be sung aloud.

## Multiple Vocalists

Hand off between voices:

```text
[Male Voice]
[Female Voice]
[Duet]
[Both]
[Choir]
[Group Vocals]
[Child Voice]
[Narrator]
```

Use these when the song needs verse trading, a duet chorus, or a featured guest section. Keep the count low and audition the hand-offs; distinct voices are not guaranteed. If the user has a trained Voice selected, do not fight it with vocal-gender tags. To steer the singer's gender for the whole take, the control is the Vocal Gender dropdown under the advanced options (see `suno-v6-controls.md` § Vocal Gender), not a tag.

A vocalist label can take a short descriptor in the same hyphen form:

```text
[Female Voice - wordless hum]
[Male Voice - spoken, close]
[Group Vocals - answer only]
```

Use them on their own line before the affected passage. Keep the label short enough that it works as a cue, not a lyric.

## Ad-Libs and Backing Phrases

Short parenthetical phrases suggest backing or ad-lib vocals, but may be delivered as lead lines:

```text
I'm not coming back (no no)
Hold the line (hold it)
Say it again (say it, say it)
```

Use sparingly in choruses, post-choruses, and rap hooks. Long parentheticals get sung as lead and clutter the line.

## Sound Effects and Texture

Suno will attempt ambience or one-shot effects from tags like:

```text
[Applause]
[Crowd Cheering]
[Laughing]
[Phone Ringing]
[Rain]
[Vinyl Crackle]
[Static]
[Door Slam]
[Footsteps]
```

Reliability varies. Treat these as nice-to-have, not load-bearing. If an effect is essential, also describe it in `Style` (or the `Instrumental Prompt` for an instrumental package), for example `vinyl texture` or `crowd ambience`.

When the sound design is part of the concept, short arrangement cues can sit in the lyric block. Keep each descriptor to a few words:

```text
[Intro - Rhodes and bass]
[Verse 1 - street ambience]
[Bridge - kick and bass only]
[Outro - fade on engine drone]
```

A longer scene-setting tag (`[Intro - 8 bars, bus doors hiss, street ambience, Rhodes and bass groove]`) is a tradeoff: it can set a scene, but it gets less reliable as it grows and is more likely to be sung. Move the persistent part of that scene into Style and keep the tag for what changes.

## Ending Control

Suno will often invent extra verses or fade awkwardly if the lyric block ends without a signal. Use:

```text
[Outro]
[Fade Out]
[End]
```

`[End]` after the final section requests closure; it cannot guarantee that generation stops there. `[Hard Stop]` appears in community prompts and is not documented Suno syntax; like `[End]`, it requests closure at most. Give the last sung line a section after it (see `v6-production-direction.md` § Endings), then Crop an unwanted tail or edit the generated audio when precision matters. For loopable instrumentals, do the opposite: avoid a hard ending and mark `[Loop Point]`.

## Rules and Failure Modes

- **Mid-line tags get sung:** Keep cues on their own line.
- **Too many tags get ignored or turn muddy:** Budget tags by purpose. A groove-narrative song can carry more arrangement cues than a pop song, but each cue should change the recording.
- **Persistent direction lives in Style:** A tag marks a change at its moment; see Where Direction Goes.
- **`[End]` requests closure:** If the user complains Suno keeps adding verses, add `[End]`.
- **Other tools may not read bracket cues:** Check whether the target tool supports section headers or inline cues before carrying them across, and say so when writing portable prompts.

## Output Note

When meta-tags materially shape the arrangement, mention it briefly in `Suno v6 Notes:` (e.g. `Uses [Guitar Solo] after Chorus 2 and [End] to cap length`). Do not narrate every tag: the lyric body already shows them.
