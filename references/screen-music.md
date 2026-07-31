# Screen Music: Anime, TV, Trailers, Idents

Use this reference for music tied to picture: anime openings and endings, TV theme songs and idents, end-credit songs, trailer cuts, and video-game themes. Some of these are full vocal songs (anime OP/ED, end-credit song); some are pure cues (trailers, idents): route the output shape accordingly.

Relationship to other references:
- Purely instrumental cues (trailer beds, idents, stings, game loops, OST scoring): see `references/instrumental.md`; this file adds the screen-specific forms and editing notes.
- Japanese / Korean lyrics for OP/ED themes: see `references/multilingual.md`.
- Per-lane BPM/instrument/production palettes (anime OP, anime ED, TV theme, city pop, etc.): see `references/genre-palettes.md`.

## Anime Opening (OP)

An OP is a full pop/rock/electronic song with a TV-size edit, not a score cue. Defaults:

- **Genre:** J-rock, J-pop, idol pop, electronic, math-rock-tinged, or city-pop-tinged depending on the show. Shounen action skews energetic rock/electronic; slice-of-life skews bright pop; dark/psychological skews tense, dissonant, or driving electronic.
- **Tempo:** often fast, ~150-185 BPM, but mid-tempo OPs exist. Pick from the show's energy, not a default.
- **Shape (TV size, ~90 seconds):** instrumental hook/riff intro (~8-15s) → short verse → pre-chorus lift → big chorus with the title hook → instrumental tag/button. Full-length adds a second verse/chorus and often a bridge or solo.
- **Signature:** a recognizable instrumental riff (guitar, synth, or piano) that bookends the OP. Make the hook land inside the first 30 seconds.
- **Vocals:** Japanese lead, sometimes with English hook phrases or section labels. Energetic, anthemic, often a soaring chorus.

Section tags for a TV-size OP:

```text
[Intro Riff]
[Verse]
[Pre-Chorus]
[Chorus]
[Outro Tag]
```

Note the cut in `Suno v5.5 Notes:` (e.g. `TV-size edit (~90s): intro riff, one verse, one chorus, button - use [End] to cap it`). For a full version, use the standard pop form.

## Anime Ending (ED)

An ED is usually the OP's quieter counterpart: mid-tempo or slow, reflective, bittersweet. Common lanes: ballad, city pop, acoustic singer-songwriter, dream pop, lo-fi, soft electronic, jazz-pop. Shorter and lower-energy than the OP, Japanese vocals, often a single verse/chorus in the TV cut. Mood typically lands on melancholy, warmth, or quiet resolve: the emotional exhale after the episode.

## TV Theme Songs And Main Titles

- **Sitcom / comedy theme:** short (30-60s), instantly hooky, often a tiny complete song or a vocal sting. Bright, warm, sing-along.
- **Drama / prestige main title:** atmospheric, often instrumental or wordless-vocal, motif-driven, sets tone in 30-90s. Treat like a short OST cue (`Arrangement:`).
- **Reality / competition / talk show:** energetic stings, percussive beds, brand-forward; usually instrumental with optional chant hooks.
- **Cartoon / kids' theme:** fast, simple, narrative ("here's the premise"), big group vocals, lots of repetition.

State the target length and whether it's a full song or a sting. Hooks must land almost immediately: there is no slow build in a 45-second theme.

## End-Credit / Needle-Drop Songs

A full vocal song placed over end credits or a key scene. Write it as a normal song (standard output contract), but aim it: end-credit songs usually deliver emotional payoff, echo the story's theme, and leave the world rather than introduce it. Note the placement intent in `Suno v5.5 Notes:` so the lyrics serve it.

## Trailer Cuts

Trailer music is a cue, not a song: return `Arrangement:`. See `references/instrumental.md` § Trailer / Epic Cue for ingredients. Screen-specific structure (three-beat trailer): atmospheric setup → turn (impact / "braam" / record-scratch) → escalating action build with rising rhythm and risers → climax → button (final hit or sudden silence). Teaser cuts compress this to ~30-60s; full trailers run ~2-2.5 min with two builds. Keep `no vocals` unless the brief wants choir, chants, or a licensed song over the cut (then write it as a separate vocal song).

## Idents, Stings, Bumpers, Logos

3-15 seconds: channel idents, logo audio, segment bumpers, app sounds. Mostly instrumental: one motif, one gesture, a clean resolution or a clean loop. Treat as a micro-cue (`Arrangement:`), describe the single sound idea, and note the exact length. Cross-ref `references/instrumental.md`.

## Video-Game Themes

Title-screen themes, area themes, boss themes, victory stingers: see `references/instrumental.md` § Game Loop and § OST. Themes that loop must avoid a final cadence and mark `[Loop Point]`; victory/defeat stingers are short one-shots with a hard button.

## Edit-Length Guidance

- **Full version:** standard form for the genre.
- **TV size (~90s):** intro hook → one verse → one chorus → tag; use `[End]`.
- **Sting / theme (~30-60s):** intro hook → chorus or single statement → button.
- **Ident (~3-15s):** one motif, one resolution.

Put the chosen length and structure in `Suno v5.5 Notes:`. For anything that should not loop or extend, end the lyric/arrangement block with `[End]` (see `references/suno-meta-tags.md`); for loopable themes, mark `[Loop Point]` and avoid a hard ending.

Hit these lengths with v5.5's Duration control (Custom slider, 0:10-6:00 in 5s steps (see `references/suno-v55-controls.md` § Duration) *and* a structure written to size: set Duration ~5-15s longer than the target cut (e.g. ~1:40 for a TV-size ~90s OP) so the ending resolves, cap with `[End]`, then Crop to the exact time. The slider alone won't compress an oversized lyric. Idents shorter than 10s are below the slider's minimum) generate at 0:10-0:15 and Crop, or use Suno Sounds for the very shortest hits.

## Output Shape

- Anime OP/ED, end-credit song, sitcom theme with words → vocal song output (`Title`, `Style`, `Excluded Styles`, `Lyrics`, `Language Notes` when Japanese/other, and `Suno v5.5 Notes` with the cut; add sliders/checks only when useful or requested).
- Trailer cut, drama main title, ident, game theme → instrumental output (`Instrumental Prompt:` plus `Arrangement:` instead of `Style:` / `Lyrics:`; no sliders; add instrumental checks only when useful or requested).

## Checks (screen-specific, in addition to the usual ones)

- Hook or motif lands inside the first 30 seconds (or sooner for short formats).
- The stated edit length matches the structure actually written.
- Vocal language and register fit the format (e.g. Japanese OP/ED, with English hook only if intended).
- Instrumental cues vs sung lyrics are routed correctly (trailer/ident = `Instrumental Prompt:` + `Arrangement:`, OP/ED = `Lyrics:`).
- Loopable themes mark `[Loop Point]`; non-looping cuts end with `[End]`.
