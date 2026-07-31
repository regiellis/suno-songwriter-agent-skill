# Genre Fusion And Multi-Genre Songs

Use this reference when a request involves more than one genre in a single deliverable. Route by what the user actually wants: the three cases produce different outputs:

1. **Fusion (blend):** one song, one hybrid sound throughout → one carefully-built Style line.
2. **Genre switch (shift):** one song that changes genre between sections → Style narrates the arc, section tags mark the moments.
3. **Genre versions (variants):** the same song delivered in several genre treatments → one lyric, multiple packages.

Pair with `references/genre-palettes.md` (per-lane menus), `references/rule-of-3.md` (arrangement discipline), and `references/suno-v55-controls.md` (Style formatting, sliders).

## Fusion: One Hybrid Sound

The core move is **anchor + accent**, never 50/50. A Style line that names two genres without assigning roles averages into mush.

- The **anchor** genre owns the rhythm section, the tempo, and the structure.
- The **accent** genre contributes 2-3 signature elements: an instrument, a vocal identity, or a production texture: pulled from its `genre-palettes.md` row.
- Take BPM from the anchor's band. If the two genres' BPM bands do not overlap, the anchor wins outright, or use a half-time feel to let both readings coexist.
- Keep the line under 200 characters and keep Rule-of-3 discipline: a fusion earns at most one extra descriptor, not a second full palette.
- If the pairing already has an established name (jazz fusion, country trap, folktronica, latin drill, electro swing), lead with that name plus specifics rather than describing the pairing from scratch. Suno resolves known lanes better than invented hyphenations.
- Use `Excluded Styles:` to block the drift the fusion invites: name the generic middle the blend could collapse into (e.g. a folk × house blend drifting to generic tropical EDM).
- Sliders: fusions usually want Weirdness one notch above the anchor lane's normal range and Style Influence kept high so the written blend holds (see the fusion row in `references/suno-v55-controls.md`).

Style line shape:

```text
[anchor genre] with [accent element(s) from second genre], [mood], [anchor BPM], [vocal identity], [production texture]
```

Examples (pick fresh pairings per request: do not reuse these):

- `bluegrass drum and bass, breathless and bright, 174 BPM, fast breakbeats and deep sub under banjo rolls and fiddle, clear female lead, wide energetic mix`
- `cumbia surf rock, salty and playful, 102 BPM, twangy reverb guitar over güira and congas, relaxed male group vocals, dry garage mix`
- `qawwali-inspired synthpop, devotional and euphoric, 118 BPM, tabla and handclaps under analog arpeggios, soaring call-and-response vocals, wide glossy mix`

## Genre Switch: Changing Mid-Song

Less reliable than fusion. Suno may smooth the switch away. Stack the odds:

- **State the arc in `Style:`** in natural language: `starts as spare piano ballad, flips to double-time house on each chorus`. The Style field is the persistent instruction; the switch must live there, not only in tags.
- **Mark the moments in the lyrics** with section-tag descriptors or a cue tag: `[Chorus - double-time house flip]`, `[Verse 2 - halftime swing feel]`, `[Beat Switch]`. This is the one sanctioned exception to "production direction belongs in Style, not tags" (`references/suno-meta-tags.md`): the Style line narrates the journey, the tag pins where it turns.
- **Hold one or two constants across the switch** (the vocalist, the key, a repeated motif or hook phrase) so it reads as one song, not two stitched clips.
- **One switch per song** is the sweet spot; two maximum (e.g. out and back). More reads as chaos and usually gets ignored.
- If generations keep averaging the two sounds instead of switching, split the song: generate part one, then Extend with the second genre's direction, or use Replace Section on the flip point (`references/studio-and-iteration.md`). Note the approach in `Suno v5.5 Notes:`.

## Genre Versions: One Song, Several Treatments

For "give me this as country and as drill" style requests:

- Keep `Title:` and the lyric's content identical; write a fresh `Style:`, `Excluded Styles:`, and `Slider Suggestions:` per version.
- Deliver each version as its own labeled package (`### Version A - modern country`, `### Version B - drill`) and state in one line what is constant across them.
- **Re-check singability per genre:** A lyric metered for a 74 BPM ballad will not scan over 140 BPM drill. Adjust line lengths, syllable density, and section tags per version, and say what changed: do not silently rewrite the song.
- Two or three versions is the useful range; more than that, ask which lanes matter.
- If the user already has a generated take they like, restyling that take is Cover/Remix territory (`references/studio-and-iteration.md`), not a fresh multi-version package.

## Checks Additions

When any of these modes is used, add the matching items to `Checks:`:

- anchor and accent roles assigned; BPM owned by one genre
- Excluded Styles blocks the blend's generic middle
- switch stated in both Style and a section tag; constants named across the switch
- each version's lyric still scans at that version's tempo; changes between versions listed
