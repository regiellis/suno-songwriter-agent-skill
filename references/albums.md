# Albums

Use this reference to plan and maintain a cohesive **album or EP** (a set of songs that sound like one body of work) captured in a Markdown file kept in the user's project. Any request to write or revise a track on the album loads the file and stays in cohesion.

An album may be tied to a **persona** (`references/personas.md`); if so, link it and the persona's vocals, cadence, and lyrical fingerprint carry across every track.

## When To Use

Triggers: "plan an album / EP / mixtape", "create an album concept", "I want a cohesive set of songs about <X>", "add a track to my album <name>", "write track 4 of <album>", "make a tracklist for...", "keep these songs consistent as an album", "sequence these into a record".

## Where The File Lives

Write the album to `albums/<album-slug>.md` relative to the user's working directory; create `albums/` if it doesn't exist. Per-song outputs go wherever the user keeps songs; the album file links them by relative path. Don't overwrite an existing album file silently: confirm or use a new slug. An optional `albums/README.md` index is fine, not required. (These files go in the user's project, never in the skill repo.)

## Album File Schema

```markdown
---
title: <album / EP title>
slug: <kebab-case>
type: album
format: album | EP | mixtape | single + B-sides
persona: <persona slug if linked, else none>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
status: planning | in-progress | complete
---

# <Album Title>

## Concept
<The throughline: theme, narrative or emotional arc, mood, era, what the record is "about." 2-5 sentences. This is what makes it an album and not a playlist.>

## Sonic Palette (album-wide)
- Genre / lane(s): <the shared sound; one primary, optional secondary>
- Production aesthetic: <the mix / recording character that unifies the record>
- BPM range: <the spread the album lives in>
- Core instrumentation: <the recurring sonic bed>
- Vocals: <from the linked persona, or stated here if no persona>
- Reusable Style kernel: `<~120-char Style fragment every track starts from>`

## Cohesion Rules
**Constant across all tracks:** <vocal identity; production aesthetic; recurring motifs / sounds; lyrical callbacks; any key or tempo relationships; interludes / segues; intro & outro framing>
**Allowed to vary:** <tempo within the band; one or two "left-turn" tracks; feature vocalists on specific tracks; an acoustic / stripped track; etc.>
<This is 80/20 applied to a tracklist - mostly one coherent identity, with deliberate variation. See references/eighty-twenty.md.>

## Recurring Elements
<Motifs (melodic / rhythmic), lyrical phrases or images that recur as callbacks, characters, sonic signatures, a sample or texture that threads through. List them and note which tracks use them.>

## Tracklist
| # | Working Title | Role | Tempo / Energy | Theme / Angle | Status | Output file |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | | opener | | | planned | |
| 2 | | | | | planned | |
| … | | | | | | |
| N | | closer | | | planned | |

(Roles: opener, single, deep cut, interlude, skit, feature track, stripped / acoustic, climax, closer, hidden track, etc.)

## Sequencing Notes
<Energy curve across the record; where the singles sit; pacing; segues and crossfades; side A / side B if relevant; how the opener sets it up and the closer lands it.>

## Excluded Styles (album-wide)
<genres, instruments, moods, production traits the album never uses>

## Suno Defaults
- Weirdness: <range>
- Style Influence: <range>
- Voices / Custom Model: <from persona or stated>
- Notes: <standing Suno guidance for the project>

## Changelog
| Date | Change |
| --- | --- |
| | |
```

## Creating An Album

1. Get the concept: theme / arc / mood / era, the format (album / EP / mixtape), and whether it's tied to a persona. If a persona is named, read `personas/<slug>.md` and pull vocals, cadence, fingerprint, and palette from it.
2. Define the sonic palette and the cohesion rules: what's constant, what's allowed to vary. Keep the constants tight; that's what makes it a record.
3. Draft a tracklist: number of tracks, each with a role, a working title, an energy level, and a theme / angle. Sequence for an energy curve. Mark everything `planned`.
4. Note recurring elements (motifs, lyrical callbacks) to thread through, and which tracks carry them.
5. Write `albums/<album-slug>.md` (creating `albums/` if needed). Don't overwrite without confirmation.
6. Tell the user the path and summarize the concept + tracklist.

## Writing A Track For An Album

When the user asks for a specific track (by number, title, or "next track"):
1. Read `albums/<album-slug>.md` (and the linked persona file, if any).
2. Build the track to fill its slot: the album's Style kernel + the track's tempo / energy / theme; honor the cohesion rules (constants) and use any recurring elements assigned to it.
3. Keep the persona's vocals / cadence / fingerprint if linked; otherwise the album-level vocals.
4. Apply the album's Suno defaults.
5. After producing the song, update the tracklist row (title finalized, status → drafted / done, output file path) and the Changelog. Update the persona's Song Log too if a persona is linked.
6. If the track surfaces a strong new recurring element, offer to add it to the album file and consider it for other tracks.

## Output Contract Additions

When a song is generated as part of an album, add an `Album:` line near the top of the output (album title, track #, file path), and in `Checks:` add:
- track fits its assigned role and energy in the sequence
- album cohesion rules respected (constants held; variation only where allowed)
- recurring elements used as planned
- sonic palette / excluded styles consistent with the album
- persona consistency if linked (defer to the persona checks)

## Checks (when creating/updating an album)

- Concept is a real throughline, not just "songs by the same artist."
- Cohesion rules clearly separate what's constant from what may vary.
- Tracklist has roles and an intentional energy curve, not a flat list.
- Reusable Style kernel ≤ ~120 chars, room for per-track additions.
- Album-wide excluded styles don't contradict the palette.
- A linked persona file actually exists; vocals / fingerprint pulled from it rather than re-invented.
- File written to `albums/<album-slug>.md`; existing file not overwritten without confirmation.
