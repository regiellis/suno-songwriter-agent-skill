# Style Selection

Use this reference when genre, vocalist, instrumentation, or production palette is missing, too generic, or at risk of repeating a previous sound.

## Anti-Lock-In Rule

Before finalizing a Style line, ask whether it was chosen because of this specific request or copied from a prior example.

If it was copied from habit, replace at least three dimensions:
- genre/subgenre
- BPM range
- vocal identity
- rhythm section
- lead instruments
- production texture
- structure tags

Do not reuse `cinematic alt-R&B`, `gospel pads`, `warm male vocal`, `piano and strings`, or similar defaults unless requested or clearly justified by the brief.

## Translating Reference Artists

When the user says "make it sound like [artist or band]", do not pass the name through to `Style:`. Suno's copyright filters can reject it or return a flattened result. Decode the reference into traits instead:

- era / decade and scene: `late-90s East Coast hip hop`, `early-2010s Toronto melodic rap`, `1980s Manchester post-punk`
- rhythm section: tempo feel, drum character, bass role
- lead/signature sound: the instrument or texture most associated with that sound
- production character: lo-fi vs hi-fi, analog vs digital, dry vs cavernous, narrow vs wide

Example: instead of `sounds like a boom-bap legend`, write `late-90s East Coast boom bap, dusty and hard-hitting, chopped soul sample, knocking SP-1200 drums, upright bass, gritty vinyl mix`. This is also more portable to other AI music tools.

## Style Selection Matrix

| Theme / Intent | Possible Lanes | Notes |
| --- | --- | --- |
| grief, regret, apology | acoustic folk, piano ballad, soul, indie rock, modern country | Choose intimacy or catharsis; do not always choose piano ballad. |
| confidence, ambition, rivalry | trap, drill, pop rap, rock anthem, phonk | Match aggression level to the user's tone. |
| romantic joy, summer, movement | dance pop, afrobeats, reggaeton, disco, house | Use brighter tempos and percussion-forward production. |
| spiritual struggle, prayer, redemption | gospel, soul, folk, cinematic pop, worship, blues rock | Gospel is one option, not the default. |
| surreal, chaotic, experimental | hyperpop, art pop, glitch, psychedelic rock, ambient | For vocal/custom modes, raise Weirdness and keep a few guardrails; for Instrumental Mode, make the prompt texture more specific. |
| story song, memory, small-town detail | country, Americana, folk, singer-songwriter, indie rock | Prioritize plainspoken detail and narrative arc. |
| menace, night drive, tension | dark synthpop, techno, trap, industrial, post-punk | In vocal/custom modes, use Excluded Styles to prevent unwanted drift; in Instrumental Mode, put must-avoid traits in the prompt. |
| study, focus, low-distraction background | lofi chillhop, ambient, downtempo, jazzhop, soft house | Use no vocals and loopable arrangement tags. |
| game or film scene | orchestral, hybrid trailer, chiptune, ambient, synthwave, post-rock | Structure around cue function, not lyric hooks. See `references/instrumental.md`. |
| screen-tied song (anime OP/ED, TV theme, end-credit song, trailer) | J-rock/J-pop anime OP, mellow anime ED, sitcom theme, atmospheric main title, hybrid trailer cue, needle-drop ballad | Pick the format first; it dictates length, structure, and whether it's a vocal song or a cue. See `references/screen-music.md`. |
| multilingual pop or regional vocal song | Latin pop, reggaeton, bachata, bossa nova, chanson, J-pop, city pop, K-pop, Korean ballad, K-hip hop, Korean indie, Afrobeats, Bollywood-inspired, Arabic pop, trot | Match lyric phrasing to the language, not only the genre label. "Korean music" spans many lanes beyond K-pop. See `references/multilingual.md`. |

## Vocal Identity Options

Choose intentionally:
- intimate male vocal
- airy female vocal
- raw group vocals
- whispered vocal
- spoken-word vocal
- clean rap vocal
- melodic rap vocal
- choir-backed vocal
- duet
- no vocals

Avoid defaulting to male vocal or female vocal when the user did not specify. If the vocal identity matters, ask or label the assumption.

## Production Texture Options

Use varied production language:
- polished radio mix
- raw basement production
- warm tape texture
- glossy synth production
- live band energy
- sparse acoustic room
- wide cinematic mix
- dry upfront vocal
- dusty vinyl texture
- heavy sidechain pump
- intimate bedroom production
- orchestral hall ambience

## Style Prompt Examples

### Pop

```text
catchy upbeat pop, bright and confident, 118 BPM, energetic vocal, glossy synths and punchy drums, polished radio mix
```

### Garage Rock

```text
garage punk, restless and defiant, 148 BPM, shouted group vocals, distorted guitars and live drums, raw basement production
```

### Trap

```text
dark trap, tense and focused, 140 BPM, melodic rap vocal, heavy 808s, sparse bells, atmospheric pads, clean vocal mix
```

### Country

```text
modern country ballad, plainspoken and bittersweet, 74 BPM, heartfelt vocal, acoustic guitar, pedal steel, warm live-room mix
```

### Afrobeats

```text
afrobeats pop, joyful and romantic, 105 BPM, smooth lead vocal, syncopated percussion, bright guitars, polished dance mix
```

### House

```text
melodic house, uplifting sunrise mood, 124 BPM, ethereal vocal chops, rolling bassline, lush pads, euphoric festival drop
```

### Chanson

```text
modern French chanson, wistful and elegant, 82 BPM, intimate French vocal, accordion, piano, brushed drums, warm cafe ambience
```

### Instrumental Score

```text
instrumental hybrid orchestral trailer cue, 118 BPM, low strings, brass swells, taiko hits, synth pulses, heroic final climax, no lead vocals
```
