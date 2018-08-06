phenrsteno
==========

Phonemic and non-rhotic English stenotype theory implemented as a system
for `Plover <https://github.com/openstenoproject/plover>`__.

.. figure:: https://raw.githubusercontent.com/wiki/contrum/phenrsteno/png/layout.png
   :alt: phenrsteno layout

   phenrsteno layout

Check out the
`wiki <https://github.com/contrum/phenrsteno/wiki/Introduction>`__ to
learn more.

Installation
============

1. Install `Plover version
   4.x.x <https://github.com/openstenoproject/plover/releases>`__
2. In the main Plover window, select ``Plugins Manager`` from the
   toolbar

   -  In the plugins list, find and select plover-phenrsteno and click
      ``Install/Update``

3. Quit (Ctrl-q) and re-open Plover
4. In the main Plover window, select ``Configure``

   -  Go to the ``System`` tab
   -  Select ``Phenrsteno`` from the dropdown box
   -  Click ``OK``

Usage
=====

Once installed, you have two options:

-  Use someone else’s dictionaries
-  Create your own

You can `download my dictionaries from this
repository <https://github.com/contrum/phenrsteno/tree/master/json>`__.
``verbatim.json`` is for fingerspelling individual letters.
``vocabulary.json``, ``prefixes.json``, and ``suffixes.json`` are for
transcribing (British) English words.

In Plover, click the big green plus icon to add dictionaries.

Development
===========

To-do:

-  [x] Use unicode IPA symbols for stroke notation

   -  [x] If that works, convert my dictionaries to this new format

-  [ ] Implement prefix keys

   -  [ ] Integrate with `prefix
      support <https://github.com/openstenoproject/plover/issues/974>`__
   -  [ ] Or use a Python dictionary as a workaround

Ideas:

-  Use a corpus of word-to-IPA data to generate a fallback dictionary
   for perfectly phonetic translations
