# Suno Sounds (Custom Audio Samples)

Use this reference when the user wants an individual **audio sample** rather than a song or a full instrumental track: a sound effect, foley hit, ambience bed, transition/whoosh, animal sound, or a musical one-shot / drum loop. Suno's "Sounds" feature generates these from a text prompt plus a few settings; the output here is a sound prompt, not the song or instrumental contract.

Reference: Suno help: "Suno Sounds: Generate Custom Audio Samples" (`help.suno.com/en/articles/10625537`). It's an experimental feature; behavior may change.

## When To Use

Triggers: "make me a <sound effect>", "I need a whoosh / glitch / riser / impact", "generate an 808 kick one-shot", "a snare sample", "a drum loop at 90 BPM in A minor", "rain ambience", "city-street background noise", "footsteps foley", "a sci-fi teleport sound", "a sound sample / SFX for my video / game / podcast / stream".

If the user wants a *piece of music* (even a short one with melody or harmony (a sting, an ident, a melodic loop)) that is an instrumental track: use `references/instrumental.md` and return `Instrumental Prompt:` plus `Arrangement:`, not this sound-sample contract.

## What Suno Sounds Does

Generates a short custom audio clip from a text description, with three settings:

- **Type:** `One Shot` (a single, non-repeating sound) or `Loop` (a clip built to repeat without an audible seam).
- **BPM:** for rhythmic material (drum loops, pulsing ambience) so it locks to a tempo.
- **Key:** a musical key (e.g. `C major`, `A minor`) for pitched/tonal material so it sits in a track.

Categories it handles well:
- **Sound effects & transitions**: e.g. `cinematic whoosh`, `digital glitch effect`, `sci-fi teleport swoosh`, `fast aggressive swish with bass`
- **Ambient & background noise**: e.g. `gentle rain on window`, `busy city street`, `forest with birds`, `coffee shop ambiance`
- **Foley & action sounds**: e.g. `footsteps on wooden floor`, `heavy metal door slam with echo`, `thunder rumble`, `ocean waves crashing`
- **Animal sounds**: e.g. `lion roaring`, `horse neigh and galloping`, `dog barking (medium-sized breed)`
- **Musical samples & drum kits**: e.g. `deep 808 kick drum one shot`, `crisp hip hop snare`, `tight clap sample`, `bongo drums pattern loop`

## Writing A Good Sound Prompt

- **Be specific and concise:** `wind howling strong` beats `a windy atmosphere`; `heavy metal door slam with echo` beats `door noise`.
- **Use recognizable onomatopoeic/technical vocabulary** the model knows: `whoosh`, `swish`, `glitch`, `riser`, `impact`, `boom`, `rumble`, `crash`, `crackle`, `hum`, `drone`, `bark`, `neigh`, `kick drum`, `snare`, `clap`, `hi-hat`, `808`, `ambiance`.
- **State duration when it matters:** `5-second sci-fi teleport swoosh`, `10-second forest-with-birds ambience`.
- **Add character:** material (`on wooden floor`, `metal`, `gravel`), space (`with echo`, `in a small room`, `distant`), motion (`fast aggressive`, `slow building`), size (`medium-sized dog`, `huge cinematic`).
- **Match Type to intent:** One Shot for discrete effects, stingers, single hits; Loop for ambience beds, drum grooves, sustained textures.
- **Set BPM/Key for musical material** so the sample drops into a session cleanly; leave them unset for pure SFX/ambience.

## Output Shape

A Sounds request returns, instead of the song contract:

```text
Sound: <the prompt - specific, concise, with material/space/motion/size and duration when useful>
Type: One Shot | Loop
BPM: <number, or n/a>
Key: <musical key, or n/a>
Variations: <2-3 alternate phrasings to try if the first take misses>
Notes: <optional - usage/layering tips; note that it's experimental so results vary>
```

For several related samples (a small SFX pack, a drum-kit set), list each as its own `Sound:` block with a one-line label.

## Checks

- It is a sample request, not a short *piece of music* (which would be an instrumental track instead).
- Prompt is specific and uses vocabulary the model recognizes.
- Type matches intent (One Shot vs Loop).
- BPM/Key set for musical material, omitted for pure SFX/ambience.
- Duration stated when it matters.
- Variations offered for retry.
