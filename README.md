# [Phenrsteno](https://github.com/contrum/plover-phenrsteno/wiki)

![Stenotype layout for Phenrsteno][layout]

Non-rhotic and purely phonemic system for [Plover](https://github.com/openstenoproject/plover). See the [wiki](https://github.com/contrum/plover-phenrsteno/wiki) to learn more.

## Installation

1.  Install [Plover version 4.x.x][plover-releases]
2.  In the main Plover window, select `Plugins Manager` from the toolbar
      - In the plugins list, find and select plover-phenrsteno and click `Install/Update`
3.  Quit (Ctrl-q) and re-open Plover
4.  In the main Plover window, select `Configure`
      - Go to the `System` tab
      - Select `Phenrsteno` from the dropdown box
      - Click `OK`
      
![Phenrsteno layout display][layout-display-png]
      
If you like, you can download [layout-display.json][layout-display-json] to load into Ted Morin's [layout display plugin][plover-layout-display].

## Usage

Once installed, you need to load a dictionary. You can [download my dictionaries from this repository](https://github.com/contrum/plover-phenrsteno/tree/master/yaml). `verbatim.yaml` is for fingerspelling individual letters. `vocabulary.yaml` contains some 10 thousand or so words and phrases. They're in YAML format, so you'll need to either convert them to JSON or install [plover-yaml-dictionary](plover-yaml-dictionary) from the Plugins Manager.
<!-- TODO: Set up automatic YAML-to-JSON conversion in this repo -->

In Plover, click the big green plus icon to add dictionaries.

[layout]: https://raw.githubusercontent.com/wiki/contrum/plover-phenrsteno/png/layout.png
[plover-releases]: https://github.com/openstenoproject/plover/releases
[layout-display-json]: https://github.com/contrum/plover-phenrsteno/blob/master/layout-display.json
[layout-display-png]: https://raw.githubusercontent.com/wiki/contrum/plover-phenrsteno/png/layout-display.png
[plover-layout-display]: https://github.com/morinted/plover_layout_display
[plover-yaml-dictionary]: https://github.com/nsmarkop/plover_yaml_dictionary
