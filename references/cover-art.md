# Cover Art And Animated Covers

Use this reference when the user wants visuals to go with a Suno track: a still cover image, an animated (looping video) cover, or a prompt for Suno's **Generate Cover Art** / **Animate** tools: text-to-image, text-to-video, or image-to-video.

This is the *visual* side of a release. It is not music; route here only the artwork/video-prompt part of a request and keep the song itself on the normal song/instrumental contract.

## What Suno's Cover/Video Tools Do

Every song Suno generates already has an auto cover-art image embedded in the MP3. On top of that, the song menu offers **Generate Cover Art** and, on an existing cover image, **Animate**. There are three creation paths:

- **Text to Image**: write a prompt, get a still cover image. Most control over the starting frame. Cheapest. Use it first when you want a specific image you'll then animate.
- **Text to Video**: write a prompt, get a short looping animated cover straight from text. Use when there's no artwork yet and you want motion in one step.
- **Image to Video (Animate)**: take an existing cover (the auto one, an uploaded one, or a Text-to-Image result) and add motion: camera drift, light shifts, particle movement. Use when you already have the right image. If the goal is "put this image on the song, then animate it," do the cover step *first*, then Image to Video.

Controls and limits (as of 2026-05: re-check the app):
- **Quality Mode:** Basic or Advanced.
- **Video length:** 5 or 10 seconds, looping.
- **Aspect ratio:** square (1:1) only: compose for a square crop.
- **Prompt length:** roughly **800 characters** per prompt field (the image/scene prompt and the motion prompt are each capped around there). Write tight: lead with subject and composition, then medium/style, palette, lighting, mood; drop hedging adjectives and duplicated cues. If a prompt runs long, cut atmosphere words before you cut the subject.
- **Motion prompt:** optional free-text field guiding movement and atmosphere on video paths (same ~800-char ceiling).
- Returns ~2 variants per generation; preview both, pick one. Video generation can take up to ~5 minutes (Basic / shorter is faster).
- Credit cost scales with mode and length (still image cheapest; Advanced 10s video most expensive). State this only if the user asks about cost.
- No timeline or multi-scene editing: it's a single looping shot, motion guided by prompt only. For a real multi-scene music video edited to picture, that's outside Suno: take the finished track into a dedicated video tool and say so (see below).

## Make The Visual Match The Song

Pull the cover concept from the same place as the Style line: genre, era, mood, palette, the song's central image. The artwork and the music should read as one release:

- Translate the song's **lane** into a visual medium: a grimy boom-bap track might be a scratched photocopy / zine collage; a city-pop song a 1980s airbrushed magazine illustration; a folk record a hand-developed film photo; a hyperpop track a glossy 3D render with chromatic aberration; an OST cue a painterly key-art landscape. Don't default every cover to the same look.
- Echo a concrete image from the lyrics or the brief (the box fan, the empty pool, the bus window) rather than a generic mood board.
- Match energy: a ballad cover is still and spacious; a club track can be saturated and kinetic.
- If there's a persona or album spec, use its stated visual identity / palette and keep it consistent across tracks.

## Writing The Image Prompt (Text to Image / the cover still)

Give it, roughly in this order: **subject and composition → art style / medium → color palette → lighting → mood / era → framing notes.**

- Be concrete about the subject and where it sits in the frame ("a lone figure at the far left, vast empty sky filling the rest"). Square crop: keep the focal point off dead-center if you want room for it to breathe, but assume 1:1.
- Name a medium and style explicitly (35mm film photo, oil painting, risograph print, anime cel, charcoal sketch, vaporwave 3D render, Letraset collage). "Album cover" alone gives the model nothing.
- Specify a small, deliberate color palette and the light (warm low sun, cold fluorescent, single neon sign as the only source).
- **No text in the image**: AI renders type as garbled glitch. Ask for a clean image and add the title/artist later in a real layout tool. If you must, request "space at the top for a title" rather than the title itself.
- **No real artist names, band names, logos, brands, or trademarked characters**: same copyright filter logic as the Style field; describe the *look* (era, scene, technique) instead.
- Avoid the anti-generic word list in the visual too (`neon`, `fire`, `flames`, `shadows`, `echoes`, `broken`, `fading`, `forever`) unless the user asks, and avoid the AI-art clichés: not every cover is a neon-lit rainy city street, a lone astronaut, or a glowing portal.
- One coherent idea beats a pile of elements. A cover is read in a thumbnail.
- Keep it under ~800 characters (the field's limit). One subject, one medium, one palette, one light source: that fits comfortably; a paragraph of stacked atmosphere does not.

## Writing The Motion Prompt (Text to Video / Image to Video)

The motion prompt describes **how the existing (or generated) image moves**, not a new scene. Keep it loop-friendly: the end should land back near the start.

- Pick one or two gentle motions: slow camera push-in or pull-back, lateral drift / parallax between layers, a slow tilt, light flicker, drifting fog or smoke, falling snow / ash / dust, rippling water, a flickering sign, hair or fabric moving in wind, film grain and gate weave.
- Tie the motion to the song's feel: a slow ballad gets a barely-there drift; an uptempo track can pulse, flicker, or push in faster.
- Say it should loop cleanly, with no visible seam. Avoid hard cuts, scene changes, fast action, text, and anything that morphs faces or hands (it goes wrong).
- For Image to Video, also note what should stay locked (the subject's face, the composition) vs what may move (background, light, atmosphere).
- Length: 5s for a tight breathing loop, 10s for a slower drift. Square only.

## Output Shape

Standalone visual request: return:

1. `Cover Concept:` one or two lines tying the image to the song (lane, era, key image, palette).
2. `Image Prompt:` the still-image prompt, ready to paste into Text to Image (or to describe the cover before Image to Video).
3. `Motion Prompt:` the animation prompt, for Text to Video / Image to Video: omit if the user only wants a still.
4. `Settings:` recommended path (Text to Image / Text to Video / Image to Video), Quality Mode, length (5s/10s), and the 1:1 / no-text reminders.
5. `Notes:` only if useful: e.g. "generate the still first, then Animate it"; persona/album visual-consistency notes; that results vary and you may need a few rolls.

When the user asked for a full song *package* and a cover too, append a `Cover Art:` block with `Image Prompt:` / `Motion Prompt:` / `Settings:` after the song's `Checks:` rather than replacing the song contract.

Checks for a visual output:
- Image prompt names a medium/style, palette, lighting, and composition (not just "album cover")
- Image prompt and motion prompt each stay under ~800 characters
- No text, logos, brands, or real artist/character names in the prompt
- Composed for a 1:1 square crop
- Motion prompt describes motion only, loops, and avoids faces/hands morphing and hard cuts
- Visual lane matches the song's genre/era/mood; not an AI-art cliché
- Persona/album visual identity respected when one exists

## Related Suno Visual Features

- **Suno Scenes** is the *reverse* of cover art: you point your phone camera at a photo or video and Suno writes a *song* inspired by it. That's a song-creation entry point (iOS app, "Camera mode"), not artwork generation: handle the resulting song on the normal song contract; this file is only about generating visuals *for* a track.
- **Full music videos** (multi-scene, cut to the track, captions, character consistency) are beyond Suno's looping-cover tool. The workflow is: finish the song in Suno → take the audio (and stems, via Studio) into a dedicated video/edit tool → edit to picture. Tell the user that's the path and that this skill can still write the *song* and a *cover/animated-cover prompt*; it doesn't drive an external video editor.
