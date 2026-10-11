# Studio And Iteration

Use this reference for what happens after the first generation: choosing between takes, extending, restyling, fixing a section, splitting stems, and deciding whether to edit or re-roll. This is workflow guidance to fold into `Suno v6 Notes:` when the user is iterating or preparing a production, not something to dump on every request.

## Two Clips Per Run

Suno returns two variations per generation. Treat the first run as "pick the stronger seed," not "the answer." Advise the user to keep the better take and build from it (Extend / Replace Section / Remix) rather than regenerating the whole prompt repeatedly: re-rolling from scratch throws away a take that was already 80% right.

When a prompt is close but not landing, change **one** lever at a time between runs: the prompt, or, when exposed, Weirdness, Style Influence, or Audio Influence (see `references/suno-v6-controls.md` § Troubleshooting).

Set Variety to 0 when comparing exact Style text. Suno documents that Variety can rewrite Styles; its per-model defaults are unverified. Hold the source, model, visible controls, and personalization constant. Generation remains stochastic at 0, so a better single take does not prove the prompt change caused the improvement. Compare both candidates and repeat only when the decision warrants the credit cost.

## Extend

Continues an existing track from a chosen point.

Use for:
- a take that ends too early or fades awkwardly
- adding a bridge, solo, or outro that the original didn't generate
- building a longer arrangement in stages

Tips:
- Feed the continuation only the *new* sections in the lyrics box, with section tags, so the model knows what comes next.
- Keep the Style line consistent with the original take or the seams will be obvious.
- Use `[End]` on the final extension to request closure, then listen for unwanted additions.

## Remix: Cover, Extend, Reuse, Speed

