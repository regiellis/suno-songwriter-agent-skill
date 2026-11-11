# Cleanup Evaluation Record

Date: 2026-09-05. Evaluator: Codex, in the editing session. These are generated text samples and self-reviewed results against `references/evals.md`, not an independent forward test. Fresh-session skill selection, trigger logs, Suno generation, pronunciation, mixes, and loop playback were not tested. No paid generations were made.

## MX1: Ninety-Second Matrix Only

Prompt: Plan a 90-second indie-pop song at 120 BPM in 4/4 about leaving a shared apartment. Matrix only, no lyrics.

Candidate output:

| Section | Bars | Job | Hook / Phrase | Arrangement |
| --- | --- | --- | --- | --- |
| Intro | 4 | Empty room, move-out morning | Establish guitar motif | Guitar and room tone |
| Verse 1 | 8 | Divide the familiar objects | Short observations | Add bass and restrained drums |
| Chorus | 8 | Admit what cannot be packed | Repeated title idea: The Things We Leave | Open rhythm and backing response |
| Verse 2 | 8 | One object changes the decision | New action, same phrase rhythm | Reduce guitar; keep pulse |
| Final chorus | 12 | Accept the departure | Return the hook with a changed final thought | Full band, then thin to motif |
| Outro | 4 | Close the door | Motif return | Short resolved ending |

44 bars × 4 × 60 / 120 = 88 seconds, leaving roughly two seconds for the tail. This budgets the draft; check and edit generated audio for an exact 90-second delivery.

Result: pass for plan-only scope, arithmetic, section development, and qualified timing.

## MX2: Compound Meter

Prompt: Budget a 30-second cue in 6/8 at dotted-quarter 60 BPM.

Candidate output: A bar contains two dotted-quarter beats, so each bar takes two seconds. Fifteen bars fill 30 seconds before tails. Plan 2 bars of introduction, 4 of motif, 4 of development, 4 of return, and 1 of resolution. If the tail must fit inside 30 seconds, shorten the final gesture or leave its last beat empty and check the rendered result.

Result: pass for pulse unit, bar count, and tail qualification.

## IC1: Custom Instrumental Controls

Prompt: My Suno Custom screen has Instrumental, Styles, Exclude, Weirdness, and Style Influence. Give settings for a no-voice 120 BPM game loop.

Candidate output:

```text
Title: Clockwork Courtyard
Instrumental: On
Style: 120 BPM clockwork game cue, plucked marimba motif, muted synth bass, dry ticking percussion, restrained dynamics, repeating harmonic cycle
Excluded Styles: vocals, choir, chants, vocal chops
Slider Suggestions:
- Weirdness: 20-35%
- Style Influence: 75-90%
Arrangement:
- 8 bars: introduce the marimba motif over bass and ticking percussion.
- 8 bars: vary the response, then return to the opening harmony and texture.
Notes:
- Settings are starting ranges, not official presets.
- Arrangement is a planning map; summarize its essentials in Styles.
- At steady 120 BPM in 4/4, 16 bars budget 32 seconds. Audition and edit the loop boundary, including reverb tails; the prompt cannot guarantee a clean loop.
```

Result: pass for honoring visible controls, no-voice constraints, field mapping, and listening limits. Rendered loop quality untested.

## AI1: Uploaded Demo

Prompt: I uploaded my guitar demo. Keep its melody but change the drums. How should I iterate?

Candidate output: Keep the uploaded clip and model fixed. Describe only the new drum groove and retain the melody direction. If Audio Influence is exposed, start with its current value; compare a modest increase only if the melody drifts. Listen for melody retention and drum change separately. If the performance is otherwise right, edit the drum layer in Studio or work from stems instead of regenerating the whole track. Stop after a baseline comparison and one targeted change to reassess; no setting guarantees exact melody preservation.

Result: pass for reference preservation, conditional Audio Influence, controlled comparison, and bounded iteration.

## LP1: Detailed Style Prompt

Prompt: Write a detailed Style prompt for a folk-to-drum-and-bass switch. My field allows 1,000 characters.

Candidate output:

```text
Begin with close fingerpicked acoustic guitar and a restrained lead vocal, intimate folk phrasing over a quiet 87 BPM pulse. At the chorus, shift to 174 BPM drum-and-bass with tight breaks and a rounded sub, retaining the guitar motif and singer. Keep the chorus hook spacious against the faster percussion. Drop back to the intimate texture for the next verse, then restore the breaks for the final hook. Dry, clear vocal; percussion supplies the lift without burying the acoustic attack.
```

Result: pass for exceeding the compact default when useful while fitting the user-supplied counter, specifying the transition, and retaining musical constants. This is a prompt, not proof that the switch renders correctly.

## EN1: Exact Ending

