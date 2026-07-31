# Suno v5.5 Controls

Use this reference for Suno-specific vocal/custom prompt fields, sliders, personalization, and troubleshooting. For Instrumental Mode, do not return Style, Excluded Styles, or sliders; use `Instrumental Prompt:` plus `Arrangement:` instead.

## Field Separation

Keep fields clean:

- `Style:` positive musical direction only for vocal/custom modes.
- `Excluded Styles:` negative sound direction only for vocal/custom modes.
- `Lyrics:` singable words and section tags only.
- `Instrumental Prompt:` paste-ready natural-language prompt for Instrumental Mode.
- `Arrangement:` musical cue map for instrumental tracks.
- `Suno v5.5 Notes:` short operational guidance only when useful.

## Title Field

Suno has a separate Title field. It is mostly a label, but the model does read it: a vivid, on-theme title nudges mood and lyrical content, and a generic one (`Untitled`, `Song 1`) wastes a small signal. Use the same `Title:` you put in the output. For vocal/custom modes, do not stuff genre or production words into the title; that belongs in `Style:`. For Instrumental Mode, put genre/production detail in `Instrumental Prompt:`.

## Style Field

Use this only for vocal/custom modes, not Instrumental Mode.

Use a compact positive prompt:

```text
[genre/subgenre], [mood], [BPM], [vocal style or no vocals], [instruments], [production], [theme/cue function]
```

Vocal/custom good:

```text
garage rock, restless and defiant, 132 BPM, raw group vocals, distorted guitars and live drums, punchy basement production
```

If the user is not using Instrumental Mode, this can describe a no-vocal custom track:

```text
lofi chillhop, relaxed 78 BPM, no vocals, dusty drums, mellow Rhodes, upright bass, vinyl texture, loopable study beat
```

Avoid:

```text
pop, sad, cool, no country, no drums, no guitar, not too slow, make it viral
```

A useful quick frame for the positive direction is three anchors plus modifiers: core genre/subgenre, vibe/texture, and the lead instrument or signature sound, then add tempo, vocal, and production. For example `Delta blues, dusty and analog, slide resonator guitar` or `synthwave, neon-cold and propulsive, fat analog bass and gated drums`: then extend with BPM, vocal, mix.

### No Artist Names

Do not write `sounds like <artist>`, `<artist> type beat`, or song titles in the Style field. Suno's copyright filters increasingly reject these or return a flattened, generic take. Describe the era, scene, and production instead:

- not `sounds like Drake` -> `early-2010s Toronto melodic rap, moody nocturnal R&B production, sparse 808s, reverbed vocal`
- not `like a Tarantino soundtrack` -> `1960s surf rock and spaghetti-western score, twangy reverb guitar, dramatic horns`
- not `make it sound like <band>` -> name the subgenre, the decade, the rhythm section, and the mix character that band is known for

This also keeps the prompt portable to other AI music tools and easier to tweak one trait at a time.

## Excluded Styles

Use Suno's `Excluded Styles` input as a negative prompt field for vocal/custom modes. Instrumental Mode does not expose this field; put must-avoid vocal texture in `Instrumental Prompt:` instead.

Good exclude targets:
- unwanted genres: `country`, `EDM`, `metal`, `trap`
- unwanted instruments: `banjo`, `saxophone`, `distorted guitar`, `808 bass`
- unwanted vocal traits: `male vocal`, `female vocal`, `choir`, `rap vocals`, `spoken word`
- unwanted production or mood: `lo-fi`, `muddy mix`, `comedy`, `children's music`, `happy upbeat tone`
- unwanted language drift: `English lyrics`, `Spanish vocals`, `K-pop style` when those conflict with the target

Keep it short. Three to seven precise items usually works better than a long list.

Never exclude a trait requested in `Style:`.

## Weirdness

Do not return slider suggestions for Instrumental Mode.

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
- surreal custom-mode cues

## Style Influence