[Remix](https://help.suno.com/en/articles/6050497) is Suno's umbrella term for four workflows: Cover, Extend, Reuse, and Speed. [Cover](https://help.suno.com/en/articles/2872257) is the style-change tool, re-generating a song in a new style while keeping melody and structure, driven by a new Style line. It is still labeled Beta and still limited to Pro and Premier. There is no separate tool called Restyle; do not use that name.

Use for:
- "same song, different genre": write a fresh Style line for the target lane (see `references/genre-palettes.md`)
- turning a demo idea into a polished version
- A/B-ing two production directions for the same lyrics

Tips:
- The new Style line does the work here; keep it specific.
- Expect melody to drift somewhat on heavy genre changes; lower Weirdness if it drifts too far, and confirm Variety is at 0 before blaming the Style line.
- Max Mode is aimed at covers that must stay close to the source; suggest it here rather than during prompt calibration.

## Replace Section / Edit / Inpainting

Regenerates a selected span (a verse, a chorus, a few bars) inside an otherwise-finished track.

Use for:
- one weak verse in an otherwise good take
- fixing a mumbled or mispronounced line: rewrite that line simpler, then replace just that section
- swapping a section's energy without re-rolling the song
- removing or replacing a section the model invented

Tips:
- Keep the replacement lyrics' syllable count and line shape close to the original span so the new audio fits the surrounding bars.
- This is the fix for "everything's good except ___": reach for it before regenerating.

v6 added plain-language editing on top of these surfaces rather than as a new tool. The [v6 FAQ](https://help.suno.com/en/articles/13924481) documents editing one section by describing the change while the rest is preserved, and changing a single lyric without rebuilding the song (its example: change the lyric from `love` to `light`). Write the instruction as a plain sentence naming the section and the wanted change. Suno does not document a separate button for this, so do not name one.

## Crop / Trim

Cuts the track to a span: for grabbing a clean loop, a stinger, or removing a bad intro/outro tail. Mention when the user needs a specific length or a loop for game/video use.

## Stems

Splits a finished track into separate audio layers (commonly vocals, drums, bass, other / instrument groups).

Use for:
- handing the track to a DAW for mixing, re-arranging, or scoring to picture
- isolating an instrumental from a vocal take (or vice versa) without re-generating
- replacing one layer with live performance

Note in `Suno v6 Notes:` when stems are part of the intended workflow (e.g. `Plan: generate, pick take, split stems, mix in DAW`). Don't promise specific stem counts/quality: it varies, and Suno publishes no stem count or tier gating for the export outside Studio. [Advanced Stem Separation](https://help.suno.com/en/articles/13670529) with Split from Mix and Advanced Split lives inside Studio 2.0, which is Premier only. Stems drawn from a song count inside that song's single download, not as extra downloads.

## Remaster

Creates variations focused on sound and production while retaining the song. The [official Remaster guide](https://help.suno.com/en/articles/8105281) describes Model and Variation strength controls: Subtle, Normal, and High. Start with Subtle for a keeper whose balance or clarity needs refinement; stronger variation may change vocal or musical details. Use section editing for lyric changes. Source checked 2026-09-05.

## What Still Works On Pre-v6 Songs

Suno retired the pre-v6 models for generation, not the songs. Existing tracks stay in the library unchanged and are never modified by any of these operations.

Officially guaranteed on a song made with a retired model, per the [v6 FAQ](https://help.suno.com/en/articles/13924481) and the [Upcoming Changes FAQ](https://help.suno.com/en/articles/13614785): listen, share, Remaster, Cover, Extend, Remix. Each runs on v6, so warn the user that the result can drift from the original character even when the source is untouched.

Suno documents nothing either way about Replace Section, Crop, stems, or the new plain-language editing applied to a pre-v6 song. Say that it is undocumented and suggest a trial rather than promising it works or refusing it.

A v5.5-era recipe cannot be rerun for comparison. When a user misses an old track's sound, treat the old song as the reference and rebuild toward it on v6 rather than claiming the settings can be restored.

## Download Budget

Downloads became a capped resource separate from credits on 2026-09-03, per [Suno's downloads and Terms update](https://suno.com/blog/suno-updates-tos): 7 lifetime on Free, 20 per month on Pro, 60 per month on Premier, with Studio exports on Premier uncapped. One song is one download regardless of format or re-download, and its stems come inside that same download.

This constrains the loop this reference teaches. Credits buy far more generations than downloads allow releases, so the expensive step is deciding, not generating. Audition and compare inside Suno, and spend a download once a take is final. Flag the cost before recommending a workflow that ends in several downloaded files, and be specific with a free-plan user, where seven downloads is the whole account for its lifetime.

## Edit-vs-Re-roll Decision

| Situation | Do this |
| --- | --- |
| One verse/chorus is weak, rest is good | Replace Section |
| One line is mumbled / mispronounced | Rewrite that line simpler, Replace Section |
| Song ends early or fades wrong | Extend (with `[End]`) |
| Model added verses you did not write | Crop an unwanted tail; edit or remove an internal span. Request closure with `[End]` on future generations. |
| Right song, wrong genre | Cover / Remix with a new Style line |
| Need a loop or specific length | Crop |
| Going to a DAW | Stems |
| Whole vibe is off, structure too | New prompt: change one lever, re-roll |
| Old take, low fidelity, otherwise liked | Remaster |

## Output Note

When iteration matters, add a compact plan to `Suno v6 Notes:`, e.g.:

```text
Suno v6 Notes:
- Generate, keep the stronger of the two takes.
- If the bridge is missing, Extend with the [Bridge]/[Final Chorus] block and [End].
- If V2 mumbles, simplify those lines and Replace Section.
```

Keep it to a few lines. Do not narrate the whole Studio feature set unless the user asks.

## Studio 2.0: When Text Is Not Enough

Suno's [Studio 2.0 announcement](https://suno.com/blog/studio-2), released 2026-08-13 and checked 2026-09-05, describes MIDI import/recording/editing, MIDI clips as generation prompts, automation, audio effects, and a beta chat bar. The announcement lists Premier access; check the user's current entitlement before prescribing it.

- Exact motif or bass rhythm: use a MIDI clip or recorded reference to communicate notes and timing.
- Precise section lift: arrange layers and automate parameters rather than requesting the same change repeatedly in text.
- One instrument needs work: compare stems and edit that part while preserving the useful performance.

Offer this route when the brief needs it. This skill prepares the musical brief; it does not operate Studio or create a MIDI file unless an available tool is used for that action.

## Take Comparison And Stopping Rule

For iteration requests, agree on the most important two or three listening criteria: hook delivery, intelligibility, groove, identity, ending, or a specific cue. Compare the available takes before changing the prompt.

| Take | Source / Model / Mode | Prompt And Settings | One Change | Heard Result | Keep / Next Step |
| --- | --- | --- | --- | --- | --- |
| A | User's clip or take ID | Exact prompt; visible controls; selected Voice/upload | Baseline | User observation or actual listening note | Keep the strongest section |
| B | Same source and model | Same except the tested variable | Shorter chorus phrasing | Record after listening | Keep, edit, or revert |

Retain the final expanded Style text if My Taste was used. Record Audio Influence only with an audio reference. Text-only review cannot score the rendered mix, pronunciation, or loop boundary; mark these pending if no audio was heard.

For an unspecified iteration budget, propose a baseline comparison and one targeted change, then reassess. Stop when the priority criteria pass or comparisons cease to improve them; use an edit for a local defect. Do not recommend endless paid re-rolls. A user's explicit credit or attempt budget takes precedence.
