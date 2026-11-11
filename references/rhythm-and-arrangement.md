# Rhythm And Arrangement

Use when tempo labels fail to describe the groove, sections lack contrast, or parts compete with a vocal or motif. Treat examples as musical plans to audition, not guaranteed Suno syntax. For time budgets, use `song-matrix.md`; for directed prompts, use `v6-production-direction.md`.

## Specify The Pulse

Tempo, meter, subdivision, and feel are separate decisions. Name the ones that matter to the request.

| Decision | What To Specify | Common Confusion |
| --- | --- | --- |
| Tempo | Pulse rate and beat unit when ambiguous | 90 BPM can support sparse ballad phrasing or dense rap |
| Meter | Beat grouping, such as 4/4, 3/4, or 6/8 | 3/4 and 6/8 both contain six eighth notes but group them differently |
| Subdivision | Straight eighths, sixteenths, triplets, or a swung pair | Swing is unequal timing within a pair, not a tempo change |
| Backbeat | Snare placement and weight | Half-time changes the perceived pulse without requiring a BPM change |
| Pocket | On top of, centered on, or behind the beat | Behind the beat does not mean progressively slowing down |
| Density | How often each part attacks | Busy hi-hats can increase motion over a spacious bass part |

In 3/4, the usual grouping is three quarter-note beats; in 6/8, it is two dotted-quarter beats, each split into three eighths. Write `6/8, dotted-quarter pulse at 72 BPM` if that distinction matters. An eight-bar passage at that pulse lasts about 13.3 seconds: 8 x 2 x 60 / 72. Do not apply a four-quarter-beats-per-bar formula to it.

In 4/4 at 140 quarter-note BPM, a snare on beat 3 can give a 70 BPM half-time impression. Request `140 BPM, half-time backbeat, active sixteenth-note hats` if that is the target. Faster subdivisions do not automatically make the song double-time.

For odd meter, name the grouping: `7/8 grouped 2+2+3`. For syncopation, specify which part anticipates or delays accents while another part anchors the pulse. Avoid calling any busy rhythm a polyrhythm; simultaneous 3-against-2 and a single 3+3+2 accent pattern are different constructions.

## Assign Each Part A Job

A small ensemble with distinct roles often reads more clearly than a long instrument list.

| Role | Useful Direction |
| --- | --- |
| Pulse | Kick and bass establish the downbeat; shaker keeps subdivisions audible |
| Foundation | Bass outlines roots with occasional approach notes |
| Harmony | Guitar or keys sustain or punctuate chords around the singer |
| Hook | Lead instrument repeats one identifiable figure |
| Answer | Short fills occupy the gaps after vocal phrases |
| Texture | Pad, drone, room tone, or percussion adds depth without competing for the lead |

Choose a foreground part per moment. If guitar answers the singer, ask it to fill the rests rather than solo continuously. Separate competing parts through register, rhythm, articulation, or entrances before asking for `clearer mixing`. Low piano chords, sustained low guitar, and busy bass can blur even with clean production.

Describe bass and kick interaction: locked attacks for weight, bass notes between kicks for motion, or sustained bass under a sparse drum pattern. Avoid prescribing sidechain processing when an arrangement change solves the actual problem.

## Build Contrast Deliberately

Choose one or two changes at a section boundary. Keep an identity anchor such as the groove, motif, singer, or recurring instrument.

| Desired Change | Possible Arrangement |
| --- | --- |
| Lift without more volume | Raise melody register, widen voicings, shorten chord duration |
| More momentum at fixed BPM | Add subdivision in percussion; shorten bass articulation |
| Intimate bridge | Remove chord layers and backing vocals; retain pulse in one part |
| Strong return | Brief rest or pickup fill, then restore the established hook |
| Fuller final chorus | Add an answering harmony or countermelody in vocal gaps |
| Maintain heavy verse energy | Keep rhythm guitar and drums active; simplify their competing figures under words |

An intentional dropout is part of the composition. Do not apply `full-band energy throughout` to a brief that asks for a sparse bridge. Put both states in their sections rather than letting global instructions conflict.

## Three Compact Briefs

```text
ska punk, 164 BPM, clipped offbeat guitar upstrokes, walking bass, tight snare backbeat; brass answers vocal rests, gang responses on the chorus
```

```text
slow soul in 6/8, dotted-quarter pulse at 64 BPM, triplet piano figures, restrained bass, brushes; lead vocal leaves space for short organ answers
```

```text
instrumental electro, 128 BPM, syncopated drum-machine kick, clipped octave bass, dry arpeggio hook; thin the middle section to bass and hats before the hook returns
```

These are contrasting examples, not defaults. Preserve the user's chosen tradition and instrumentation.

## Listening Checks

Check pulse and backbeat before deciding the BPM is wrong. Then listen for the foreground part, phrase breathing, section contrast, and ending. At an edit boundary, check downbeat alignment, chord continuity, sustained notes, and reverb tails. Exact loops need audio editing and boundary checks; tags cannot prove a clean join. Without audio, report these as listening targets rather than verified results.