Do not return Style Influence suggestions for Instrumental Mode.

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
| Cross-genre fusion (anchor + accent blends) | 45-60% | 75-85% | One notch above the anchor lane's normal Weirdness; keep Style Influence high so the written blend holds. See `references/genre-fusion.md`. |
| Ambient, noise, avant-garde, surreal experiments | 70-100% | 20-65% | Expect inconsistent takes; regenerate more. |
| Custom Model consistency | 15-40% | 65-85% | Let model identity show without derailing the track. |
| Trained Voice consistency | 15-35% | 70-90% | Lower Weirdness protects vocal identity and delivery. |

## Duration

v5.5's Create form has a **Duration control** (web): **Auto** (default: the model picks a natural length) or **Custom**, a slider from **0:10 to 6:00 in 5-second steps**.

- Leave **Auto** for standard full songs with no target cut.
- Use **Custom** when the brief has a length: TV-size OP/ED (~1:30), sting (30-60s), ident, ad read, or a loop of known bar length. Recommend the setting in `Slider Suggestions:`.
- **The slider does not compress the lyric:** Match the written structure to the set time: an oversized `Lyrics:`/`Arrangement:` body gets rushed or cut off mid-phrase. Write the cut to size *and* set the slider.
- Set Custom **5-15s longer than the intended cut** so the ending resolves instead of clipping, then **Crop** to the exact time.
- The most reliable band for full songs is roughly **2:00-3:30**; very long Custom settings stretch material thin.
- `[End]` / `[Fade Out]` still control *how* the track closes; **Crop** trims and **Extend** lengthens after the fact.

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

## Content Filters

Suno can silently reject, blank, or blandly average a generation when the inputs trip a content or copyright filter. Common triggers:

- names of real living people, bands, or song titles: in `Style:`, `Instrumental Prompt:`, **and** `Lyrics:` (see `Style Field` § No Artist Names)
- brand and trademark names
- explicit profanity or slurs (some profanity is allowed; heavy use is risky)
- graphic violence, sexual content, or self-harm depiction in the lyrics

If a generation comes back blank or weirdly generic, suspect the filter before the sliders. Fixes: replace the proper noun with a description, soften or imply the explicit content, or move the edge into subtext. Note any deliberate softening in `Suno v5.5 Notes:` so the user knows why a line changed.

## Iteration

Suno returns two takes per generation: treat the first run as picking the stronger seed, not the final answer. Build from the better take with Extend / Replace Section / Remix rather than re-rolling the whole prompt. When you do re-roll, change one lever at a time: prompt, Weirdness, or Style Influence. For Extend, Cover/Remix, Replace Section, Crop, stems, and the edit-vs-re-roll decision, see `references/studio-and-iteration.md`.

## Troubleshooting

- Style ignored: raise Style Influence by 10-15%, front-load genre, remove conflicting tags.
- Output too generic: raise Weirdness by 10% or add one sharper production descriptor.
- Output chaotic: lower Weirdness by 10-20%.
- Vocal identity drifts: lower Weirdness and simplify vocal descriptors.
- Wrong genre appears: add it to `Excluded Styles` and keep Style Influence medium-high.
- Generic or blocked result from an artist reference: remove the artist name and rebuild the Style line from era, subgenre, rhythm section, and mix character.
- Blank or oddly generic generation: suspect a content/copyright filter: check for real names, brands, or explicit lyrics before touching sliders.
- Vocals mumbled or unintelligible: cut syllables per line, use stronger open vowels, simplify the syntax, and slow the implied delivery; then Replace Section rather than re-rolling the whole take.
- Model invents extra verses you didn't write: add `[End]` after the last section in the lyrics (see `references/suno-meta-tags.md`); to remove an already-generated extra section, use Replace Section.
- Chorus sounds like just another verse: make the chorus lyrics mechanically simpler: shorter lines, fewer new images, more repetition of the title phrase.
- Pronunciation or accent drift (esp. non-English): respell the problem word phonetically in the lyric line, or add a `Pronunciation Notes:` line; for one bad word in a good take, Replace Section.
- Mix feels muddy: add positive style terms such as `clean production`, `wide stereo`, `clear vocal upfront`.
- Prompt feels overcontrolled: remove half the adjectives before changing sliders.
- When iterating, change one thing at a time: prompt, Weirdness, or Style Influence.
