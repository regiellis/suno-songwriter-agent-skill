# Suno Meta-Tags

Use this reference for bracketed and parenthetical cues that go *inside* the `Lyrics:` body, beyond plain section headers. Suno reads these as performance, arrangement, and structure instructions.

## Section Headers vs Inline Cues

Two different things:

- **Section headers** start a section: `[Verse 1]`, `[Chorus]`, `[Bridge]`, `[Theme A]`. Always on their own line.
- **Inline cues** sit between or inside lyric lines and tell Suno to change delivery, hand off vocals, drop in an instrumental moment, add an effect, or stop the song.

Section headers can also carry a short performance descriptor (see `references/song-structure.md` § Section Tag Descriptors): `[Whispered Verse]`, `[Explosive Chorus]`, `[Half-time Verse 2]`.

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

These work in both vocal songs and as structural markers. Keep them sparse: one or two per song. A long stack of solo tags usually produces a muddy jam, not a clean arrangement.

## Vocal Delivery

Cue how a line is sung:

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

Place the cue on its own line directly above the lines it affects, or at the start of a section header. Mid-line cues risk being sung aloud.

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

Use these when the song needs verse trading, a duet chorus, or a featured guest section. Keep the count low: two or three voices is reliable; more tends to blur. If the user has a trained Voice selected, do not fight it with vocal-gender tags.

Parenthetical vocalist labels are also useful for duet/storytelling layouts:

```text
(Male)
(Female - wordless hum, background texture)
(Female - wordless "oooh" echo underneath)
(Male - spoken, intimate)
```

Use them on their own line before the affected passage. Keep the label short enough that it works as a cue, not a lyric.

## Ad-Libs and Backing Phrases

Short parenthetical phrases become backing/ad-lib vocals rather than lead lines:

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

Reliability varies. Treat these as nice-to-have, not load-bearing. If an effect is essential, also describe it in `Style:` for vocal/custom modes or `Instrumental Prompt:` for Instrumental Mode (e.g. `vinyl texture`, `crowd ambience`).

For groove-narrative vocal songs, short arrangement cues can be useful inside the lyric block:

```text
[Intro - 8 bars, bus doors hiss, street ambience, Rhodes and bass groove]
[drums enter bar 7]
[Bridge - drums drop to kick and hi-hat, bass lead]
[Fade to end - bus engine drone, night crickets, Rhodes chord]
```

Use these when the sound design is part of the concept. Avoid overloading every section with long production notes.

## Ending Control

Suno will often invent extra verses or fade awkwardly if the lyric block ends without a signal. Use:

```text
[Outro]
[End]
[Fade Out]
[Hard Stop]
```

`[End]` after the final section is the most reliable way to stop the model adding material. For loopable instrumentals, do the opposite: avoid a hard ending and mark `[Loop Point]`.

## Rules and Failure Modes

- **Tags get sung if placed mid-line:** Keep cues on their own line.
- **Too many tags = ignored or muddy:** Budget tags by purpose. A groove-narrative song can carry more arrangement cues than a pop song, but each cue should affect the recording.
- **Don't put production direction in tags:** Persistent genre/instrument/mix direction belongs in `Style:` for vocal/custom modes or `Instrumental Prompt:` for Instrumental Mode. Tags are for moment-to-moment changes.
- **`[End]` controls length:** If the user complains Suno keeps adding verses, add `[End]`.
- **Brackets in lyrics ≠ Suno-only:** Most other AI music tools that accept bracket tags handle section headers; many do not handle inline cues. Note that when writing portable prompts.

## Output Note

When meta-tags materially shape the arrangement, mention it briefly in `Suno v5.5 Notes:` (e.g. `Uses [Guitar Solo] after Chorus 2 and [End] to cap length`). Do not narrate every tag: the lyric body already shows them.
