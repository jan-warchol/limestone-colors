Limestone syntax highlighting
-----------------------------

_Limestone_ is a family of color themes for IDEs and text editors.

![limestone logo](https://i.imgur.com/V6rZL00.png)

Project goal is to design the **most readable** syntax highlighting - convey as
much information about the tokens as possible (thus enhancing the understanding
of the code), but do it in a clear, organized way, without overwhelming the
reader with too many intense colors. Based on years of experience gained
developing selenized, it offers unmatched readability.

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

Read more in the [design document](DESIGN.md).


The themes (with screenshots)
-----------------------------

The limestone family consists of several themes with different amount or color used:

- monochrome version: the absolute minimum. You'll be surprised how much
  information can be conveyed just by varying lightness and font styles
  ([see screenshots](screenshots.md#limestone-monochrome)).

- two-color version: moderately minimalistic version using shades of two accent
  colors in addition to the base monochromatic color scale ([see
  screenshots](screenshots.md#limestone-two-color)).

- "full color" version: using shades of 8 accent colors. Not ready yet, I want
  to reach the state in which the first two are mature before working on this
  one (as working with strong constraints makes me think hard about the
  decisions).


Installation
------------

Instructions are in the directory corresponding to the particular editor, for
example:

- [Visual Studio Code](vscode/)
- [PyCharm](pycharm/)


Supported languages
-------------------

Limestone comes with basic styling rules for all common token types (comments,
keywords, strings etc.), which should be sufficient for **most languages**.
However, a lot depends on the editor and the grammar it's using. There are more
detailed styling rules for Python and JavaScript, and in the near future I plan
to add support for Go, Ruby and Java.


Development & contributing
--------------------------

_Note: `devel` branch is frequently rebased!_

You'd like to suggest changes in styling or generate a customized version of
the theme? Great! See [Contributing.md](CONTRIBUTING.md).

Roadmap for the near future:

1. Settle on styling of basic token types.
1. Create theme variants for people with various kinds of color blindness.
1. Add support for Vim.
