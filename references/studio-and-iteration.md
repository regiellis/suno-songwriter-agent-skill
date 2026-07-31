# Studio And Iteration

Use this reference for what happens after the first generation: choosing between takes, extending, restyling, fixing a section, splitting stems, and deciding whether to edit or re-roll. This is workflow guidance to fold into `Suno v5.5 Notes:` when the user is iterating or preparing a production, not something to dump on every request.

## Two Clips Per Run

Suno returns two variations per generation. Treat the first run as "pick the stronger seed," not "the answer." Advise the user to keep the better take and build from it (Extend / Replace Section / Remix) rather than regenerating the whole prompt repeatedly: re-rolling from scratch throws away a take that was already 80% right.

When a prompt is close but not landing, change **one** lever at a time between runs: the prompt, or for vocal/custom modes, Weirdness or Style Influence (see `references/suno-v55-controls.md` § Troubleshooting).

## Extend

Continues an existing track from a chosen point.

Use for:
- a take that ends too early or fades awkwardly
- adding a bridge, solo, or outro that the original didn't generate
- building a longer arrangement in stages

Tips:
- Feed the continuation only the *new* sections in the lyrics box, with section tags, so the model knows what comes next.
- Keep the Style line consistent with the original take or the seams will be obvious.
- Use `[End]` on the final extension to stop further additions.

## Cover / Remix / Restyle

Re-generates a song in a new style while keeping the melody/structure (Cover) or reworks the arrangement (Remix), driven by a new Style line.

Use for:
- "same song, different genre": write a fresh Style line for the target lane (see `references/genre-palettes.md`)
- turning a demo idea into a polished version
- A/B-ing two production directions for the same lyrics

Tips:
- The new Style line does the work here; keep it specific.
- Expect melody to drift somewhat on heavy genre changes; in vocal/custom modes, lower Weirdness if it drifts too far.

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

## Crop / Trim

Cuts the track to a span: for grabbing a clean loop, a stinger, or removing a bad intro/outro tail. Mention when the user needs a specific length or a loop for game/video use.

## Stems

Splits a finished track into separate audio layers (commonly vocals, drums, bass, other / instrument groups).

Use for:
- handing the track to a DAW for mixing, re-arranging, or scoring to picture
- isolating an instrumental from a vocal take (or vice versa) without re-generating
- replacing one layer with live performance

Note in `Suno v5.5 Notes:` when stems are part of the intended workflow (e.g. `Plan: generate, pick take, split stems, mix in DAW`). Don't promise specific stem counts/quality: it varies.

## Remaster

Re-renders an older or lower-fidelity generation at current model quality. Mention only when the user is reviving an old track or complains about fidelity on a take they otherwise like.

## Edit-vs-Re-roll Decision

| Situation | Do this |
| --- | --- |
| One verse/chorus is weak, rest is good | Replace Section |
| One line is mumbled / mispronounced | Rewrite that line simpler, Replace Section |
| Song ends early or fades wrong | Extend (with `[End]`) |
| Model added verses you didn't write | Replace Section to remove, or re-roll with `[End]` in lyrics |
| Right song, wrong genre | Cover / Remix with a new Style line |
| Need a loop or specific length | Crop |
| Going to a DAW | Stems |
| Whole vibe is off, structure too | New prompt: change one lever, re-roll |
| Old take, low fidelity, otherwise liked | Remaster |

## Output Note

When iteration matters, add a compact plan to `Suno v5.5 Notes:`, e.g.:

```text
Suno v5.5 Notes:
- Generate, keep the stronger of the two takes.
- If the bridge is missing, Extend with the [Bridge]/[Final Chorus] block and [End].
- If V2 mumbles, simplify those lines and Replace Section.
```

Keep it to a few lines. Do not narrate the whole Studio feature set unless the user asks.
