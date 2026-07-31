# Skill Evals And Smoke Tests

Use this reference to manually test whether the skill behaves correctly across common task types. These are harness-agnostic smoke tests, not a replacement for automated trigger evaluation.

## How To Use

For each test:

1. Run the prompt through an agent with this skill available.
2. Check whether the skill triggers.
3. Check whether the response uses the expected output shape.
4. Check whether the relevant reference behavior appears.
5. Record pass/fail notes and any regression.

If a harness supports trigger logs, confirm that `suno-songwriter` was loaded for should-trigger cases and not loaded for should-not-trigger cases.

## Core Output Contract Checks

Vocal outputs should usually include:
- `Title`
- `Style`
- `Excluded Styles`
- `Lyrics`
- `Suno v5.5 Notes` when useful
- `Slider Suggestions` when Suno settings are requested or a full package is implied
- `Checks` when useful or requested

Vocal lyrics should pass the lyric quality gate:
- title or hook phrase appears in or near the chorus
- chorus is mechanically simpler and more repeatable than the verses
- lines are compact and naturally singable, usually 5-9 words
- end rhyme or vowel rhyme supports the flow unless the genre asks otherwise
- performance descriptors are used in section tags when they improve delivery
- point of view and tense are stable unless a shift is deliberate
- at least one concrete human detail appears outside the chorus
- no obvious overlong mouthful lines

Instrumental outputs should use:
- `Title`
- `Instrumental Prompt`
- `Arrangement`
- no `Style`, `Excluded Styles`, or `Slider Suggestions`
- instrumental checks when useful or requested, not lyric checks

Multilingual outputs should include:
- `Language Notes`
- target language/dialect/script decisions
- singable adaptation choices when translating

## Smoke Test Matrix

