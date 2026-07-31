# Suno Songwriter

> [!NOTE]
> I don't use Suno for professional music production. I use Suno to create music for my own personal listening, and this skill was built for that kind of use.

Portable agent skill for creating Suno v5.5-ready vocal songs, instrumental tracks, vocal style prompts, excluded styles, vocal/custom slider suggestions, multilingual lyric adaptations, and broader AI music prompts.

This is an agent skill, not a Codex-only package. Any harness can use it if it can read `SKILL.md`, decide when the skill applies, and optionally load files from `references/`.

## Documentation

Browseable docs live at [regiellis.github.io/suno-songwriter-agent-skill](https://regiellis.github.io/suno-songwriter-agent-skill/): the output contract, workflow, every mode, Suno v5.5 controls, and the full reference index. The site is a single static page in `docs/`, served by GitHub Pages, no build step.

## What It Covers

- Suno v5.5 Custom Mode song packages
- Lyrics, hooks, section structure, and singable rewrites
- Hook-first lyric quality gates: clear title/hook, chorus lift, stable point of view, concrete detail, and singable line lengths
- Instrumental prompts and arrangements for lofi, OST, game loops, ambience, and background music
- `Style` and `Excluded Styles` separation for vocal/custom modes
- Weirdness and Style Influence slider suggestions for vocal/custom modes
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

## Files

- `SKILL.md` - main skill instructions and trigger description
- `references/templates.md` - reference index and routing map
- `references/output-templates.md` - reusable output skeletons and prompt patterns
- `references/suno-v55-controls.md` - vocal/custom Style, Excluded Styles, sliders, Title field, personalization, content filters, and troubleshooting
- `references/suno-meta-tags.md` - inline lyric cues: instrumental moments, vocal delivery, multiple vocalists, ad-libs, sound effects, and `[End]` length control
- `references/studio-and-iteration.md` - choosing takes, Extend, Cover/Remix, Replace Section, Crop, stems, remaster, and the edit-vs-re-roll decision
- `references/songwriting-craft.md` - hooks, sections, rhyme, meter, point of view, vivid detail, and lyric transformation
- `references/song-structure.md` - section jobs, section-tag descriptors, common forms, bridge/pre-chorus choices, and structure fixes
- `references/rule-of-3.md` - statement, repetition, twist, motif payoff, and arrangement focus
- `references/eighty-twenty.md` - hook-first prioritization, high-impact revision, and 80% familiar / 20% fresh balance
- `references/instrumental.md` - lofi, OST, game loops, ambience, idents, vocal chops, and non-lyric arrangements
- `references/suno-sounds.md` - individual audio samples / sound effects / foley / ambience / drum one-shots and loops (Suno Sounds), with the `Sound`/`Type`/`BPM`/`Key` output shape
- `references/cover-art.md` - cover images and animated looping-video covers (Suno Generate Cover Art / Animate): text-to-image, text-to-video, image-to-video; image-prompt and motion-prompt craft; `Cover Concept`/`Image Prompt`/`Motion Prompt`/`Settings` output shape
- `references/screen-music.md` - anime openings/endings, TV theme songs, end-credit songs, trailer cuts, idents, game themes, and edit-length guidance
- `references/multilingual.md` - translation, adaptation, dialect, script, pronunciation, and Korean lanes beyond K-pop
- `references/style-selection.md` - genre/palette selection and anti-lock-in examples
- `references/genre-palettes.md` - per-lane BPM/instrument/production/vocal/structure menu, used as a picker not as defaults
- `references/genre-fusion.md` - multi-genre songs: fusion blends (anchor + accent), mid-song genre switches, and same-song genre versions
- `references/remix-and-style-match.md` - lyric remix/flip, writing in an artist's style/cadence without copying lyrics, and lyric-style analysis
- `references/personas.md` - creating and reusing a consistent artist persona; persona spec file written to the user's project
- `references/albums.md` - planning and maintaining a cohesive album/EP; album spec file written to the user's project
- `references/evals.md` - smoke tests, trigger queries, regression checks, and output rubric

## Reference Loading Guide

Use `references/templates.md` as the index.

Common routing:

- Full output skeletons: `references/output-templates.md`
- Suno vocal/custom controls and sliders: `references/suno-v55-controls.md`
- Inline lyric cues / meta-tags: `references/suno-meta-tags.md`
- Post-generation workflow (Extend, Remix, Replace Section, stems): `references/studio-and-iteration.md`
- Lyric craft and rewrites: `references/songwriting-craft.md`
- Song forms and section order: `references/song-structure.md`
- Stronger repetition/payoff: `references/rule-of-3.md`
- Hook-first revision: `references/eighty-twenty.md`
- Instrumental tracks: `references/instrumental.md`
- Individual audio samples / sound effects (Suno Sounds): `references/suno-sounds.md`
- Cover art / animated covers (text-to-image, text-to-video, image-to-video): `references/cover-art.md`
- Anime OP/ED, TV themes, trailers, idents, game themes: `references/screen-music.md`
- Non-English or bilingual lyrics (incl. Korean beyond K-pop): `references/multilingual.md`
- Genre and palette choice: `references/style-selection.md`
- Concrete per-lane palette menu: `references/genre-palettes.md`
- Blending genres, mid-song switches, multi-genre versions: `references/genre-fusion.md`
- Lyric remix / write in an artist's style / lyric-style analysis: `references/remix-and-style-match.md`
- Reusable artist persona (consistent singer/band): `references/personas.md`
- Cohesive album/EP planning across tracks: `references/albums.md`
- Skill testing and smoke tests: `references/evals.md`

## Typical Invocations

Vocal song:

```text
Use $suno-songwriter to write a Suno v5.5-ready song about protecting a child from the world.
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
Use $suno-songwriter to improve this Suno v5.5 prompt.
Suggest Style, Excluded Styles, Weirdness, and Style Influence.
The song should be polished dance pop but not EDM or hyperpop.
```

## Installing in Claude Desktop and Codex Desktop

Grab `suno-songwriter.zip` from the [latest release](https://github.com/regiellis/suno-songwriter-agent-skill/releases/latest). The zip contains the skill folder at its root, which is the layout both desktop apps expect.

### Claude Desktop

1. Download `suno-songwriter.zip` from the latest release.
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

After editing the source, re-sync the installed copy:

```bash
cp SKILL.md ~/.agents/skills/suno-songwriter/SKILL.md
rm -rf ~/.agents/skills/suno-songwriter/references
cp -R references ~/.agents/skills/suno-songwriter/references
cp agents/openai.yaml ~/.agents/skills/suno-songwriter/agents/openai.yaml
```

Adapt the destination path for other harnesses.

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

For a fuller manual test set, use `references/evals.md`.

## Development Notes

- Keep `SKILL.md` concise and route deeper guidance to `references/`.
- Prefer adding new focused reference files over making one large reference file.
- Update `references/templates.md` whenever a new reference file is added.
- Update harness metadata under `agents/` without putting harness-specific behavior in `SKILL.md`.
- Sync the installed copy after source changes.
