# Suno Lyrics

Portable agent skill for creating Suno v5.5-ready vocal songs, instrumental tracks, style prompts, excluded styles, slider suggestions, and multilingual lyric adaptations.

## What It Covers

- Suno v5.5 Custom Mode song packages
- Lyrics, hooks, section structure, and singable rewrites
- Instrumental prompts for lofi, OST, game loops, ambience, and background music
- `Style` and `Excluded Styles` separation
- Weirdness and Style Influence slider suggestions
- Multilingual lyrics, translation, adaptation, dialect, script, and pronunciation notes
- Reference-lyrics transformation without copying the source too closely
- Portable prompts for other AI music tools

## Files

- `SKILL.md` - main skill instructions and trigger description
- `references/templates.md` - reference index and routing map
- `references/output-templates.md` - reusable output skeletons and prompt patterns
- `references/suno-v55-controls.md` - Style, Excluded Styles, sliders, personalization, and troubleshooting
- `references/songwriting-craft.md` - hooks, sections, rhyme, meter, vivid detail, and lyric transformation
- `references/rule-of-3.md` - statement, repetition, twist, motif payoff, and arrangement focus
- `references/instrumental.md` - lofi, OST, game loops, ambience, and non-lyric arrangements
- `references/multilingual.md` - translation, adaptation, dialect, script, and pronunciation guidance
- `references/style-selection.md` - genre/palette selection and anti-lock-in examples
- `agents/openai.yaml` - OpenAI harness metadata

Other agent harnesses can use the skill by reading `SKILL.md` and loading reference files as needed. Harness-specific metadata should live under `agents/`.

## Typical Invocation

```text
Use $suno-lyrics to write a Suno v5.5-ready song about protecting a child from the world.
Genre: modern country.
Vocal: male.
Return title, style, excluded styles, lyrics, slider suggestions, and checks.
```

```text
Use $suno-lyrics to create a no-vocal OST cue for a snow-covered village before a boss fight.
Use orchestral strings, celesta, low brass, and taiko.
Return title, style, excluded styles, arrangement, slider suggestions, and checks.
```

## Install Location

One active installed copy may live at:

```text
/Users/rellis/.agents/skills/suno-lyrics
```

Keep this repository copy and the installed copy synced when making changes.