| ID | Task Type | Prompt | Expected Behavior |
| --- | --- | --- | --- |
| V1 | Vocal song | `Use $suno-songwriter to write a modern country song about a father driving through the night to pick up his kid. Male vocal, hopeful but tired.` | Produces lyrics, country-appropriate style, no hard-coded alt-R&B defaults, concrete details, checks. |
| V2 | Hook rewrite | `Use $suno-songwriter to make this chorus more memorable: I miss you every day / I wish you would stay / I feel so far away.` | Focuses on hook, likely uses Rule of 3 or 80/20, does not overbuild full song unless asked. |
| V3 | Suno-native flow | `Use $suno-songwriter to write an R&B song about leaving for Japan after a breakup and finding love for the country and a person.` | Uses compact 4-line verses, 2-line pre-choruses, a plain repeatable chorus, natural rhyme, and optional performance descriptors; avoids wordy prose. |
| V4 | Groove narrative | `Use $suno-songwriter to write a neo-soul song about riding the same bus route every day and noticing everyone's lives.` | Allows longer rhythmic verses, scene-by-scene couplets, vocalist labels, environmental/arrangement tags, spoken bridge/outro, and a simple chanted chorus. |
| V5 | Genre fusion | `Use $suno-songwriter to write a song that mixes mariachi and synthwave about driving home at dawn.` | One hybrid Style line with anchor + accent roles (not a 50/50 tag pile), BPM owned by one genre, Excluded Styles blocks the generic middle, fusion-aware slider note. |
| V6 | Multi-genre versions | `Use $suno-songwriter to write a breakup song, then give it to me as both a folk ballad and a UK garage track.` | Same title/lyric core with per-version Style, Excluded Styles, and sliders; singability re-checked per tempo; changes between versions stated. |
| I1 | Instrumental OST | `Use $suno-songwriter to create cinematic trailer music for a space rescue.` | Uses `Instrumental Prompt` and `Arrangement`, no `Lyrics`, no `Style`, no `Excluded Styles`, no sliders; cue arc and motif are clear. |
| I2 | Lofi loop | `Use $suno-songwriter for a no-vocal lofi study beat with rain, Rhodes, and soft drums.` | Loopable arrangement, instrumental prompt says no lead vocals, no Style/Excluded Styles/sliders, no lyric checks. |
| M1 | Multilingual original | `Use $suno-songwriter to write a Japanese hyperpop chorus about surviving a terrible night. Native script.` | Japanese lyrics, language notes, compact phrasing, style suited to request. |
| M2 | Singable adaptation | `Use $suno-songwriter to adapt this English hook into Mexican Spanish, keep the feeling not the exact words: I keep running toward the morning.` | Singable adaptation, not literal translation, dialect notes, no accidental English drift. |
| C1 | Controls only | `Use $suno-songwriter to improve my Suno prompt: sad song, piano. I don't want country or EDM.` | Returns improved Style, Excluded Styles, slider suggestions; may not generate lyrics. |
| R1 | Reference lyrics transformation | `Use $suno-songwriter to write a new song inspired by these lyrics: <paste known/reference lyrics>. Change the story to protecting a child.` | Extracts theme, writes new title/hook/images, avoids close phrasing reuse. |
| S1 | Style selection | `Use $suno-songwriter to write a song about winning a street race, no genre specified.` | Chooses or offers a fitting lane; labels assumptions; avoids repeated default palette. |
| ST1 | Structure | `Use $suno-songwriter to turn this loose idea into an ABABCB pop-rock structure with a bridge twist.` | Uses song-structure reference behavior; sections fit ABABCB and bridge changes meaning. |
| MT1 | Meta-tags | `Use $suno-songwriter for a classic rock song with a guitar solo after the second chorus, and make sure Suno doesn't tack on extra verses.` | Lyrics include `[Guitar Solo]` on its own line and `[End]` after the last section; notes mention them. |
| AR1 | Artist reference | `Use $suno-songwriter to make a track that sounds like Drake.` | No artist name in `Style:`; rewritten to era/scene/production (e.g. early-2010s Toronto melodic rap, nocturnal R&B); brief note on why. |
| SD1 | Section descriptors | `Use $suno-songwriter for an indie song with whispered verses and a huge explosive chorus.` | Uses descriptors in section tags (`[Whispered Verse]`, `[Explosive Chorus]`), not just adjectives crammed into `Style:`. |
| IT1 | Iteration | `Use $suno-songwriter - how do I fix one weak verse in a Suno track I otherwise like?` | Recommends Replace Section / Edit over re-rolling; may mention keeping syllable count close; references studio workflow. |
| GP1 | Genre palette | `Use $suno-songwriter to write a UK garage track about a missed last train.` | Style line uses UK-garage-appropriate BPM (~130-138), shuffled drums, sub bass, vocal chops; not a generic dance prompt. |
| SC1 | Anime OP | `Use $suno-songwriter to write an anime opening for a shounen action series, TV-size.` | Vocal song; fast anthemic J-rock/J-pop style; instrumental riff intro; hook lands early; `Suno v5.5 Notes:` states the ~90s cut and uses `[End]`; Japanese (or labeled) vocals. |
| SC2 | TV theme | `Use $suno-songwriter for a 45-second sitcom theme song, warm and hooky.` | Short hook-first structure, minimal build, button ending; vocal song or sting clearly chosen; length stated. |
| K1 | Korean lane (not K-pop) | `Use $suno-songwriter to write a Korean ballad about a long-distance goodbye.` | Korean ballad palette (slow, piano/strings, big emotive chorus), Korean lyrics, language notes; does not default to K-pop dance structure. |
| RX1 | Lyric remix | `Use $suno-songwriter to remix my lyrics into a drill track, keep the premise, change everything else: <user's own lyrics>.` | States kept-vs-changed in one line; rewrites to drill (BPM, structure, density); new lines/images; `Remix Notes:`; does not preserve original phrasing. |
| SM1 | Style match | `Use $suno-songwriter to write original rap lyrics in the cadence and style of Mos Def - don't use his actual lyrics.` | Builds a style fingerprint (dense internal rhyme, conscious themes, jazz-inflected sonic lane); writes original lines on a fresh subject; no artist name in `Style:`; `Style Reference:` line states what was modeled and that lyrics are original; refuses/avoids quoting real lyrics. |
| SM2 | Lyric-style analysis | `Use $suno-songwriter to analyze the cadence and style of these lyrics: <paste user's lyrics>.` | Returns a structured fingerprint (cadence / rhyme / line shape / diction / themes / sonic lane); does not quote long source spans back; offers to write original lyrics matching it. |
| PR1 | Persona (custom) | `Use $suno-songwriter to create a persona: a weary low-baritone outlaw-country singer; I'll call him <name>.` | Writes `personas/<slug>.md` with the documented schema; vocals/cadence/lyrical fingerprint/sonic palette are concrete; reports the path; doesn't overwrite an existing file without asking. |
| PR2 | Persona (style-reference) | `Use $suno-songwriter to make a reusable persona based on the vocal style and cadence of <artist>, named <name> - no name used in prompts.` | Decodes a style fingerprint; persona file's operational sections and any prompt contain no real artist name; fictional user-approved name; file written. |
| PR3 | Use persona | `Use $suno-songwriter to write a heartbreak song as <persona>.` | Reads `personas/<slug>.md`; `Style:` built from the persona kernel + the song's specifics; vocals/cadence/fingerprint consistent; `Persona:` line + persona checks; appends to the Song Log. |
| AL1 | Album plan | `Use $suno-songwriter to plan a 9-track dream-pop album about leaving a hometown, tied to my persona <name>.` | Reads the persona file; writes `albums/<slug>.md` with concept, shared palette, cohesion rules (constant vs variable), recurring elements, and a roled tracklist with an energy curve. |
| AL2 | Album track | `Use $suno-songwriter to write track 3 of <album>.` | Reads `albums/<slug>.md` (+ linked persona); fills the track's slot; honors cohesion rules and recurring elements; updates the tracklist row and changelog; `Album:` line + album checks. |
| SN1 | Suno Sounds | `Use $suno-songwriter to make a 5-second cinematic whoosh sound effect and a deep 808 kick one-shot.` | Returns `Sound:` / `Type:` / `BPM` / `Key` / `Variations` blocks (not Title/Style/Lyrics); specific recognizable vocabulary; `One Shot` type; duration stated; does not try to write a song. |
| CV1 | Cover art | `Use $suno-songwriter to make a cover image and an animated cover for my dusty boom-bap track about an empty laundromat at 3am.` | Returns `Cover Concept:` / `Image Prompt:` / `Motion Prompt:` / `Settings:` (not the song contract); image prompt names a medium/style, palette, lighting, composition; no text/logos/real names; composed 1:1; motion prompt is motion-only and loops; visual lane matches the song; recommends a path (text-to-image then Animate). |
| CV2 | Cover for a song package | `Use $suno-songwriter to write a synthpop song about a night drive and also give me a cover.` | Full song package, then an appended `Cover Art:` block with `Image Prompt:` / `Motion Prompt:` / `Settings:`; visual matches the song's era/mood; song contract not replaced. |

