# Personas

Use this reference to create and reuse a **persona** (a consistent fictional singer, rapper, band, or vocal act) so multiple songs share the same voice, cadence, lyrical fingerprint, and sound. A persona is captured in a small Markdown file kept in the user's project so any later request can load it and stay consistent.

A persona can be built two ways:
- **Custom**: from the user's own description (`a weary low-baritone outlaw-country singer who...`, `a glitchy hyperpop duo that...`).
- **Style-reference**: by pointing at a real artist or group; decode their *style, cadence, and vocal character* into a fingerprint and **never carry the real name into prompts, into the `Style:` field, or into the spec file's operational sections** (see `references/remix-and-style-match.md` and `references/suno-v6-controls.md` § No Artist Names). The persona file records the decoded fingerprint, not the name.

Either way the persona is a fictional act with a name the **user** chooses (or you suggest and they approve), not a real person.

## When To Use

Triggers: "create a persona / artist / band", "make a consistent singer", "build an artist identity for my project", "I want all my songs to sound like the same artist", "use my persona <name>", "write a song as <persona>", "make a persona based on the style/cadence/vocals of <artist>", "give me a singer I can reuse".

## This File Is Not A Suno Feature

The persona file is a portable creative brief. It does not select, train, or reproduce anything inside Suno by itself, and it carries no guarantee that two songs render the same singer. Suno provides the platform features that do that work, and a persona file should record which of them the act uses rather than duplicating their job.

**Voices and Style Personas are one surface, not two.** Style Personas sits inside the Voices menu and opens `Create a Voice` (Beta): record or upload a sample, and Suno uses it "to influence how your generated songs sound." Older Personas were converted into that library, so an existing one is reached through `Select from library` rather than a separate Personas screen.

| Input | Notes |
| --- | --- |
| `Upload Audio` or drag a file | An existing recording |
| `Record` | Captured in the browser |
| `Select from library` | Previously captured voices, including converted older Personas |

The in-product guidance: sing in the style and language you want, pick a quiet spot, at least 10 seconds. Suno's [Voices article](https://help.suno.com/en/articles/11362369) states a 15 second minimum and describes a spoken verification step; the shipped UI asks for 10 seconds. Follow the UI. Generation with a Voice is limited to its creator, and the feature is 18+ and geographically restricted.

[Custom Models](https://help.suno.com/en/articles/11362497) are a different thing again: a private model trained on at least 6 of the user's own songs, max 3 per account, now running on v6. A model is not a voice.

Keep these distinct in output. A Voice or Style Persona is captured audio, a Custom Model is a trained model, and this file is a written brief. Never describe one as another, and never claim a text description selects any of them.

Suno's help center has lagged the shipped UI repeatedly, including on this feature's own minimum sample length. When a spec depends on a platform feature, ask the user what their screen shows and record that. Whether a Style Persona captured under a retired pre-v6 model still applies to a v6 generation is not documented either way; treat it as worth a trial, not a promise.

## Where The File Lives

Write the persona to `personas/<persona-slug>.md` relative to the user's working directory; create the `personas/` directory if it doesn't exist. `<persona-slug>` is the persona name in kebab-case. If a file already exists at that path, do **not** overwrite it silently: show the user what's there and confirm, or use a new slug. An optional `personas/README.md` index is fine but not required. (These files go in the user's project, never in the skill repo.)

## Persona File Schema

```markdown
---
name: <persona stage name - fictional, user-chosen>
slug: <kebab-case>
type: persona
basis: custom | style-reference
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
voice_id: <Suno Voice name if one is associated, else none>
style_persona: <Suno Style Persona name if one is associated, else none>
custom_model: <Suno Custom Model name if associated, else none>
---

# <Persona Name>

## Identity
<One short paragraph: what kind of act this is, the lane they live in, what they're known for, the era/scene their sound evokes. Optional light backstory only if the user wants it - keep it serving the music.>

## Vocals
- Configuration: <solo male / solo female / duo / group / androgynous; number of voices>
- Voice type & range: <e.g. warm low baritone; bright belt soprano; raspy alto>
- Timbre & texture: <breathy, gritty, smooth, nasal, airy, full-bodied...>
- Delivery: <conversational, declamatory, intimate, aggressive, deadpan, theatrical...>
- Ad-libs & habits: <signature ad-libs, hums, vocal tics, harmony habits, call-response>
- Accent / dialect: <e.g. light Southern US; London; none specified>
- Vocal production: <raw / lightly doubled / heavily stacked / autotune-as-texture / dry-and-upfront / reverb-washed...>

## Cadence & Phrasing
<For rap personas: flow character - syllable density, pocket (behind / on / ahead of the beat), triplet vs straight feel, internal-rhyme density, multisyllabic rhyme, breath habits. For sung personas: melodic tendencies, range use, melisma, phrasing against the beat, where the big notes land. Concrete enough to reproduce.>

## Lyrical Fingerprint
- Themes: <what this act writes about>
- Diction & register: <vocabulary level, slang era/region, formality, profanity level>
- Recurring imagery: <the domains they pull images from - places, objects, references>
- Point of view: <first/third-person tendencies, narrator stance>
- Language(s): <primary language + dialect; any code-switching habit - see references/multilingual.md>
- Anti-patterns: <words / clichés / moves this act avoids - extends the skill's anti-generic list>

## Sonic Palette (Style kernel)
- Genre / subgenre lane(s): <primary, plus any secondary>
- BPM bands: <typical ranges>
- Signature instruments: <4-8 listed; pick 2-4 for any actual Style line>
- Production texture: <the mix / recording character>
- Reusable Style kernel: `<a ~120-char Style fragment every song starts from, before adding the specific song's mood / theme / tempo>`