Prompt: Can [End] guarantee this theme stops at exactly 45 seconds?

Candidate output: No. `[End]` requests closure. Budget the theme for 45 seconds, use Duration if available, then listen and trim or edit to the exact cut. Leave space for the final note and its decay.

Result: pass for avoiding an ending guarantee and providing a practical next step.

## FM1: Strophic Form

Prompt: Write a three-stanza folk lyric with a repeated last line, no chorus or bridge.

Candidate output:

```text
[Verse 1]
The kitchen chair still holds your coat
I sweep around the shoes below
I leave the latch where you would know

[Verse 2]
The frost has split the garden pail
I bring the last tomatoes in
I leave the latch where you would know

[Verse 3]
Your postcard leans against the clock
I read it once and let you go
I leave the latch where you would know
```

Result: pass for three stanzas, exact refrain, stable speaker, concrete detail, and no imposed chorus, bridge, or four-line rule. The refrain's unresolved attachment is deliberate; singability is text-reviewed only.

## SR1: Bland Take And Moderation

Prompt: Suno made one bland take. Does that prove my lyrics were secretly filtered?

Candidate output: No. A bland take alone does not establish moderation. Check for an actual error or warning, then review whether the prompt gives a defining groove, sound, or arrangement change. Compare one specific revision while holding other settings fixed.

Result: pass for evidence-based diagnosis.

## Remaining Validation

Run these prompts in a fresh skill-enabled harness and retain full responses before claiming independent behavioral coverage. Run should-trigger and should-not-trigger cases with selection logs when the harness supports them. Generate and listen to representative vocal, instrumental, and multilingual outputs before making audio-quality claims.

## Web Documentation Checks

The updated static site was checked in headless Chrome at 1440 × 1100 desktop and 390 × 844 mobile viewports. All 19 routes displayed their intended page without document-level horizontal overflow. The mobile menu opened and closed on navigation. All reference-index targets matched source files, and the page script passed a JavaScript syntax check. Desktop matrix and mobile cover-art screenshots were visually inspected. These checks used local files; they do not establish public deployment status.

## PO1-PO4: Field Hygiene, Reviewed Against Prior Skill Output

Date: 2026-09-13. Evaluator: Claude, in the editing session. Two song packages generated by the previous skill version were supplied by the repository owner and reviewed against the rules in `SKILL.md`. Self-reviewed text only. No audio was generated, and nothing here was tested by listening.

Sample 1 (vocal song, art-rock and folktronica, English with a French bridge):

- `Style` ended with an inline `exclude:` list, so five intended exclusions read as positive prompt text. `SKILL.md` already required negative direction to sit in `Excluded Styles`.
- `Style` contained a stray `trap` token contradicting the rest of the brief and the exclusions.
- The bridge read `(vocal chop, rhythmic): "I don't drown, I don't drown"`, placing production direction inside the parentheses and the sung words outside. `SKILL.md` already required parentheses to hold only sung words.
- No `Title`, no section tags, no `Language Notes` for the French bridge, and the final sung line had no section after it.

Sample 2 (same `Style` and `Excluded Styles`, new lyric, refrain form, no chorus):

- Section tags were present and detailed, so the missing tags in sample 1 are variance rather than a systematic fault.
- The reused `Style` still promised a spoken French bridge over chopped vocal ad-lib, massed choral layers, and a key lift. The new lyric contains no French, no bridge, and no key change.
- Seven of nine section tags used an en-dash and two used a plain hyphen, mixed within one output. The voice spec requires a plain hyphen in taught tag syntax.
- Lyric craft passed: refrain returns three times with the meaning changing on each pass, detail is concrete, point of view and tense are deliberate.

Finding: the craft guidance held in both samples; the failures were all field hygiene, and every one occurred after the drafting rules had been applied. Two of the three rule violations were already stated in `SKILL.md`, so more drafting prose was not the fix. Added a `Pre-Output Check` that reads the finished fields against each other, and regression cases `PO1`-`PO4`.

Limits: two samples, one reused `Style` line, one skill version, one evaluator, no forward test in a fresh session and no generated audio. The inline `exclude:` fault is a single observation, not a measured rate.

## Music Guidance Site Update

Date: 2026-09-24. Local headless Chrome checks covered all 23 routes at 1440 x 1100 and 390 x 844. Each route displayed one intended page without document-level horizontal overflow; the mobile menu opened and closed on navigation. All 30 source-reference links mapped to local files, both download links resolved to the packaged ZIP, and no page script errors occurred. Rhythm and arrangement screenshots were visually reviewed at both sizes after disabling transition animations for capture.

