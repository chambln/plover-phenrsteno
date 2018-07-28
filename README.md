# phenrsteno
Phonemic and non-rhotic English stenotype system for [Plover][1]. The layout is optimised for RP and Midlands stenographers.

![phenrsteno layout](./doc/layout.png)

# Chorded phonemes
This sections describes how you can transcribe phonemes other than those printed on the keys.

## Vowels
Diphthongs like [aɪ] and [eɪ] arise naturally from the layout. Strokes for other vowel sounds are in the table below.

| Vowel | Stroke |
| ----- | -------|
| [ɒ]   | `ae`   |
| [iː]  | `ɪʊ`   |
| [uː]  | `eʊ`   |
| [ɑː]  | `aɪʊ`  |
| [ɔː]  | `aeɪʊ` |
| [əʊ]  | `aeʊ`  |


## Consonants

Phonemes under the left hand:

| Initial consonant | Left-hand stroke |
| ----------------- | ---------------- |
| [f]               | `sb`             |
| [v]               | `sd`             |
| [k]               | `pb`             |
| [l]               | `td`             |
| [j]               | `wr`             |
| [tʃ]              | `twr`            |
| [dʒ]              | `dwr`            |
| [ʃ]               | `swr`            |
| [g]               | `pt`             |
| [h]               | `ptw`            |
| [n]               | `bd`             |
| [m]               | `bdr`            |
| [θ]               | `bt`             |

Phonemes under the right hand:

| Final consonant | Right-hand stroke |
| --------------- | ----------------- |
| [p]             | `ft`              |
| [b]             | `ftʃ`             |
| [k]             | `td`              |
| [θ]             | `tdʃ`             |
| [ŋ]             | `ng`              |
| [m]             | `ftnd`            |

# Development
To-do:

- [ ] Integrate with [Plover's plugin manager][2]
- [ ] Include JSON dictionaries for
  - [ ] vocabulary
  - [ ] affixes
  - [ ] plover commands


[1]: https://github.com/openstenoproject/plover "Plover GitHub repository"
[2]: https://github.com/benoit-pierre/plover_plugins_manager "Plover Plugin Manager GitHub repository"
