# Song Matrix

Use a matrix to turn a vague brief into musical choices, compare treatments, or fix a song whose sections do not develop. Fill only the cells that affect the work. This is a planning aid, not a required form or Suno syntax.

## Decision Matrix

| Axis | Choose | What It Changes |
| --- | --- | --- |
| Song promise | Want, refusal, confession, discovery, celebration | What the hook must communicate |
| Speaker and listener | Who sings, to whom, from what moment | POV, diction, stakes, tense |
| Emotional movement | Denial to admission; fear to action; stillness to acceptance | What must change between sections |
| Hook carrier | Title phrase, rhythmic chant, melodic contour, instrumental riff | What repeats and what gets space |
| Groove | Straight, swung, shuffled, half-time; meter and pulse | Phrase placement and rhythmic density |
| Harmonic motion | Pedal/drone, repeating loop, delayed resolution, changing bass | Tension without adding more words |
| Contrast | Density, register, rhythm, harmony, width, silence | How the next section feels different |
| Signature | One image, instrument, rhythmic cell, or production gesture | What identifies this song |
| Constraint | Target time, language, vocal range if known, loop or ending | What the draft must fit |

Choose a lane from `genre-palettes.md` only when needed. A sad lyric can ride a bright groove; emotional contrast is a choice. Do not infer key or singer range from mood or gender.

For alternatives, offer two or three distinct hook/arrangement directions, state the tradeoff, and develop the user's choice. Do not generate combinatorial tables of every possible genre and mood.

## Section Matrix

A useful row records section, story job, approximate bars, relative energy, phrase/hook behavior, and arrangement change. Energy 1-5 is a comparison within this song, not a loudness setting.

Example: a 96 BPM, 4/4 country-soul song about returning a borrowed truck after a falling-out. Hook: "I brought it back." These are planning choices, not fixed defaults.

| Section | Bars | Story Job | Energy | Phrase / Hook | Arrangement Change |
| --- | --- | --- | --- | --- | --- |
| Intro | 4 | Establish the empty driveway | 1 | Guitar motif, no words | Guitar pickup and rim clicks |
| Verse 1 | 8 | Keys, dented fender, unsaid apology | 2 | Conversational pairs with breath gaps | Bass enters; narrow vocal |
| Chorus | 8 | Returning the truck means trying again | 4 | Repeat title; leave its last word space | Full backbeat and response guitar |
| Verse 2 | 8 | Owner opens the door; stakes change | 2 | New action, familiar phrase rhythm | Pull back drums; keep bass motion |
| Chorus | 8 | Same words, now heard as an offer | 4 | Preserve the recognizable hook | Add one backing response |
| Bridge | 4 | Admit what cannot be repaired | 1 | Brief confession, no new subplot | Drop drums; hold harmony |
| Final Chorus | 8 | Accept an imperfect reconciliation | 5 | Keep hook, change one earned line | Restore band, broaden harmony |
| Outro | 4 | Leave the keys within reach | 1 | Guitar motif returns | Short resolved ending |

This is 52 bars, about 130 seconds before pickup or tail. A bridge is optional. For a refrain song, put the hook at verse ends; for a loop, replace the final cadence with a return that matches the opening texture.

## Bar And Time Budget

For a steady tempo:

```text
seconds = bars * beats_per_bar * 60 / BPM
bars = seconds * BPM / (60 * beats_per_bar)
```

Use beats that match the BPM unit. In 4/4 with quarter-note BPM, beats_per_bar is 4. In 6/8 with dotted-quarter BPM, it is 2; with eighth-note BPM, it is 6. State the assumption rather than mixing units. Sum separate sections if tempo changes; free-time passages need a listening estimate.

At 120 BPM in 4/4, 8 bars take 16 seconds. A 90-second plan has about 45 bars before pickups and tails. Allocate sections first, then fit lyric phrases; four lyric lines do not necessarily occupy four bars. Leave room for sustained notes, rests, solos, and the ending. A half-time groove changes perceived pace without necessarily changing the BPM grid.

Suno may depart from the plan. For a delivered exact cut or game loop, audition and edit the generated audio. Check the loop boundary for clicks, reverb tails, groove alignment, and harmonic return; a `[Loop Point]` tag does not prove it loops.

## Prosody And Hook Pass

Speak the lyric over the intended pulse. Mark natural word stress privately and look for collisions with strong beats. Shorten clauses that force rushed syllables; keep an intentional syncopation that still reads naturally. Without a melody or audio, describe singability as a draft assessment.

Check the hook in three ways: can it stand alone, does its rhythm recur, and is there room to sustain or answer it? A chorus can contrast with dense verses through fewer words and more silence. A rap refrain can use a rhythmic cell; an instrumental can reuse a contour or timbre instead of a title phrase.

## Diagnose Before Rewriting

| Symptom | First Change To Try | Keep Fixed |
| --- | --- | --- |
| Chorus feels like another verse | Reduce its phrase density or change register/entry | Central hook and story |
| Verse 2 repeats Verse 1 | Add a consequence, new action, or changed listener | POV and groove |
| Constant maximum energy | Remove a layer or add a rest before the payoff | Tempo and signature motif |
| Too many ideas | Give one hook the foreground; move a competing idea to another song | User's main promise |
| Lyric rushes | Reduce syllables or allocate more bars | Meaning and natural stress |
| Genre blend loses identity | Assign rhythmic and textural roles | Requested genres |
| Loop feels finished | Remove terminal cadence; match exit to entrance | Motif and pulse |

Change one cause at a time. For generated audio, use the take comparison workflow in `studio-and-iteration.md` and distinguish an actual listening observation from a prediction.
