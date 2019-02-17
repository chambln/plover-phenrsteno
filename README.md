# [Phenrsteno](https://github.com/chambln/plover-phenrsteno/wiki)

<p align="center"><img src="https://raw.githubusercontent.com/wiki/chambln/plover-phenrsteno/png/layout.png" alt="Stenotype layout for Phenrsteno"/> </p>

Non-rhotic and truly phonemic system for [Plover](https://github.com/openstenoproject/plover). See the [wiki](https://github.com/chambln/plover-phenrsteno/wiki) to learn more.

## Installation

1.  Install [Plover version 4.x.x][plover-releases]
2.  In the main Plover window, select `Plugins Manager` from the toolbar
      - In the plugins list, find and select plover-phenrsteno and click `Install/Update`
3.  Quit (Ctrl-q) and re-open Plover
4.  In the main Plover window, select `Configure`
      - Go to the `System` tab
      - Select `Phenrsteno` from the dropdown box
      - Click `OK`

If you like, you can download [layout-display.json][layout-display-json] to load into Ted Morin's [layout display plugin][plover-layout-display].  

<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/chambln/plover-phenrsteno/png/layout-display.png" alt="Phenrsteno layout display"/>
</p>

## Usage

Once installed, you need to load a dictionary. You can [download my dictionaries from this repository](https://github.com/chambln/plover-phenrsteno/tree/master/yaml). `verbatim.yaml` is for fingerspelling individual letters. `vocabulary.yaml` contains some 6 thousand or so affixes, words and phrases. They're in YAML format, so you'll need to either convert them to JSON or install [plover-yaml-dictionary](plover-yaml-dictionary) from the Plugins Manager.
<!-- TODO: Set up automatic YAML-to-JSON conversion in this repo -->

In Plover, click the big green plus icon to add dictionaries.

## Support and discussion

Come and chat with us in the [Plover Discord group][discord]! Include `@chambln#1483` in your message to (eventually) get my attention.

[plover-releases]: https://github.com/openstenoproject/plover/releases
[layout-display-json]: https://github.com/chambln/plover-phenrsteno/blob/master/layout-display.json
[plover-layout-display]: https://github.com/morinted/plover_layout_display
[plover-yaml-dictionary]: https://github.com/nsmarkop/plover_yaml_dictionary
[discord]: https://discord.gg/0lQde43a6dGmAMp2