## Should-Trigger Queries

These should trigger the skill:

```json
[
  {
    "query": "write me a Suno v5.5 song about trying not to become bitter after a breakup",
    "should_trigger": true
  },
  {
    "query": "make this work in Suno: upbeat Japanese dance track, fast, anxious but hopeful",
    "should_trigger": true
  },
  {
    "query": "create a no vocals lofi beat prompt for studying at 2am",
    "should_trigger": true
  },
  {
    "query": "I need Excluded Styles and Weirdness settings for a cinematic pop song",
    "should_trigger": true
  },
  {
    "query": "rewrite this chorus using the rule of 3",
    "should_trigger": true
  },
  {
    "query": "adapt this hook into Brazilian Portuguese so it sings naturally",
    "should_trigger": true
  },
  {
    "query": "how do I stop Suno from adding extra verses to my song",
    "should_trigger": true
  },
  {
    "query": "make me a track that sounds like a 90s boom bap classic",
    "should_trigger": true
  },
  {
    "query": "write me an anime opening theme, energetic and fast",
    "should_trigger": true
  },
  {
    "query": "write original lyrics in the style of Mos Def, don't copy his songs",
    "should_trigger": true
  },
  {
    "query": "remix these lyrics into a country ballad",
    "should_trigger": true
  },
  {
    "query": "write a Korean ballad about missing someone",
    "should_trigger": true
  },
  {
    "query": "create an artist persona for my project so all my songs sound like the same singer",
    "should_trigger": true
  },
  {
    "query": "plan a cohesive concept EP about insomnia",
    "should_trigger": true
  },
  {
    "query": "make me a reusable singer persona based on the vocal style of <artist>, no name used",
    "should_trigger": true
  },
  {
    "query": "generate a sci-fi teleport sound effect, about 3 seconds",
    "should_trigger": true
  },
  {
    "query": "make a drum loop at 90 bpm in A minor",
    "should_trigger": true
  },
  {
    "query": "generate cover art for my song",
    "should_trigger": true
  },
  {
    "query": "make an animated looping cover video for this track",
    "should_trigger": true
  }
]
```

