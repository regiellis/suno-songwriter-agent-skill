# Multilingual Songs

Use this reference for non-English lyrics, bilingual lyrics, translation, localization, dialect, script, romanization, and pronunciation notes.

## First Clarify

Ask or infer:
- target language
- dialect/region
- native script, romanization, or both
- original writing vs translation vs singable adaptation
- bilingual/code-switching amount
- genre and regional style
- pronunciation help needed

Examples:
- Spanish (Mexico), native script
- Portuguese (Brazil), native script
- Arabic (Levantine), romanized
- Japanese, kana/kanji plus romaji chorus
- Korean, Hangul with short English post-chorus

## Translation Modes

### Literal Translation

Use only when the user asks to understand meaning. Not ideal for Suno lyrics.

### Singable Adaptation

Default mode for songs. Preserve:
- meaning
- speaker
- emotional arc
- hook function
- section energy

Change:
- word order
- idioms
- line length
- rhyme
- imagery
- repetition

### Bilingual Rewrite

Use deliberate code-switching:
- English title phrase in a K-pop or Latin pop hook
- Spanish verses with English post-chorus
- French chorus with English bridge

Do not accidentally mix dialects or languages.

## Language Notes Field

Use:

```text
Language Notes: Spanish (Mexico), native script, singable adaptation, open-vowel hook, no English code-switching.
```

Or:

```text
Language Notes: Japanese, native script with optional romaji hook; compact J-pop phrasing; English title phrase repeated only in chorus.
```

## Pronunciation

Suno (and AI music models generally) frequently anglicize vowels, mangle tonal languages, stress the wrong syllable, or slur unfamiliar consonant clusters: more so when the vocal model wasn't trained heavily on that language. Plan for it instead of hoping.

Two tools:

1. **In-line phonetic respelling**: rewrite the troublesome word *in the lyric line itself* the way it should sound, when the literal spelling reliably fails. Example: write `cora-SOHN` instead of `corazón` if the model keeps saying "kor-uh-zon". Use it sparingly, only on words that actually break, and note it so the user can revert for a lyric sheet.
2. **`Pronunciation Notes:` block**: keep the lyrics clean and put guidance separately:

```text
Pronunciation Notes: "corazón" = "co-ra-SOHN" (stress the last syllable, open "o"); keep "ll" in "lluvia" soft, not "y".
```

Other levers: choose romanization over native script if the model handles it better for that language; pick simpler near-synonyms over words with hard clusters; lower Weirdness, which helps vocal stability. If quality matters for release, recommend native-speaker review and a re-take or Replace Section on bad lines (see `references/studio-and-iteration.md`).

Do not clutter every line with phonetics unless requested.

## Language Structure Notes

These are heuristics, not grammar guarantees. If publication quality matters, recommend native-speaker review.

| Language / Family | Practical Songwriting Notes |
| --- | --- |
| Spanish | Often needs more syllables than English; use open vowels, natural stress, repeated hooks, and avoid word-for-word English syntax. |
| Portuguese | Brazilian pop can use conversational phrasing and open vowel hooks; watch nasal sounds and regional vocabulary. |
| French | Prioritize smooth vowel flow and elegant phrasing; exact English-style end rhyme may sound forced. |
| Italian | Strong vowels and melodic phrasing work well; keep lines singable and avoid overlong translations. |
| Japanese | Short compact phrases, repetition, and occasional English hook phrases can work; choose native script or romaji intentionally. Anime OP/ED, city pop, and J-rock have their own phrasing norms (see `references/screen-music.md`). |
| Korean | Not only K-pop: also Korean ballad (long emotive lines, big belted chorus), K-hip hop / K-R&B (conversational sung-rap, English ad-libs), Korean indie/folk (gentle, restrained), OST, and trot. K-pop itself uses code-switching, pre-chorus lift, post-chorus tags, dance-break sections, and compact repeated hooks. Ask or infer which lane; phrasing and structure differ a lot between them. Hangul by default; English hook phrases are common but should be intentional. |
| Mandarin | Tone and meaning matter; keep phrases simple, avoid dense metaphors, and consider native-speaker review. |
| Arabic | Specify dialect or Modern Standard Arabic; melisma-friendly vowels and refrain/call-response can fit many styles. |
| Hindi/Urdu | Hooks may lean on repeated title phrases and vowel-rich endings; specify script/romanization and avoid mixing registers accidentally. |
| German | Compound-heavy literal translations can become bulky; simplify ideas and use strong rhythmic stresses. |

## Section Structure

Do not force English section density onto every language.

Use:
- shorter lines for languages with dense syllable flow
- repeated title phrases when natural
- fewer details in chorus
- more conversational phrasing in verses
- native idioms instead of literal English metaphors

## Style Field For Multilingual Songs

Mention target-language vocal:

```text
Latin pop ballad, Spanish male vocal, 86 BPM, acoustic guitar, soft percussion, warm romantic production
```

For bilingual songs:

```text
K-pop inspired dance pop, Korean and English female vocals, 118 BPM, glossy synths, punchy drums, chant post-chorus
```

Use `Excluded Styles` for unwanted language drift:

```text
Excluded Styles: English verses, rap vocals, EDM drop
```

## Checks

- Target language and dialect are stated.
- Native script or romanization choice is stated.
- Translation is singable, not word-for-word, unless requested.
- Hook works naturally in the target language.
- English code-switching is intentional.
- Cultural references and slang are plausible.
- Native-speaker review is recommended when confidence is limited.
