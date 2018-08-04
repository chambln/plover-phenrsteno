# phenrsteno

Phonemic and non-rhotic English stenotype theory implemented as a system for [Plover](https://github.com/openstenoproject/plover "GitHub repository for Plover").

![phenrsteno layout](https://raw.githubusercontent.com/wiki/contrum/phenrsteno/png/layout.png)

Check out the [wiki](https://github.com/contrum/phenrsteno/wiki/Introduction) to learn more.

# Installation

1.  Install [Plover version 4.x.x](https://github.com/openstenoproject/plover/releases)
2.  In the main Plover window, select `Plugins Manager` from the toolbar
3.  In the plugins list, find and select plover-phenrsteno and click `Install/Update`
4.  In the main Plover window, select `Configure`, go to the `System` tab, and select `Phenrsteno` from the dropdown box
5.  Click `OK`
6.  Quit (Ctrl-q) and re-open Plover

# Usage

Once installed, you have two options:

  - Use someone else’s dictionaries
  - Create your own

You can [download my dictionaries from this repository](https://github.com/contrum/phenrsteno/tree/master/json). `verbatim.json` is for fingerspelling individual letters. `vocabulary.json`, `prefixes.json`, and `suffixes.json` are for transcribing (British) English words.

In Plover, click the big green plus icon to add dictionaries.

# Development

To-do:

  - [x] Move explanations to the wiki
  - [x] Write installation instructions in README.md
  - [x] Use unicode IPA symbols for stroke notation
      - [ ] If that works, convert my dictionaries to this new format
  - [ ] Implement prefix keys
      - [ ] Integrate with [prefix support](https://github.com/openstenoproject/plover/issues/974)
      - [ ] Or use a Python dictionary as a workaround
