# Instrumental And Score

Use this reference for non-lyric or mostly non-lyric tracks: lofi beats, OST cues, game loops, ambient, trailer music, underscore, menu themes, battle themes, meditation music, and background music.

## Instrumental Mode Rules

- Use `Arrangement:` instead of `Lyrics:`.
- Put `no vocals` in `Style:` or `Excluded Styles:` unless vocal chops, choir, chants, or syllables are wanted.
- Write section tags as musical cue directions, not sung lyrics.
- Describe motif, texture, rhythm, dynamics, transitions, and loopability.
- Use checks for form, cue clarity, loopability, instrumentation, and excluded vocal consistency.

## Lofi / Chillhop

Style prompt ingredients:
- BPM: 68-88
- groove: dusty drums, swung hats, soft kick, vinyl texture
- harmony: Rhodes, felt piano, jazz guitar, muted keys
- bass: upright bass, soft sub, warm electric bass
- mood: cozy, rainy, late-night, study, reflective
- structure: loopable, subtle A/B variation, no big climax

Section form:

```text
[Intro]
[Theme A]
[Theme B]
[Breakdown]
[Theme A Variation]
[Loop Point]
```

Checklist:
- Can it loop without a hard ending?
- Is the melody simple enough for focus?
- Are transitions subtle?
- Are vocals excluded unless requested?

## OST / Soundtrack Cue

Define the scene function first:
- title screen
- village exploration
- reveal
- chase
- boss battle
- aftermath
- credits
- emotional flashback

Prompt ingredients:
- ensemble: strings, brass, woodwinds, choir, synths, percussion
- motif: short memorable phrase or interval
- arc: mystery to danger, grief to hope, calm to battle
- dynamics: sparse intro, swelling development, full climax, soft resolution
- cinematic texture: orchestral, hybrid, chiptune, ambient, post-rock

Section form:

```text
[Intro]
[Theme A]
[Development]
[Climax]
[Resolution]
[Outro]
```

## Game Loop

Game loops need clear repeat points and usually avoid big final endings.

Section form:

```text
[Intro]
[Loop A]
[Loop B]
[Intensity Layer]
[Breakdown]
[Loop Return]
```

Rules:
- Make `[Loop Return]` explicit.
- Avoid a final cadence unless the user asks for a stinger.
- Keep melody memorable but not fatiguing.
- Use layers for intensity rather than totally new sections.

## Ambient / Meditation

Prompt ingredients:
- slow pulse or no pulse
- evolving pads
- drones
- bells
- bowls
- soft noise
- field recordings
- minimal harmonic movement

Section form:

```text
[Fade In]
[Texture A]
[Subtle Shift]
[Deep Hold]
[Release]
[Fade Out]
```

Use low Weirdness for stable meditation; higher Weirdness for dark ambient or experimental sound design.

## Trailer / Epic Cue

Prompt ingredients:
- tempo: 90-140 depending on action level
- percussion: taiko, toms, hybrid impacts
- harmony: low strings, brass, choir, synth pulses
- arc: tension bed, build, drop, climax, button ending

Section form:

```text
[Tension Intro]
[Pulse Build]
[Break]
[Full Climax]
[Final Hit]
```

## Vocal Chops And Non-Lexical Vocals

"Instrumental" does not always mean "zero human voice." Many tracks want wordless vocals as texture: chopped/pitched samples, choir "aahs", "oohs", "la la" hooks, chants, hums, breaths.

If the user wants these:
- Do **not** put a blanket `no vocals` in `Style:`/`Excluded Styles:` — that fights the request. Instead exclude only what you don't want, e.g. `Excluded Styles: lead vocals, rap vocals, spoken word`.
- Describe the wordless vocal in `Style:`: `ethereal vocal chops`, `wordless choir aahs`, `chanted "hey" hook`, `breathy hums`.
- In `Arrangement:`, mark where they enter: `[Theme B] add chopped vocal stabs over the groove`, `[Climax] full wordless choir`.
- If you need actual syllables sung, put them in `Lyrics:` with section tags and keep them non-lexical (`Ooh, ah, na na na`), and say so in `Suno v5.5 Notes:`.

If the user genuinely wants nothing vocal at all, keep `no vocals` in both fields and exclude `choir`, `vocal chops`, and `chants` explicitly.

## Stems And Handoff

When the instrumental is headed for a DAW, a video edit, or layering with live performance, mention stems in `Suno v5.5 Notes:` (e.g. `Plan: generate, pick take, split stems, score to picture`). For loops and stingers, note that Crop can trim the take to length. See `references/studio-and-iteration.md` for the full post-generation workflow.

## Instrumental Output Checks

- Arrangement form:
- Motif clarity:
- Section contrast:
- Loopability or cue arc:
- Instrumentation consistency:
- Dynamic arc:
- Excluded vocal consistency:

## Example Style Lines

```text
lofi chillhop, relaxed 78 BPM, no vocals, dusty drums, mellow Rhodes, soft upright bass, vinyl texture, loopable study beat
```

```text
orchestral fantasy OST cue, 92 BPM, no vocals, strings, harp, low brass, taiko swells, mysterious village-to-battle arc
```

```text
dark ambient drone, slow 55 BPM pulse, no vocals, evolving pads, bowed textures, distant bells, slow tension build, no drums
```
