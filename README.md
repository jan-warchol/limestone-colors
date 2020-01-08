Minimalistic syntax highlighting
--------------------------------

Project goal is to design syntax highlighting with **high readability** (making
important information easy to see, and putting boilerplate in the background)
using a limited set of colors (so that the result doesn't jump on you).

It's currently in early phase of development, no stable version has been
released yet. **See
[`devel`](https://github.com/jan-warchol/monochrome-syntax/tree/devel) branch
for current state of work.**


Features
--------

- moderate **contrast** - very readable but not tiring to the eyes
- precise **lightness** relationships calculated using scientific
  [CIE Lab](http://en.wikipedia.org/wiki/Lab_color_space) color space
- accent colors and formatting styles assigned based on
  **semantic** meaning of tokens
- **accessible** - easy to adapt to people with color vision deficiencies
- fully **parameterized** - easy to generate your own version
  with customized hues or contrast


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
