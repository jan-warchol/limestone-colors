Limestone syntax highlighting
-----------------------------

_Limestone_ is a family of color themes for IDEs and text editors.

![limestone logo](https://i.imgur.com/V6rZL00.png)

Project goal is to design syntax highlighting with **high readability** (making
important information easy to see, and putting boilerplate in the background)
using a limited set of colors (so that the result doesn't jump on you).

It's currently in active development, approaching beta release. **See
[`devel`](https://github.com/jan-warchol/monochrome-syntax/tree/devel) branch
for current state of work.**


Features
--------

- moderate **contrast** - very readable but not tiring to the eyes
- colors and formatting styles assigned to tokens based on
  their semantic **meaning**
- precise lightness relationships calculated using **scientific**
  [CIE Lab](http://en.wikipedia.org/wiki/Lab_color_space) color space
- **accessible** - easy to adapt to people with color vision deficiencies
- fully **parameterized** - easy to generate your own version
  with customized hues or contrast


Installation
------------

Instructions are in the directory corresponding to the particular editor, for
example:

- [Visual Studio Code](vscode/)
- [PyCharm](pycharm/)


Development & contributing
--------------------------

_Note: `devel` branch is frequently rebased!_

You'd like to suggest changes in styling or generate a customized version of
the theme? Great! See [Contributing.md](CONTRIBUTING.md).

Roadmap for the near future:

1. Settle on styling of basic token types.
1. Create theme variants for people with various kinds of color blindness.
1. Add support for Vim.
