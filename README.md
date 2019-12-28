Minimalistic syntax highlighting
--------------------------------

This is an attempt to design a syntax highlighting theme that uses only shades
of one or two colors, but still maintains high readability. It's currently in
early phase of development, no stable version has been released yet. **See
[`devel`](https://github.com/jan-warchol/monochrome-syntax/tree/devel) branch
for current state of work.**


Features
--------

- moderate contrast: very readable but not tiring to the eyes
- styling rules designed to make important information easy to find
- precise lightness relationships calculated using CIE Lab colorspace
- parameterized: adjust foreground, background or contrast
  and generate all other shades from that


Theme installation
------------------

Instructions are in the directory corresponding to the particular editor, for
example:

- [Visual Studio Code](vscode/)
- [PyCharm](pycharm/)


Theme builder usage
-------------------

First install dependencies:

    pip3 install --user -r requirements.txt

Building a palette:

    python3 palette_builder.py palettes/grey_60.py

Generating a config file from a template:

    python3 build_theme.py -t vscode-template.json.j2 -p palettes/grey_60.py