## Excluded Styles
<genres, instruments, vocal traits, moods, production traits this persona never uses>

## Suno Defaults
- Model: <v6 unless the act's identity wants v6-wild; v6-mini on the free plan>
- Weirdness: <range>
- Style Influence: <range>
- Variety: 0 <a persona only stays recognizable if its Style kernel reaches generation unrewritten; raise it only for a one-off experiment>
- Voices / Custom Model: <how to handle if associated - e.g. "select Voice '<name>'; don't over-describe the voice in Style">
- Notes: <any standing Suno-specific guidance for this act>

## Basis
<basis: custom - "Built from the user's description on <date>."
basis: style-reference - "Decoded from the style, cadence, and vocal character of a reference act. The reference name is intentionally kept out of all prompts and out of this file's operational sections; the fingerprint above stands on its own. All output is original." (The user may keep the inspiration source in their own private notes.)>

## Song Log
| Date | Title | Output file | Notes |
| --- | --- | --- | --- |
| | | | |
```

## Creating A Persona

1. Determine the basis. If style-reference, run the style-fingerprint extraction in `references/remix-and-style-match.md` (use web/search if the harness has it to sharpen the fingerprint, but never pull verbatim lyrics in), then translate everything into the schema above. Do not record or use the reference artist's name in the file's operational sections or in any prompt.
2. Get or propose the persona's fictional name; confirm if the user didn't give one.
3. Fill the schema. Be concrete: "warm low baritone, conversational, sits slightly behind the beat" beats "nice male voice." Leave a field `unspecified` rather than inventing detail the user didn't ask for, but offer a sensible default and label it as an assumption.
4. Write `personas/<slug>.md` (creating `personas/` if needed). Don't overwrite an existing file without confirmation.
5. Tell the user the path and give a one-line summary.

## Using A Persona To Write A Song

When the user asks for a song "as <persona>" or names a persona:
1. Read `personas/<slug>.md`.
2. Build the song with the persona's sonic palette as the `Style:` kernel, then layer the **specific song's** mood, tempo, and theme on top, without contradicting the persona's lane or excluded styles.
3. Keep vocals, cadence, and lyrical fingerprint consistent with the file. If the request conflicts with the persona (a ballad persona asked for a death-metal track), flag it and ask whether to bend the persona for one song or update the persona file.
4. Apply the persona's Suno defaults (model, sliders, Variety 0, Voice / Style Persona / Custom Model handling) unless the user overrides.
5. Append the new song to the persona's Song Log (update the file).
6. If the song reveals something new and consistent about the act (a habit, a recurring image), offer to update the persona file.

## Output Contract Additions

When a song is generated under a persona, add a `Persona:` line near the top of the output (persona name + file path), and in `Checks:` add:
- vocal identity matches the persona file
- cadence / phrasing matches
- lyrical fingerprint (themes, diction, imagery) matches
- sonic palette consistent with the persona; excluded styles respected
- no real-artist name in `Style:` (for style-reference personas)
- Variety at 0, so the persona's Style kernel reaches generation unrewritten

## Checks (when creating/updating a persona)

- Name is fictional and user-approved.
- Schema fields are concrete enough to reproduce the act.
- For style-reference personas: the reference name is absent from operational sections and from any prompt; the fingerprint stands on its own.
- Reusable Style kernel is ≤ ~120 chars and leaves room for per-song additions.
- Excluded styles don't contradict the sonic palette.
- File written to `personas/<slug>.md`; existing file not overwritten without confirmation.
