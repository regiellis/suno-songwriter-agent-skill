# Suno v5.5 Controls

Use this reference for Suno-specific prompt fields, sliders, personalization, and troubleshooting.

## Field Separation

Keep fields clean:

- `Style:` positive musical direction only.
- `Excluded Styles:` negative sound direction only.
- `Lyrics:` singable words and section tags only.
- `Arrangement:` musical cue map for instrumental tracks.
- `Suno v5.5 Notes:` short operational guidance only when useful.

## Style Field

Use a compact positive prompt:

```text
[genre/subgenre], [mood], [BPM], [vocal style or no vocals], [instruments], [production], [theme/cue function]
```

Good:

```text
garage rock, restless and defiant, 132 BPM, raw group vocals, distorted guitars and live drums, punchy basement production
```

Good:

```text
lofi chillhop, relaxed 78 BPM, no vocals, dusty drums, mellow Rhodes, upright bass, vinyl texture, loopable study beat
```

Avoid:

```text
pop, sad, cool, no country, no drums, no guitar, not too slow, make it viral
```

## Excluded Styles

Use Suno's `Excluded Styles` input as a negative prompt field. Put unwanted sound traits there instead of crowding the positive Style field with many `no...` phrases.

Good exclude targets:
- unwanted genres: `country`, `EDM`, `metal`, `trap`
- unwanted instruments: `banjo`, `saxophone`, `distorted guitar`, `808 bass`
- unwanted vocal traits: `male vocal`, `female vocal`, `choir`, `rap vocals`, `spoken word`
- unwanted production or mood: `lo-fi`, `muddy mix`, `comedy`, `children's music`, `happy upbeat tone`
- unwanted language drift: `English lyrics`, `Spanish vocals`, `K-pop style` when those conflict with the target

Keep it short. Three to seven precise items usually works better than a long list.

Never exclude a trait requested in `Style:`.

## Weirdness

Weirdness runs from Safe to Chaos. Around 50% is Suno's normal expected result. Lower values are more conventional and stable; higher values add surprise, unusual transitions, and more risk.

Use ranges:
- reliable genre song: 20-35%
- creative but listenable: 35-50%
- experimental but guided: 50-70%
- exploratory chaos: 70-100%

Lower Weirdness for:
- ballads
- worship
- children's music
- commercial pop
- trained Voice consistency
- clear emotional storytelling

Raise Weirdness for:
- hyperpop
- glitch
- art pop
- psychedelic
- avant-garde
- unusual fusions
- surreal instrumental cues

## Style Influence

Style Influence runs from Loose to Strong and controls how closely Suno follows the Style field.

Use ranges:
- specific genre/vocal/instrument target: 75-90%
- creative but still guided: 60-80%
- loose exploration: 20-60%

Raise Style Influence when:
- the generated song ignores the style prompt
- genre drift appears
- unwanted instruments keep appearing
- a Custom Model needs clearer direction

Lower Style Influence when:
- the output is accurate but stiff
- the prompt is intentionally broad
- the user wants unexpected interpretation

## Slider Recipes

| Goal | Weirdness | Style Influence | Notes |
| --- | --- | --- | --- |
| Clean commercial pop, country, worship, ballad | 15-35% | 75-90% | Stable structure, clear vocal, predictable genre results. |
| Emotional alt-R&B, indie, cinematic pop | 25-45% | 70-85% | Enough variation without distracting from lyric emotion. |
| Rap, trap, drill, phonk | 25-50% | 65-85% | Raise Weirdness for stranger flows or darker textures. |
| EDM, house, dance pop | 30-55% | 65-85% | Higher Weirdness can help drops and transitions feel less generic. |
| Hyperpop, glitch, psychedelic, art pop | 55-80% | 60-85% | Keep Style Influence strong if the fusion needs guardrails. |
| Ambient, noise, avant-garde, surreal experiments | 70-100% | 20-65% | Expect inconsistent takes; regenerate more. |
| Custom Model consistency | 15-40% | 65-85% | Let model identity show without derailing the track. |
| Trained Voice consistency | 15-35% | 70-90% | Lower Weirdness protects vocal identity and delivery. |

## Personalization

### Voices

If the user has a trained Voice selected, do not over-describe the voice. Use light phrasing like:

```text
in my trained voice
```

Avoid stacking incompatible vocal descriptions when the Voice is selected.

### Custom Models

If a Custom Model is selected, prompt normally around song intent. Avoid fighting the model with too many contradictory genre tags.

Good:

```text
signature style track, melancholic but hopeful, piano-driven, warm vocal, subtle electronic textures, building chorus
```

Avoid:

```text
my unique sound, jazz metal hyperpop reggae country opera, exactly like six unrelated artists
```

### My Taste

Suggest the Magic Wand in the Styles field for personalized suggestions, then revise the result for genre, mood, tempo, vocal, instruments, and exclusions.

## Troubleshooting

- Style ignored: raise Style Influence by 10-15%, front-load genre, remove conflicting tags.
- Output too generic: raise Weirdness by 10% or add one sharper production descriptor.
- Output chaotic: lower Weirdness by 10-20%.
- Vocal identity drifts: lower Weirdness and simplify vocal descriptors.
- Wrong genre appears: add it to `Excluded Styles` and keep Style Influence medium-high.
- Mix feels muddy: add positive style terms such as `clean production`, `wide stereo`, `clear vocal upfront`.
- Prompt feels overcontrolled: remove half the adjectives before changing sliders.
- When iterating, change one thing at a time: prompt, Weirdness, or Style Influence.
