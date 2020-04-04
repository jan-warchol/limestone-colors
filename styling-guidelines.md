Syntax highlighting design principles
-------------------------------------

Here are some general guidelines for deciding which types of tokens should be
colored with which color:

- overall effect shouldn't be overwhelming - don't color everything, strive for
  harmony (compare with [this monokai
  example](https://i.imgur.com/ATVTHr6.png), which has colors all over the
  place)
- contrasting colors shouldn't appear next to each other too often
- structurally most important elements should be most visible
- less important content should be visually "in the background"
- short tokens (and punctuation, if it's to be colored) should preferably use
  stronger colors 
- long tokens should use "softer" colors to avoid making the result too
  aggressive
- rare tokens should use a color that draws attention and is not used by some
  common tokens
- try to leverage common color associations wherever possible (e.g. red ->
  problem, green -> no problem)
- warm colors (orange, yellow) are best for tokens associated with action
- cold colors (cyan, blue) are best for things that don't change
- [non-spectral colors](https://en.wikipedia.org/wiki/Spectral_color) (purple,
  magenta) are best for things with special meaning/behavior

This means that, for example:

- comments must be gray, so that they fade into background (unlike many schemes
  in which comments are green and clutter the view)
- function and class definitions must be clearly visible from distance (perhaps
  bright bold foreground)
- orange is a good color for numbers
- exceptions should probably be bold and they must not be green
- preprocessor, interpolation, macros and other meta-processing things "feel"
  magenta
- cyan is a good color for `CONSTANTS`
- should boilerplate be blue? or gray? or not colored at all?


