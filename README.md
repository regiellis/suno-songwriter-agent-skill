# Suno Songwriter

> [!NOTE]
> I don't use Suno for professional music production. I use Suno to create music for my own personal listening, and this skill was built for that kind of use.

Portable agent skill for creating Suno v6-ready vocal songs, instrumental tracks, vocal style prompts, excluded styles, Advanced slider suggestions, multilingual lyric adaptations, and broader AI music prompts.

This is an agent skill, not a Codex-only package. Any harness can use it if it can read `SKILL.md`, decide when the skill applies, and optionally load files from `references/`.

## Documentation

Browseable docs live at [regiellis.github.io/suno-songwriter-agent-skill](https://regiellis.github.io/suno-songwriter-agent-skill/): the output contract, workflow, every mode, Suno v6 controls, and the full reference index. The site is a single static page in `docs/`, served by GitHub Pages, no build step.

## What It Covers

- Song planning matrices: story movement, hooks, energy, arrangement, and timing
- Suno v6 song packages for Simple or Advanced mode
- Lyrics, hooks, section structure, and singable rewrites
- Practical harmony and melody: chord motion, modes, motif development, vocal range, and chorus contrast
- Rhythm and arrangement: meter, subdivision, pocket, instrumental roles, and section transitions
- Songwriting craft: lyric angles, hook placement, section development, rhyme architecture, prosody, and revision diagnostics
- Five genre-writing families covering pop/roots/soul, rap/rock/heavy, electronic/experimental, regional/diasporic, and jazz/stage/screen directions
- Genre fusion through shared pulse, phrasing, harmony, form, and timbral roles, with conflict resolution and worked blends
- Instrumental prompts and arrangements for lofi, OST, game loops, ambience, and background music
- `Style` and `Excluded Styles` separation for vocal and Advanced modes
- Model choice across `v6`, `v6-wild`, and `v6-mini`, Weirdness and Style Influence starting ranges, Variety control for prompt comparisons, and Audio Influence when an upload exposes it
- Multilingual lyrics, translation, adaptation, dialect, script, and pronunciation notes
- Reference-lyrics transformation without copying the source too closely
- Songwriting frameworks including structure, Rule of 3, and 80/20 hook prioritization
- Individual audio samples and sound effects (Suno Sounds)
- Cover art and animated (looping-video) covers via Suno's Generate Cover Art / Animate tools (text-to-image, text-to-video, image-to-video)
- Reusable artist personas and cohesive album/EP planning
- Portable prompts for other AI music tools

## How Agent Harnesses Should Use It

At minimum, a harness should:

1. Read the YAML frontmatter in `SKILL.md`.
2. Use `name` and `description` to decide when the skill should trigger.
3. Load the body of `SKILL.md` when triggered.
4. Follow the routing instructions in `SKILL.md` to load only relevant files from `references/`.
5. Return outputs in the skill's requested shape: vocal songs use `Title`, `Style`, `Excluded Styles`, and `Lyrics`; instrumentals use `Title`, `Instrumental Prompt`, and `Arrangement`; add notes, slider suggestions, language notes, and checks only when useful and supported by the mode.

The `references/` directory is intentionally split for progressive disclosure. Do not load every reference for every request unless your harness has no selective loading mechanism.

## Harness Metadata

Harness-specific metadata belongs in `agents/`.

- `agents/openai.yaml` - OpenAI harness metadata

Other harnesses can add their own files, for example:

```text
agents/
  openai.yaml
  claude.yaml
  local-agent.json
```

Keep the portable behavior in `SKILL.md` and `references/`; keep product-specific configuration in `agents/`.

## How The Skill Is Organized

`SKILL.md` holds the workflow, output contract, quality criteria, and routing table. [The reference index](references/templates.md) lists focused guidance loaded only when needed.

Useful starting points:

- [Song matrix](references/song-matrix.md): connect section purpose, hooks, energy, phrasing, arrangement, and bar/time budgets.
- [Songwriting craft](references/songwriting-craft.md): lyric revision, stress, rhyme, concrete detail, and groove narrative.
- [Output templates](references/output-templates.md): vocal, instrumental, and multilingual skeletons.
- [Suno controls](references/suno-v6-controls.md): model choice, field mapping, official sources, sliders, Max Mode, and personalization.
- [Production direction](references/v6-production-direction.md): community field notes on instrument activity, verse energy, production clauses, and ending buffers.
- [Studio and iteration](references/studio-and-iteration.md): take comparison, section repair, MIDI reference workflows, and stopping criteria.

The skill's instrumental labels are portable planning fields. In Suno's Advanced mode, the Instrumental toggle coexists with Styles and the rest of the Advanced controls; include available controls when requested. The roughly 200-character Style target is a compact default, not a platform limit. Prompt tags, BPM, key, and duration need checking against generated audio.

## Typical Invocations

Vocal song:

```text
Use $suno-songwriter to write a Suno v6-ready song about protecting a child from the world.
Genre: modern country.
Vocal: male.
Return title, style, excluded styles, lyrics, slider suggestions, and checks.
```

Instrumental:

```text
Use $suno-songwriter to create a no-vocal OST cue for a snow-covered village before a boss fight.
Use orchestral strings, celesta, low brass, and taiko.
Return title, instrumental prompt, arrangement, and useful notes or checks.
```

Multilingual adaptation:

```text
Use $suno-songwriter to adapt this chorus into Mexican Spanish for a singable Latin pop hook.
Keep the emotional meaning, not the exact wording.
Return language notes and pronunciation notes if needed.
```

Prompt controls:

```text
Use $suno-songwriter to improve this Suno v6 prompt.
Suggest Style, Excluded Styles, Weirdness, and Style Influence.
The song should be polished dance pop but not EDM or hyperpop.
```

## Installing in Claude Desktop and Codex Desktop

Use the **Download Skill ZIP** button on the [documentation site](https://regiellis.github.io/suno-songwriter-agent-skill/) for the bundled skill, or get a tagged version from the [latest release](https://github.com/regiellis/suno-songwriter-agent-skill/releases/latest). The zip contains the skill folder at its root, which is the layout both desktop apps expect.

### Claude Desktop

1. Download `suno-songwriter.zip` from the docs or a tagged release.
2. In Claude Desktop, open Settings, then Capabilities, then Skills (Pro, Max, Team, and Enterprise plans, with code execution enabled).
3. Choose Upload skill and select the zip.
4. Toggle the skill on. Claude reads the name and description from `SKILL.md` and triggers it on songwriting requests.

### Codex (desktop app and CLI)

Both read skills from the same directory. Unzip into it:

```bash
unzip suno-songwriter.zip -d ~/.codex/skills/
```

Codex matches your prompt against the skill description and loads it on demand. Invoke it explicitly with `$suno-songwriter` in a prompt.

### Claude Code and other harnesses

Clone or unzip into the harness's skills directory:

```bash
# Claude Code
unzip suno-songwriter.zip -d ~/.claude/skills/

# Generic agents directory
unzip suno-songwriter.zip -d ~/.agents/skills/
```

Installed copies are separate from this source checkout. When updating one, confirm its destination, copy the runtime files, and review stale references before removing them. Repository guidance and local writing tools are not part of the skill package.

## Validation

Basic validation:

```bash
ruby -e 'require "yaml"; YAML.load_file("SKILL.md"); YAML.load_file("agents/openai.yaml"); puts "YAML OK"'
```

Check source and installed copies:

```bash
diff -rq SKILL.md ~/.agents/skills/suno-songwriter/SKILL.md
diff -rq references ~/.agents/skills/suno-songwriter/references
```

Manual smoke tests should cover:

- vocal lyric output
- instrumental arrangement output
- multilingual adaptation
- Suno controls and sliders
- reference-lyrics transformation
- style selection without repeating the same sonic palette

For the behavioral test set, use [references/evals.md](references/evals.md). Text checks do not verify generated audio; keep listening results separate.

## Development Notes

- Keep `SKILL.md` concise and route deeper guidance to `references/`.
- Prefer adding new focused reference files over making one large reference file.
- Update `references/templates.md` whenever a new reference file is added.
- Update harness metadata under `agents/` without putting harness-specific behavior in `SKILL.md`.
- Update an installed copy only when that is part of the task.
