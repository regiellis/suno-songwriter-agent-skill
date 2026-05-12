# Skill Evals And Smoke Tests

Use this reference to manually test whether the skill behaves correctly across common task types. These are harness-agnostic smoke tests, not a replacement for automated trigger evaluation.

## How To Use

For each test:

1. Run the prompt through an agent with this skill available.
2. Check whether the skill triggers.
3. Check whether the response uses the expected output shape.
4. Check whether the relevant reference behavior appears.
5. Record pass/fail notes and any regression.

If a harness supports trigger logs, confirm that `suno-lyrics` was loaded for should-trigger cases and not loaded for should-not-trigger cases.

## Core Output Contract Checks

Vocal outputs should usually include:
- `Title`
- `Style`
- `Excluded Styles`
- `Lyrics`
- `Suno v5.5 Notes` when useful
- `Slider Suggestions` when Suno settings are requested or a full package is implied
- `Checks`

Instrumental outputs should use:
- `Title`
- `Style`
- `Excluded Styles`
- `Arrangement`
- `Slider Suggestions`
- instrumental checks, not lyric checks

Multilingual outputs should include:
- `Language Notes`
- target language/dialect/script decisions
- singable adaptation choices when translating

## Smoke Test Matrix

| ID | Task Type | Prompt | Expected Behavior |
| --- | --- | --- | --- |
| V1 | Vocal song | `Use $suno-lyrics to write a modern country song about a father driving through the night to pick up his kid. Male vocal, hopeful but tired.` | Produces lyrics, country-appropriate style, no hard-coded alt-R&B defaults, concrete details, checks. |
| V2 | Hook rewrite | `Use $suno-lyrics to make this chorus more memorable: I miss you every day / I wish you would stay / I feel so far away.` | Focuses on hook, likely uses Rule of 3 or 80/20, does not overbuild full song unless asked. |
| I1 | Instrumental OST | `Use $suno-lyrics to create cinematic trailer music for a space rescue.` | Uses `Arrangement`, no `Lyrics`, includes no-vocal style/exclusions, cue arc, motif, sliders. |
| I2 | Lofi loop | `Use $suno-lyrics for a no-vocal lofi study beat with rain, Rhodes, and soft drums.` | Loopable arrangement, no vocals, chillhop style, no lyric checks. |
| M1 | Multilingual original | `Use $suno-lyrics to write a Japanese hyperpop chorus about surviving a terrible night. Native script.` | Japanese lyrics, language notes, compact phrasing, style suited to request. |
| M2 | Singable adaptation | `Use $suno-lyrics to adapt this English hook into Mexican Spanish, keep the feeling not the exact words: I keep running toward the morning.` | Singable adaptation, not literal translation, dialect notes, no accidental English drift. |
| C1 | Controls only | `Use $suno-lyrics to improve my Suno prompt: sad song, piano. I don't want country or EDM.` | Returns improved Style, Excluded Styles, slider suggestions; may not generate lyrics. |
| R1 | Reference lyrics transformation | `Use $suno-lyrics to write a new song inspired by these lyrics: <paste known/reference lyrics>. Change the story to protecting a child.` | Extracts theme, writes new title/hook/images, avoids close phrasing reuse. |
| S1 | Style selection | `Use $suno-lyrics to write a song about winning a street race, no genre specified.` | Chooses or offers a fitting lane; labels assumptions; avoids repeated default palette. |
| ST1 | Structure | `Use $suno-lyrics to turn this loose idea into an ABABCB pop-rock structure with a bridge twist.` | Uses song-structure reference behavior; sections fit ABABCB and bridge changes meaning. |

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
    "query": "I need Excluded Styles and Weirdness settings for a cinematic trailer cue",
    "should_trigger": true
  },
  {
    "query": "rewrite this chorus using the rule of 3",
    "should_trigger": true
  },
  {
    "query": "adapt this hook into Brazilian Portuguese so it sings naturally",
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
- Does an instrumental prompt return `Arrangement` instead of `Lyrics`?
- Does a multilingual request include `Language Notes`?
- Does `Excluded Styles` avoid contradicting `Style`?
- Does style selection avoid repeatedly defaulting to the same genre/palette?
- Do slider ranges match the intended risk level?
- Does the response load only relevant reference behavior rather than all guidance?

## Output Quality Rubric

Score each from 0-2:

- Trigger fit: skill invoked only when appropriate.
- Field separation: Style, Excluded Styles, Lyrics/Arrangement are clean.
- Musical specificity: genre, tempo, instruments, and production are clear.
- Song craft: hook, structure, and section jobs are coherent.
- Reference handling: copied lyrics are transformed, not reused closely.
- Suno usability: output is ready to paste into Custom Mode.
- Constraint handling: language, no-vocal, exclusions, and sliders match the request.

Suggested pass threshold: 10/14 for rough smoke tests, 12/14 for release confidence.
