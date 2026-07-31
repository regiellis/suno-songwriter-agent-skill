# Remix And Style Match

Use this reference when the user wants to (a) **remix or flip** an existing lyric/song into a new version, (b) write **in the style of** a named artist or song, or (c) **analyze** a set of lyrics for their style and then get original lyrics in that vein. The common thread: there is a source, and the output must capture its *approach* without reproducing its *expression*.

Related: `SKILL.md` § Revision Mode, `references/songwriting-craft.md` § Reference Lyrics Transformation, `references/suno-v55-controls.md` § No Artist Names.

## Hard Rule: Style Yes, Expression No

Style, cadence, rhyme strategy, song structure, subject matter, and genre are not protected: you can freely write *like* an artist. Specific lyrics, hooks, distinctive turns of phrase, and the actual recording are protected. So:

- Never reproduce, closely paraphrase, or continue copyrighted lyrics. Do not quote them back, even "as an example."
- Do not put the artist's name in `Style:` (it can also trip Suno's copyright filter: see `references/suno-v55-controls.md` § No Artist Names). Translate the sound into era/scene/production instead.
- Pick a *fresh subject* so the result is plainly its own song, not a re-skin of one specific track.
- If the user supplies lyrics they own (their own work, public domain, properly licensed), remixing those closely is fine: confirm ownership first if it's ambiguous.
- If the user actually wants the real lyrics of a copyrighted song, or a near-verbatim continuation, decline and offer a style-match instead.

## Mode A: Lyric Remix / Flip

The user has a lyric (theirs, or supplied as raw material) and wants a transformed version: re-genre, re-structure, condense or expand, modernize, change point of view, translate, turn a verse into a hook, make it darker/funnier/bigger, etc. This is Revision Mode with the transformation dial turned up.

Steps:

1. **Confirm what to keep vs change.** Usually keep: the concept/premise, emotional arc, maybe one motif or the title idea. Change: lines, images, hook wording, structure, register: whatever the remix calls for. State this back to the user in one line before rewriting (e.g. `Keeping: the "calling at 2am" premise and the regret arc. Changing: genre to drill, structure to verse/hook, all lines and images.`).
2. **Apply the transformation.** New genre → new `Style:` line and new phrasing density to match; new structure → re-section; new POV → rewrite consistently; translation → see `references/multilingual.md`.
3. **Fix craft last** (meter, hook strength, anti-generic edits) once the new direction is set.
4. **Update title and style** if the originals are weak; label the changes.

Output: standard contract (`Title`, `Style`, `Excluded Styles`, `Lyrics`, ...), plus a one-line `Remix Notes:` stating what was kept and what was changed.

## Mode B: Style Match ("in the style of X")

The user wants original lyrics (and a fitting Style line) that *feel like* a given artist or song without being one.

### Step 1. Build the style fingerprint

Extract these dimensions, from the supplied lyrics if any, from general knowledge of the artist, and from search if the harness has it (see below):

- **Cadence & flow:** syllables per bar/line, where the stresses land, triplet vs straight feel, laid-back-behind-the-beat vs on-top, end-stopped vs enjambed lines, pause/breath habits.
- **Rhyme:** scheme (couplets, alternating, none), internal-rhyme density, multisyllabic/compound rhymes, perfect vs slant, where in the bar rhymes land, chain rhyme.
- **Line & section shape:** line length, verse/section length, hook construction (one-line vs multi-line, repeated title), ad-lib and backing-phrase habits, intro/outro patterns.
- **Diction & register:** vocabulary level, slang and its era/region, recurring imagery domains (places, objects, references: e.g. a conscious-rap voice might draw on neighborhood detail, jazz/soul lineage, spiritual language, dense wordplay), humor vs gravity, profanity level.
- **Subject matter & POV:** typical themes, first vs third person, narrator stance (witness, participant, preacher, trickster), how political/personal/abstract.
- **Delivery & structure:** verse-heavy vs hook-heavy, spoken interludes, call-and-response, sung-rap vs straight rap vs melodic, dynamic shifts.
- **Sonic lane (feeds `Style:`):** era, region/scene, production character, BPM range, beat/instrumentation signature, vocal texture.

### Step 2. Use search if available

If the harness has web/search access, look the artist up to sharpen the fingerprint: era and scene, signature techniques, frequent collaborators/producers, recurring themes, how critics describe the flow. **Do not pull verbatim lyrics into the working notes or the output**: you want the *description* of the style, not the lines. If no search is available, build the fingerprint from training knowledge and say so plainly: `Modeled on general knowledge of [artist]'s style; details may be approximate.`

### Step 3. Generate original work

- Pick a fresh subject (the user's topic, or invent one that suits the voice) so it reads as its own song.
- Write original lyrics that hit the fingerprint: match the cadence, rhyme density, line shape, diction register, and thematic territory; do not match any actual line.
- Write a `Style:` line that evokes the sonic lane (era/scene/production/BPM/vocal) without naming the artist (`references/suno-v55-controls.md` § No Artist Names).
- If the cadence needs help surviving generation, add delivery cues in `Suno v5.5 Notes:` (e.g. `melodic rap, conversational pocket behind the beat, heavy internal rhyme, half-time feel`) and consider section-tag descriptors (`references/song-structure.md`).

### Step 4. Output

Standard contract plus a `Style Reference:` line that names what was modeled and states the boundary, e.g.:

```text
Style Reference: late-90s NYC conscious hip hop - dense internal rhyme, jazz-inflected boom-bap production, witness-narrator POV. Modeled on the style and cadence of <artist>, not on any of their songs; all lyrics original.
```

## Mode C: Lyric-Style Analysis Only

If the user just pastes lyrics and asks "what's the style here" / "analyze the cadence" / "what makes these tick", return the fingerprint as a structured readout (Cadence / Rhyme / Line & section shape / Diction & register / Subject & POV / Delivery / Sonic lane) with a one-line summary, and offer to write original lyrics matching it (Mode B). Do not quote long spans of the source back; reference it by description.

## Slider And Field Notes

- Style-match work usually wants higher Style Influence (the Style line is doing precise sonic work) and moderate Weirdness (you want the genre signal clean); raise Weirdness only if the artist's style is itself experimental. See `references/suno-v55-controls.md`.
- Keep negative direction in `Excluded Styles:` (e.g. excluding a modern trap sheen if you're matching a 90s boom-bap voice).

## Checks (in addition to the usual ones)

- No reproduced or closely paraphrased lines from the source; output expression is original.
- Artist name is **not** in `Style:`; the sound is described via era/scene/production.
- Fingerprint match: cadence, rhyme density, line/section shape, diction register, and themes track the model.
- Fresh subject: the result is its own song, not a re-skin of one specific track.
- For remixes: `Remix Notes:` states what was kept and what was changed; for style-match: `Style Reference:` states what was modeled and the boundary.
- If the source ownership was unclear, ownership was confirmed before any close rework.