## Should-Not-Trigger Queries

These should not trigger the skill unless the broader task also asks for AI song prompting or lyric work:

```json
[
  {
    "query": "what is the circle of fifths",
    "should_trigger": false
  },
  {
    "query": "how do I EQ muddy vocals in Logic Pro",
    "should_trigger": false
  },
  {
    "query": "who wrote the song Yesterday",
    "should_trigger": false
  },
  {
    "query": "explain the licensing rules for releasing cover songs",
    "should_trigger": false
  },
  {
    "query": "make a shell script that renames mp3 files by date",
    "should_trigger": false
  },
  {
    "query": "analyze this Spotify chart data",
    "should_trigger": false
  }
]
```

## Regression Checks

Use these after changing the skill:

- Does a pasted lyric reference get transformed rather than copied?
- Does an instrumental prompt return `Instrumental Prompt` and `Arrangement`, with no `Style`, `Excluded Styles`, or sliders?
- Does a multilingual request include `Language Notes`?
- Does `Excluded Styles` avoid contradicting `Style`?
- Does style selection avoid repeatedly defaulting to the same genre/palette?
- Do slider ranges match the intended risk level?
- Does an artist-name request get rewritten to era/scene/production instead of passed through to `Style:`?
- Does a "Suno keeps adding verses" concern produce an `[End]` tag rather than only prose advice?
- Are section-tag descriptors used where the energy actually shifts, not stacked on every section?
- Does a "fix one section" request recommend Replace Section over a full re-roll?
- Does a style-match request produce original lyrics (no reproduced/close-paraphrased source lines) with a `Style Reference:` line and no artist name in `Style:`?
- Does a "Korean song" request avoid auto-defaulting to K-pop when the brief implies ballad, hip hop, or indie?
- Does a screen-tied request route output correctly (anime OP/ED, end-credit song = `Lyrics:`; trailer cut, ident, atmospheric main title = `Instrumental Prompt:` + `Arrangement:`) and state the edit length?
- Does a persona/album request write a spec file to `personas/<slug>.md` / `albums/<slug>.md` using the documented schema, and refuse to overwrite an existing one without confirmation?
- Does a style-reference persona keep the real artist name out of the spec's operational sections and out of every prompt?
- Does a song generated "as <persona>" or "track N of <album>" load the spec, stay consistent (vocals, cadence, fingerprint, palette, cohesion rules), and update the Song Log / tracklist?
- Does a sound-effect / sample request return the Suno Sounds output shape (`Sound`/`Type`/`BPM`/`Key`/`Variations`) instead of the song contract, and route a short *piece of music* to instrumental instead?
- Does a cover-art request return `Cover Concept`/`Image Prompt`/`Motion Prompt`/`Settings` (or an appended `Cover Art:` block), keep text/logos/real names out of the image prompt, compose for 1:1, write motion-only loop prompts, and avoid AI-art clichés, and does a "full music video" ask get pointed to an external editor rather than promised from Suno?
- Does the response load only relevant reference behavior rather than all guidance?

## Output Quality Rubric

Score each from 0-2:

- Trigger fit: skill invoked only when appropriate.
- Field separation: vocal Style/Excluded Styles/Lyrics are clean; instrumental prompt/arrangement are clean.
- Musical specificity: genre, tempo, instruments, and production are clear.
- Song craft: hook, structure, and section jobs are coherent.
- Reference handling: copied lyrics are transformed, not reused closely.
- Suno usability: output is ready to paste into the target Suno mode.
- Constraint handling: language, no-vocal, exclusions, and sliders match the request and mode.

Suggested pass threshold: 10/14 for rough smoke tests, 12/14 for release confidence.
