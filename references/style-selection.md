# Style Selection

For genre-specific phrasing and form, use `genre-songwriting.md`; sound selection follows those writing choices.

Use this reference when genre, vocalist, instrumentation, or production palette is missing, too generic, or at risk of repeating a previous sound.

Everything here is a set of suggestions for making a choice. None of it is the answer for a genre, and the example lines are illustrations to learn from, not text to reuse.

## Anti-Lock-In Rule

A Style line that could sit on any song in its genre is a default, whether or not it was copied. Build each one from this request:

1. Take two or three particulars from the brief: the speaker, the place, the time of day or year, the use.
2. Let each particular decide one dimension below. A night-shift narrator can decide tempo and space; a border town can decide the branch and the lead instrument.
3. Compare with any earlier song in the conversation, persona log, or album. For the same lane, change at least three dimensions unless the user wants continuity.

Dimensions to choose and to vary:
- branch, scene, or era of the genre
- tempo and feel
- vocal identity and role
- rhythm section behavior
- foreground instrument
- production texture and space
- form and hook mechanism

Keep `cinematic alt-R&B`, `gospel pads`, `warm male vocal`, `piano and strings`, and similar defaults out unless the brief asks for them. The same applies to any phrase that has started appearing in consecutive outputs.

## Translating Reference Artists

When the user says "make it sound like [artist or band]", do not pass the name through to `Style:`. Suno lists well-known artist names as a possible moderation trigger (see `suno-v6-controls.md` for the official source). Decode the reference into traits instead:

- era / decade and scene: `late-90s East Coast hip hop`, `early-2010s Toronto melodic rap`, `1980s Manchester post-punk`
- rhythm section: tempo feel, drum character, bass role
- lead/signature sound: the instrument or texture most associated with that sound
- production character: lo-fi vs hi-fi, analog vs digital, dry vs cavernous, narrow vs wide

Example: instead of `sounds like a boom-bap legend`, write `mid-90s East Coast boom bap, dusty and hard-hitting, chopped soul sample, knocking SP-1200 drums, upright bass, gritty vinyl mix`. This is also more portable to other AI music tools.

## Style Selection Matrix

| Theme / Intent | Possible Lanes | Notes |
| --- | --- | --- |
| grief, regret, apology | acoustic folk, piano ballad, soul, indie rock, modern country | Choose intimacy or catharsis; do not always choose piano ballad. |
| confidence, ambition, rivalry | trap, drill, pop rap, rock anthem, phonk | Match aggression level to the user's tone. |
| romantic joy, summer, movement | dance pop, afrobeats, reggaeton, disco, house | Use brighter tempos and percussion-forward production. |
| spiritual struggle, prayer, redemption | gospel, soul, folk, cinematic pop, worship, blues rock | Gospel is one option, not the default. |
| surreal, chaotic, experimental | hyperpop, art pop, glitch, psychedelic rock, ambient | Name the strange element and its role first; raise Weirdness only when the user has the slider and wants less predictable takes. |
| story song, memory, small-town detail | country, Americana, folk, singer-songwriter, indie rock | Prioritize plainspoken detail and narrative arc. |
| menace, night drive, tension | dark synthpop, techno, trap, industrial, post-punk | Decide whether the tension comes from pulse, space, or timbre; add Excluded Styles only for drift the user named or heard. |
| study, focus, low-distraction background | lofi chillhop, ambient, downtempo, jazzhop, soft house | Usually instrumental with a loopable arrangement; enable Instrumental instead of writing a negative phrase into the prompt. |
| game or film scene | orchestral, hybrid trailer, chiptune, ambient, synthwave, post-rock | Structure around cue function, not lyric hooks. See `references/instrumental.md`. |
| screen-tied song (anime OP/ED, TV theme, end-credit song, trailer) | J-rock/J-pop anime OP, mellow anime ED, sitcom theme, atmospheric main title, hybrid trailer cue, needle-drop ballad | Pick the format first; it dictates length, structure, and whether it's a vocal song or a cue. See `references/screen-music.md`. |
| multilingual pop or regional vocal song | Latin pop, reggaeton, bachata, bossa nova, chanson, J-pop, city pop, K-pop, Korean ballad, K-hip hop, Korean indie, Afrobeats, Bollywood-inspired, Arabic pop, trot | Match lyric phrasing to the language, not only the genre label. "Korean music" spans many lanes beyond K-pop. See `references/multilingual.md`. |

## Vocal Identity Options

Describe a voice by register, texture, and delivery, and choose its role in the song. Some directions, none of them a default:
- low conversational lead, close and dry
- bright nasal lead with a hard attack
- breathy head-voice lead, doubled on the hook
- weathered lead answered by a group
- spoken-word lead over a sung refrain
- clipped rap lead with sparse ad-libs
- melodic rap lead that sustains the last word of each phrase
- two leads trading lines
- choir or crowd carrying the hook while the lead comments
- instrumental, with the Instrumental toggle enabled

Name a gender only when the user did, or label it as an assumption. Register and delivery carry more of the identity; see `v6-production-direction.md` for vocal character wording.

## Production Texture Options

Pick the texture that fits the scene in the brief, and vary it between songs:
- polished radio mix
- raw basement production
- warm tape texture
- glossy synth production
- live band in one room
- sparse acoustic room
- wide cinematic mix
- dry upfront vocal
- dusty vinyl texture
- heavy sidechain pump
- intimate bedroom production
- orchestral hall ambience

## One Lane, Three Takes

The same lane and the same brief can produce very different songs. Brief: a country song about selling the family farm.

Take one treats it as a joke the narrator tells to get through the day:

```text
honky-tonk shuffle, 118 BPM, wry baritone lead, twin fiddles answering each line, walking bass, dry dance-hall room
```

Take two stays inside the last morning in the house:

```text
high-lonesome ballad in 3/4, 84 BPM, lone tenor opens unaccompanied, clawhammer banjo and bowed bass enter on verse two, close room
```

Take three is the drive away:

```text
country rock, 132 BPM train beat, baritone guitar riff between lines, group vocal on the refrain, wide open-road mix
```

All three are country. They differ in branch, tempo and meter, lead instrument, vocal role, and space, and each difference came from a reading of the brief. That is the method to repeat. These three lines are spent: write new ones for the next song, in this lane or any other.
