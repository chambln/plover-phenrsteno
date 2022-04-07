# Phenrsteno

![](contrib/layout.png "Stenotype layout for Phenrsteno")

Non-rhotic phonemic steno theory, dictionary and plugin for [Plover].

## Installation

1.  Install [Plover 4.x.x]
2.  In the main Plover window, select `Plugins Manager` from the toolbar
3.  In the plugins list, find and select plover-phenrsteno and click `Install/Update`
4.  Quit (Ctrl-q) and re-open Plover
5.  In the main Plover window, select `Configure`, go to the `System`
    tab, select `Phenrsteno` from the dropdown box and click `OK`
6.  Optionally download [layout-display.json] and load it into Ted Morin's [layout display plugin].

![](contrib/layout-display.png "Phenrsteno layout display")

## Usage

Once installed, you need to load a dictionary. You can download the
dictionaries from this repository.

-   `vocabulary.json` contains some 6 thousand or so affixes, words and phrases
-   `verbatim.json` is for fingerspelling individual letters

Once you're set up, check out the [wiki] and start writing with Phenrsteno!

## To-do / wishlist

  - [ ] Support for popular steno machines
  - [ ] Have the plugin provide this repo's dictionaries to the user on installation
  - [ ] Implement prefix keys with [prefix support] or using a Python dictionary as a workaround
  - [ ] Use a corpus of corresponding word-IPA data to generate a fallback dictionary for exact phonetic translations
  - [ ] Create a 2-key combo table like [this one](https://redd.it/78ei3n)

[Plover]: https://github.com/openstenoproject/plover
[Plover 4.x.x]: https://github.com/openstenoproject/plover/releases
[layout-display.json]: contrib/layout-display.json
[layout display plugin]: https://github.com/morinted/plover_layout_display
[wiki]: https://github.com/chambln/plover-phenrsteno/wiki
[prefix support]: https://github.com/openstenoproject/plover/issues/974