The site now includes harmony and melody, rhythm and arrangement, and production direction pages. Controls locate Variety in the Advanced tab using the user's UI confirmation. Output and validation guidance cover the whole-response punctuation rule. These checks verify local documentation and navigation, not public deployment or generated audio.

## Songwriting And Fusion Self-Review

Date: 2026-09-24. The following are candidate text outputs written and reviewed in the editing session. They are not independent agent evaluations or Suno listening tests. The larger regression matrix remains a set of cases to run, not a recorded pass count.

### GW1: Strophic Story With Unchanged Refrain

Prompt: Write three folk stanzas about inheriting a father's tools, with an unchanged final-line refrain and no chorus.

Candidate:

```text
[Verse 1]
The hammer hung beside his coat
I swept beneath it every spring
I leave them where he laid them down

[Verse 2]
Next door, her broken porch step sagged
I said those tools were all I had
I leave them where he laid them down

[Verse 3]
Today she crossed the boards I fixed
I brushed the sawdust from his bench
I leave them where he laid them down
```

Text review: three stanzas, the exact refrain persists, and the narrator moves from preserving objects to using them for another person. No added chorus or bridge. Loose rhyme is intentional. Melodic fit and breathing remain untested.

### GF1: Folk And Drum And Bass

Prompt: Plan a folk/drum-and-bass blend at 174 BPM with relaxed vocals. No lyrics.

Candidate:

| Part | Role |
| --- | --- |
| Drums and sub | Establish the 174 BPM breakbeat grid and recurring bass foundation |
| Voice | Conversational story phrases at an 87 BPM feel, with rests after important lines |
| Guitar | Answer the voice in its gaps; retain the same figure at section boundaries |
| Refrain | Return to one title phrase whose meaning changes after the second verse |
| Middle passage | Reduce guitar and drum density while retaining the pulse |
| Final return | Restore the drum activity beneath the familiar refrain |

The two tempo readings describe layers of the same grid, not a required tempo switch. Audition whether the words remain relaxed.

Text review: no lyrics invented, no BPM averaging, contributions include phrase language and form as well as timbre, and the no-audio limit is explicit.

### GF3: Compound To Simple Meter

Prompt: Plan a transition from 6/8 at dotted-quarter 72 into 4/4 house, keeping the hook.

Candidate: Keep the pulse duration constant at the transition: the old dotted-quarter beat becomes the new quarter-note beat at 72 BPM. Let the last 6/8 phrase finish, sustain one compatible tone across the boundary, and introduce the new drum grouping on the next downbeat. Rephrase the hook from triplet-based subdivisions into the intended 4/4 placement. This produces an unusually slow house interpretation. If a faster dance tempo is wanted, choose that new tempo explicitly and plan the handoff rather than claiming both goals happen automatically. Preserve the hook's words and recognizable contour where feasible; verify the audio fit.

Text review: pulse mapping is explicit, it exposes the tempo tradeoff, and it does not promise that identical melodic timing fits both meters. The proposed sustained tone still requires harmonic compatibility and listening.

### GW4: Techno Without A Big Drop

Prompt: Plan a strictly voiceless hypnotic techno track, no big drop.

Candidate:

```text
Title: Narrow Passage
Instrumental Prompt: hypnotic techno, steady kick and restrained bass,
interlocking clipped synth cells, gradual percussion changes,
small timbral shifts over a continuous pulse
Arrangement:
- Establish one synth cell over the kick and bass.
- Add a second answering cell while keeping the first recognizable.
- Remove one percussion part; vary the answer's register.
- Return to the initial balance, then reduce to the pulse for the exit.
```

Use Instrumental on the available surface and exclude voices, chants, choir, and vocal chops where Exclude is exposed. No build/drop climax is requested.

Text review: instrumental fields, recurring material, deliberate gradual development, and no forced pop form. No claim that the generated track is voiceless without audition.

### Scope Of This Pass

The audit replaced a compact-pop default with form-aware writing guidance, added five genre families, and rewrote fusion around musical roles. It does not establish equal expertise across every named tradition. Specialist rhythmic, linguistic, modal, and cultural details still require the source and reference checks described in the genre router.

### Website Verification After Genre Expansion

Local headless Chrome verified all 24 routes at 1440 x 1100 and 390 x 844, with one intended page visible per route, no document-level horizontal overflow, and no page script errors. The mobile menu opened and closed on navigation. All 44 source-reference link occurrences mapped to files, and both download links resolved to the ZIP. The Writing by Genre desktop screenshot was visually reviewed. Skill validation, reference routing, dash scans, YAML parsing, repository context lint, whitespace checks, and ZIP/source comparison passed. The prose detector's semicolon-cadence finding is explicitly allowed by the voice spec; historical changelog wording was not rewritten for unrelated detector findings.

The public site was not deployed in this pass. No audio was generated or heard.
