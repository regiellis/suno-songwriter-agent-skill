# Skill Evals And Smoke Tests

Use this reference to manually test whether the skill behaves correctly across common task types. These are harness-agnostic smoke tests, not a replacement for automated trigger evaluation.

## Structured Songwriting Benchmark

The source repository includes `evals/songwriting/cases.json`, `rubric.json`, and `README.md`: 16 self-contained cases covering lyric revision, non-pop forms, genre identity, multi-style fusion, transitions, and evidence discipline. All supplied drafts are synthetic originals. The protocol separates generation from blind judging and reports constraint failures separately from musical-quality scores.

These development assets are outside the installable skill ZIP. See the [benchmark protocol](https://github.com/regiellis/suno-songwriter-agent-skill/tree/main/evals/songwriting) for the dataset, rubric, run procedure, and limitations. Authored cases are not completed evaluations; collect raw responses and judgments before claiming behavioral results.

## How To Use

For each test:

1. Run the prompt through an agent with this skill available.
2. Check whether the skill triggers.
3. Check whether the response uses the expected output shape.
4. Check whether the relevant reference behavior appears.
5. Record pass/fail notes and any regression.

If a harness supports trigger logs, confirm that `suno-songwriter` was loaded for should-trigger cases and not loaded for should-not-trigger cases.

## Core Output Contract Checks

All outputs, including surrounding prose and code blocks, must contain neither U+2014 nor U+2013. Check character values, not just section-tag formatting.

Vocal outputs should usually include:
- `Title`
- `Style`
- `Excluded Styles`
- `Lyrics`
- `Suno v6 Notes` when useful
- `Slider Suggestions` when Suno settings are requested or a full package is implied
- `Checks` when useful or requested

For chorus-based forms, vocal lyrics should pass the lyric quality gate; adapt it for forms without a chorus:
- title or hook phrase appears in or near the chorus
- hook is recognizable through wording, rhythm, contour, or placement; lower chorus density is an option, not a requirement
- natural stress, phrase duration, and breath space suit the chosen delivery
- end rhyme or vowel rhyme supports the flow unless the genre asks otherwise
- performance descriptors are used in section tags when they improve delivery
- point of view and tense are stable unless a shift is deliberate
- at least one purposeful concrete detail appears where it serves the song
- no obvious overlong mouthful lines

Instrumental outputs should use:
- `Title`
- `Instrumental Prompt`
- `Arrangement`
- portable labels by default; map the prompt to Styles and add available Exclude/sliders when Advanced settings are requested
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
| V3 | Suno-native flow | `Use $suno-songwriter to write an R&B song about leaving for Japan after a breakup and finding love for the country and a person.` | Fits the chosen R&B phrasing, maps the narrative turn, and leaves vocal space; line counts and pre-chorus are optional. |
| V4 | Groove narrative | `Use $suno-songwriter to write a neo-soul song about riding the same bus route every day and noticing everyone's lives.` | Allows longer rhythmic verses, scene-by-scene couplets, vocalist labels, environmental/arrangement tags, spoken bridge/outro, and a simple chanted chorus. |
| V5 | Genre fusion | `Use $suno-songwriter to write a song that mixes mariachi and synthwave about driving home at dawn.` | One hybrid Style line with clear rhythmic and textural roles; respects a requested balanced hybrid; any slider range is a heuristic. |
| V6 | Multi-genre versions | `Use $suno-songwriter to write a breakup song, then give it to me as both a folk ballad and a UK garage track.` | Same requested title/lyric core with per-version Style and relevant exclusions; sliders only if useful; singability re-checked per tempo; changes between versions stated. |
| I1 | Instrumental OST | `Use $suno-songwriter to create cinematic trailer music for a space rescue.` | Uses `Instrumental Prompt` and `Arrangement`, no invented sung words; portable package by default, cue arc and motif are clear; no claim of unavailable Custom controls. |
| I2 | Lofi loop | `Use $suno-songwriter for a no-vocal lofi study beat with rain, Rhodes, and soft drums.` | Loopable arrangement, Instrumental mapping and exclusions honor no vocals, including chops and choir, no unsolicited controls or lyric checks; loop boundary requires listening. |
| M1 | Multilingual original | `Use $suno-songwriter to write a Japanese hyperpop chorus about surviving a terrible night. Native script.` | Japanese lyrics, language notes, compact phrasing, style suited to request. |
| M2 | Singable adaptation | `Use $suno-songwriter to adapt this English hook into Mexican Spanish, keep the feeling not the exact words: I keep running toward the morning.` | Singable adaptation, not literal translation, dialect notes, no accidental English drift. |
| C1 | Controls only | `Use $suno-songwriter to improve my Suno prompt: sad song, piano. I don't want country or EDM.` | Returns improved Style, Excluded Styles, slider suggestions; may not generate lyrics. |
| R1 | Reference lyrics transformation | `Use $suno-songwriter to write a new song inspired by these lyrics: <paste known/reference lyrics>. Change the story to protecting a child.` | Extracts theme, writes new title/hook/images, avoids close phrasing reuse. |
| S1 | Style selection | `Use $suno-songwriter to write a song about winning a street race, no genre specified.` | Chooses or offers a fitting lane; labels assumptions; avoids repeated default palette. |
| ST1 | Structure | `Use $suno-songwriter to turn this loose idea into an ABABCB pop-rock structure with a bridge twist.` | Uses song-structure reference behavior; sections fit ABABCB and bridge changes meaning. |
| MT1 | Meta-tags | `Use $suno-songwriter for a classic rock song with a guitar solo after the second chorus, and make sure Suno doesn't tack on extra verses.` | Lyrics include `[Guitar Solo]` on its own line and `[End]` after the last section; notes identify these as cues, not guarantees. |
| AR1 | Artist reference | `Use $suno-songwriter to make a track that sounds like Drake.` | No artist name in `Style:`; rewritten to era/scene/production (e.g. early-2010s Toronto melodic rap, nocturnal R&B); brief note on why. |
| SD1 | Section descriptors | `Use $suno-songwriter for an indie song with whispered verses and a huge explosive chorus.` | Uses descriptors in section tags (`[Whispered Verse]`, `[Explosive Chorus]`), not just adjectives crammed into `Style:`. |
| IT1 | Iteration | `Use $suno-songwriter - how do I fix one weak verse in a Suno track I otherwise like?` | Recommends Replace Section / Edit over re-rolling; may mention keeping syllable count close; references studio workflow. |
| GP1 | Genre palette | `Use $suno-songwriter to write a UK garage track about a missed last train.` | Names a UK garage/2-step groove, bass role, and syncopated phrase behavior; vocal chops and a fixed BPM band are not mandatory. |
| SC1 | Anime OP | `Use $suno-songwriter to write an anime opening for a shounen action series, TV-size.` | Vocal song; fast anthemic J-rock/J-pop style; instrumental riff intro; hook lands early; `Suno v6 Notes:` states the ~90s cut and uses `[End]`; Japanese (or labeled) vocals. |
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

## Planning And Platform Regression Cases

| ID | Prompt | Pass Criteria |
| --- | --- | --- |
| MX1 | `Plan a 90-second indie-pop song at 120 BPM in 4/4 about leaving a shared apartment. Matrix only, no lyrics.` | About 45 bars before tails; section jobs, hook behavior, and contrast; no full lyric package or exact-render guarantee. |
| MX2 | `Budget a 30-second cue in 6/8 at dotted-quarter 60 BPM.` | Uses two dotted-quarter beats per bar: 15 bars before tails, not a six-beat/quarter-note calculation. |
| IC1 | `My Suno Advanced screen has Instrumental, Styles, Exclude, Weirdness, and Style Influence. Give settings for a no-voice 120 BPM game loop.` | Uses the exposed controls, enables Instrumental, excludes choir/chops if needed, keeps Arrangement separate, qualifies loop precision. |
| AI1 | `I uploaded my guitar demo. Keep its melody but change the drums. How should I iterate?` | Discusses Audio Influence conditionally, preserves reference and other variables, defines listening criteria; no universal exact percentage. |
| LP1 | `Write a detailed Style prompt for a folk-to-drum-and-bass switch. My field allows 1,000 characters.` | Fits the supplied limit; not constrained to a claimed 200-character maximum; relationship between sections stays clear. |
| EN1 | `Can [End] guarantee this theme stops at exactly 45 seconds?` | Says no; budgets time and recommends listening plus an exact edit. |
| FM1 | `Write a three-stanza folk lyric with a repeated last line, no chorus or bridge.` | Honors strophic form and refrain; does not impose a chorus or multiple-of-four rule. |
| SR1 | `Suno made one bland take. Does that prove my lyrics were secretly filtered?` | Does not infer moderation from bland audio; checks errors and musical specificity. |
| MD1 | `Generate this on v5.5 instead, it sounded better.` | States that v5.5 and every pre-v6 model were retired on 2026-09-09 and cannot generate new material; offers a v6 rebuild; does not pretend to select the old model. |
| MD2 | `I changed two words in my Style and the two takes came out completely different. Is the prompt broken?` | Names Variety as the likely cause, says it rewrites the style prompt and is on by default, and tells the user to set it to 0 before comparing. |
| MD3 | `Should I turn on Max Mode while I dial in this brief?` | Says no during calibration, because extra credits do not fix a prompt problem; places Max Mode after the direction is right, for consistency and fidelity. |
| MD4 | `My chorus sounds huge but the verses go empty and the mix is muddy.` | Treats these as two separate faults: states verse energy and instrument activity positively, adds a short production clause, and does not reach for sliders first. |
| MD5 | `The song cut off while the singer was still on the last line.` | Recommends an instrumental section after the final vocal section as a buffer; states that `[End]` and `[Hard Stop]` request closure and cannot enforce it, and that `[Hard Stop]` is not documented Suno syntax. |
| MD6 | `Which model should I use? I'm on the free plan.` | Routes to `v6-mini`, keeps the craft identical, and omits Pro-only controls rather than recommending settings the user cannot reach. |
| MD7 | `Can I still extend and remaster my old v5.5 tracks?` | Says yes for listen, share, Remaster, Cover, Extend, and Remix, notes each re-renders on v6 so the character can drift, and says Replace Section, Crop, and stems on a pre-v6 song are undocumented rather than guessing. |
| MD8 | `I'm on the free plan and want to try twenty variations and download the best five.` | Raises the download cap before the workflow: 7 lifetime on Free, one song per download whatever the format. Recommends auditioning inside Suno and spending downloads only on final takes. |
| MD9 | `Set up a persona so every song uses my own singing voice.` | Distinguishes the Markdown spec from Voices, Style Personas, and Custom Models; says a text file selects none of them; describes the Voice verification step and that only its creator can generate with it. |
| MD10 | `Can I attach a photo and a reference song to one generation?` | Confirms v6 accepts songs, playlists, audio, images, and video as references, says image and video inputs raise credit cost, and declines to invent a UI control name Suno has not published. |
| PO1 | Any full vocal song request | Style holds no `exclude:` list, no `no ...` phrase, no slider value, and no square brackets. Negative direction appears only in `Excluded Styles`. |
| PO2 | `Write a second song reusing the same Style line.` | Style is reconciled against the new lyric: a promised bridge, language, choir, or key change that the new lyric does not contain is removed rather than carried over. |
| PO3 | Any song with a delivery instruction beside sung backing | Production direction sits in the section tag and parentheses hold only sung words. `(vocal chop, rhythmic): "line"` is the inversion to catch. |
| PO4 | Any section-tagged lyric | Tag descriptors use a plain hyphen, never an en-dash or em-dash, consistently across every tag in the output. |
| PM1 | `What is this song saying?` with any lyric | Opens with one plain sentence naming what the song is about, then any further reading. Does not lead with symbolism, etymology, or a chain of inferences. |
| PM2 | A lyric that supports a plain and an elaborate reading | Leads with the plain reading and offers the elaborate one as a second reading, rather than presenting the construction as the meaning. |

Run these prompts in a fresh skill-enabled session for behavioral regression testing. Save actual outputs, model/harness identity, date, and criterion-level results. For selection tests, keep the should-not-trigger requests separate from explicit skill invocations. Record unavailable trigger logs and audio tests as untested, not passed.

## Should-Trigger Queries

These should trigger the skill:

```json
[
  {
    "query": "write me a Suno v6 song about trying not to become bitter after a breakup",
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

- Does an edit preserve the user's draft at the requested depth, while a new work inspired by third-party lyrics uses fresh expression?
- Does an instrumental prompt return `Instrumental Prompt` and `Arrangement`, and map to available Advanced controls when requested?
- Does a multilingual request include `Language Notes`?
- Does `Excluded Styles` avoid contradicting `Style`?
- Does style selection avoid repeatedly defaulting to the same genre/palette?
- Do slider ranges match the intended risk level?
- Does an artist-name request get rewritten to era/scene/production instead of passed through to `Style:`?
- Does a "Suno keeps adding verses" concern produce an ending cue plus an edit/listening fallback, without guaranteeing that a tag stops generation?
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
- Reference handling: user drafts are preserved at the requested edit depth; third-party inspiration yields fresh expression.
- Suno usability: output is ready to paste into the target Suno mode.
- Constraint handling: language, no-vocal, exclusions, and sliders match the request and mode.

Suggested pass threshold: 10/14 for rough smoke tests, 12/14 for release confidence.


## Musical Knowledge Regression Cases

These cases specify expected behavior; they are not recorded test results. Review generated answers against the musical decisions, not exact wording. Audio compliance remains untested until a take is heard.

| ID | Prompt | Expected Behavior |
| --- | --- | --- |
| MK1 | `Plan an eight-bar Suno soul intro in 6/8 at dotted-quarter 72. How long is it?` | Uses two dotted-quarter beats per bar, about 13.3 seconds; timing is a plan, not a rendering guarantee |
| MK2 | `Make my folk chorus lift without getting louder. Keep the lyrics.` | Preserves lyrics; proposes contour, voicing, or harmonic-rhythm contrast; avoids automatic bigger drums |
| MK3 | `Give my D-minor vamp a Dorian color for Suno.` | Identifies B natural and a compatible voicing or melodic target; does not promise a mode tag enforces pitches |
| MK4 | `My singer can manage C3-E4 but tires above C4. Plan the hook.` | Distinguishes range from tessitura; keeps repeated phrases lower and avoids sustained E4 merely because it is reachable |
| MK5 | `140 BPM half-time instrumental electro with busy hats, no voices.` | Keeps BPM and half-time backbeat distinct; returns instrumental fields; adds no choir, vocal chops, or lyrics |
| MK6 | `Keep full-band verses but make the bridge just bass and voice.` | Scopes full-band direction to verses; bridge stays sparse; no contradictory global instruction |
| MK7 | `Variety is zero and take B sounds better. Did my new Style fix it?` | Treats the observation as provisional; controls model, source, settings, personalization; acknowledges stochastic variation and makes no causal guarantee |
| MK8 | `Use v6-mini on my free account for a precise melody from text.` | Respects model choice; avoids paid-control assumptions and exact-note guarantees; offers a supported reference workflow if precision is essential |


## Output Punctuation Regression Cases

| ID | Prompt | Expected Behavior |
| --- | --- | --- |
| PUN1 | `Write a Suno folk song and explain your arrangement choices.` | No U+2014 or U+2013 anywhere in title, fields, lyrics, explanation, or code blocks |
| PUN2 | `Return my draft with wording preserved, plus section tags and a tempo range.` Supply a draft containing U+2014 and U+2013. | Preserves words while normalizing dash punctuation; tags and ranges use ASCII hyphens |
| PUN3 | `Give me settings only, with a short explanation of the tradeoffs.` | Punctuation rule applies even without lyrics; sentence breaks use suitable punctuation rather than dash substitutions |


## Songwriting Breadth And Fusion Regressions

Run these as behavioral cases with the skill available. The expected behaviors are evaluation criteria, not evidence that they have been tested. Compare actual text decisions; audio timing, groove, and pronunciation require listening.

| ID | Prompt | Expected Behavior |
| --- | --- | --- |
| GW1 | `Write a three-stanza folk story with an unchanged last-line refrain. No chorus.` | Events or consequences develop; exact refrain persists; no imposed chorus or bridge |
| GW2 | `Write a hookless boom-bap verse about a night-shift bus driver. Plan breaths but don't print counting marks.` | Cadence, internal rhyme, and scene movement; no mandatory sung hook or claim that lines equal bars |
| GW3 | `Plan a doom-metal song with clean vocals and long instrumental gaps.` | Long phrase/decay budget and riff identity; no automatic screamed verse or metalcore breakdown |
| GW4 | `Write a hypnotic instrumental techno plan without a big drop.` | Repeating cell and gradual part changes; no pop narrative, compulsory chorus, or festival climax |
| GW5 | `Plan a new 32-bar AABA vocal-jazz song.` | Four planned eight-bar sections with B contrast; title/refrain can sit inside A; no confusion with verse/chorus form |
| GW6 | `Write a theater duet: one person wants to leave, the other keeps inventing reasons to stay.` | Different objectives and changing tactics; responses affect each other instead of alternating identical feelings |
| GW7 | `Give distinct writing plans for Afrobeats, Afrobeat, and amapiano.` | Different hook/groove/development roles; no universal log-drum preset or invented language |
| GW8 | `Make a salsa-inspired section with a fixed coro and changing lead responses.` | A learnable recurring answer with room for lead variation; rhythmic relationship treated as a listening target |
| GW9 | `Plan an ambient song with deliberately ambiguous images and no narrative resolution.` | Organizes sound/image recurrence; does not force literal explanation or a plot twist |
| GW10 | `Only fix the rushed second line of my original chorus; keep the title and all other words.` | Narrow edit scope; does not replace title, hook, or unrelated lines |
| GF1 | `Blend folk storytelling and drum and bass at 174 BPM; vocals should feel relaxed.` | Shared grid, possible 87 BPM vocal feel, narrative phrasing and drum/sub roles; no BPM averaging |
| GF2 | `Blend soul, post-punk, and ambient into one song, not separate genre sections.` | Distinct vocal, groove, and texture roles; continuous blend with an identity across sections |
| GF3 | `Move from a 6/8 ballad into 4/4 house while keeping my hook.` | States pulse mapping or tempo change, transition event, and vocal rephrasing needs; no automatic fit claim |
| GF4 | `Give folk and drill versions with every lyric word unchanged.` | Exact words preserved; phrase allocation and arrangement vary; changes described without silent rewriting |
| GF5 | `I want a five-section suite that changes style at every section.` | Honors count, plans meaningful transitions and continuity; no invented two-switch maximum |
| GF6 | `My folk-house hybrid keeps losing the folk identity. What should I change?` | Diagnoses narrative/phrase or instrument role loss and suggests a targeted revision; no automatic Weirdness increase or blanket exclusions |
| GF7 | `Blend a raga-based melody with techno and guarantee the exact raga in Suno.` | Clarifies the raga/reference if needed, checks melodic constraints, assigns groove/harmony roles, rejects the guarantee while offering verification |
