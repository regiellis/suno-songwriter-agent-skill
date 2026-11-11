# Harmony And Melody

Use when a hook lacks shape, a chorus needs contrast, or a brief specifies chords, mode, key, or vocal range. These are composition choices, not verified Suno commands. Describe the audible result in Style; keep note-level plans outside Lyrics. Use only the detail that serves the song.

## Choose The Harmonic Motion

Choose a tonal center and rate of chord change before adding chord colors. A chord per bar and a chord held for four bars create different motion at the same tempo. More chords do not necessarily create more lift.

| Need | Musical Choice | Prompt Translation |
| --- | --- | --- |
| Grounded, hypnotic verse | Tonic pedal or one-chord vamp | `steady tonic bass beneath shifting upper voicings` |
| Strong arrival | Dominant-to-tonic cadence in a tonal phrase | `chorus resolves firmly onto the home chord` |
| Open-ended refrain | Delay the tonic or end on dominant | `refrain hangs unresolved before the next verse` |
| Dark verse, brighter chorus | Change chord emphasis, register, or voicing | `minor-centered verse, brighter chorus voicings with a rising melody` |
| Tension without louder drums | Faster harmonic rhythm or a suspended tone | `chords change twice as often in the build, suspended melody resolves at the hook` |
| Softer final return | Keep harmony, reduce density and register | `final refrain over sparse low voicings and a descending lead` |

Roman numerals describe chords relative to a tonal center; uppercase means major, lowercase minor. In C major, I-V-vi-IV is C-G-Am-F. In A minor, i-VI-III-VII is Am-F-C-G. These share a chord collection but can establish different centers through emphasis, bass, melody, and cadences. A loop alone does not prove a key or mood.

Use an explicit convention for modal degrees: relative to the parallel major scale, A minor's F is bVI and G is bVII. Do not mix `VI` and `bVI` conventions without explaining the reference scale. Prefer chord names when ambiguity matters.

## Color Without A Chord Catalog

- Dorian: minor third with a natural sixth. In D, a Dm-G vamp can expose B natural. Request that color in the melody or chord voicing; the word `Dorian` alone may not establish it.
- Mixolydian: major third with a lowered seventh. In D, D-C-G can support that color when D remains home.
- Borrowed minor iv in a major key: C-F-Fm-C gives the inner motion A-Ab-G. Use for a specific bittersweet turn, not as an automatic sad-song recipe.
- Secondary dominant: in C major, D7-G-C temporarily points toward G before returning home. Request a brief harmonic push if detailed chord instructions distract from the song.
- Suspensions, add9 chords, sevenths, and inversions change color and voice leading. Choose one useful color rather than stacking every extension in the prompt.

Modes do not carry fixed emotions, and functional major/minor harmony is not a universal framework. For a tradition built around a different tuning, modal system, or rhythmic practice, use its own terms when understood. Research unfamiliar details rather than translating everything into Western chord loops.

## Design A Singable Motif

Choose one recognizable rhythmic cell and a short contour. Repeat enough to establish identity; vary one feature at a meaningful section turn.

| Problem | Revision |
| --- | --- |
| Hook is forgettable | Repeat its opening rhythm; change only the final note or phrase ending |
| Chorus sounds like another verse | Use a higher starting register, longer title note, or wider leap followed by stepwise return |
| Melody feels busy | Reduce note changes and leave a rest after the central phrase |
| Every line feels final | Alternate an open phrase ending with a more settled answer |
| Singer sounds strained | Lower the repeated working register before changing the whole key |
| Words lose their meaning | Align important syllables with accents or sustained notes; keep weak syllables lighter |

Range is the lowest-to-highest span; tessitura is where most of the part sits. A single reachable high note does not make a chorus comfortable if every phrase stays there. Do not infer a person's range from gender or voice labels. If the user gives a range, keep the repeated hook inside it and treat generated compliance as pending audition.

Keep a lyric's natural word stress unless intentional displacement serves the groove. A pickup can put a weak syllable before the beat and let the meaningful syllable land strongly. Melisma fits sustained vowels better than a cluster of consonants; shorten wording before stretching spelling into unreadable syllables.

## Worked Translation

Brief: a restrained folk-rock verse with a chorus that lifts without getting louder.

Plan: hold verse chords for two bars, keep the melody near its middle register, then change chords each bar in the chorus and sustain the title above the verse's contour. Keep percussion at the same intensity.

Style:

```text
folk rock, steady brushed backbeat, fingerpicked guitar; close conversational verses, chorus chords turn each bar beneath a higher sustained title phrase, restrained dynamics
```

This communicates contrast without claiming exact notes. If a fixed melody, chord sequence, or key is essential, provide a recorded or MIDI reference through a supported surface and verify the audio. Text cannot certify those details. See `studio-and-iteration.md` for the editing path.
