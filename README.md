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

Build a palette and output its colors:

    python3 palette_builder.py palettes/grey_60.py

Generate a config file from a palette and template:

    python3 build_theme.py --palette palettes/grey_60.py --template vscode-template.json.j2


Development & contributing
--------------------------

_Note: `devel` branch is frequently rebased!_

You're welcome to contribute improvements to the themes. Please just make sure
to only use the colors from the corresponding palette (see above), and avoid
any non-standard formatting styles (bold, italic and underline are fine).

Roadmap for the next few weeks:

1. Settle on styling of basic token types.
1. Design a slightly less minimalistic theme using shades of two colors (apart
   from shades of grey)
1. Use the above to create colorschemes for people with various kinds of color
   blindness.
1. Add support for Vim.
