Design principles
-----------------

Token types have shades assigned based on importance, length and frequency:

- less important elements should be dimmer:
    - comments should be clearly secondary to the code
    - boilerplate/metadata, for example variable types
- rare and important tokens (e.g. exceptions) shoud be strong, drawing
  attention
- "heading-like" elements that structure the code (e.g. class/function names)
  should be easy to spot from distance, to make navigation easy
- special/language-defined words should have some formatting distinguishing
  them from user-defined values
    - e.g. if you make a typo (like `false` instead of `False` in Python) it
      should be clear from the formatting
- separating tokens using different lightness of punctuation (example)

example: when you look at function call foo(bar=qux), you are more interested in “qux” than “bar”.
when looking at variable definition, you’re more interested in name than type
