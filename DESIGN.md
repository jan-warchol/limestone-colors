Design principles
=================

We all know that reading code without syntax highlighting is very cumbersome.
However, are all color themes equally helpful? Is the choice of colors just a
matter of personal taste? Maybe there is a combination of colors that works
better than others?

![Selection of color themes](https://i.imgur.com/bVJMIpm.png)

This is the aim of Limestone project - to develop a theme that **maximizes
readability.** With the aid of scientific tools like [CIE
Lab](http://en.wikipedia.org/wiki/Lab_color_space) color space it makes
understanding the code as easy as possible through conscious use of font
styles, lightness and colors (keeping in mind things like [perceptual
uniformity](https://vis4.net/blog/posts/avoid-equidistant-hsv-colors/) and
[Helmholtz–Kohlrausch
effect](https://en.wikipedia.org/wiki/Helmholtz%E2%80%93Kohlrausch_effect)).

Use of lightness
----------------

In general, lightness should reflect the _importance_ of tokens. Making less
important elements dimmer puts them in the background, so that the reader can
easily focus on the ones that matter most.

![Lightness example](https://i.imgur.com/wB8ZKB8.png)

1.  comments and docstrings are secondary to everything else
2.  boilerplate such as self/this shouldn’t attract attention
3.  bright punctuation aids in dividing chained constructs into individual
    tokens

Use of colors
-------------

Color is great for marking different _kinds_ of tokens. Since color naturally
draws attention, it should be avoided for “background” elements such as
comments, and should be used sparingly.

![Color example](https://i.imgur.com/libyrgz.png)

1.  keywords and built-ins use varying tones of yellow, and stand in
    opposition to user-defined symbols which are generally grey
2.  coloring operators helps in differentiating values and actions
3.  using tones of blue for all literals makes spotting magic values easy
4.  longer tokens (e.g. strings) should use less saturated than shorter ones
    (e.g. numbers)

Use of font styles
------------------

Consistent use of styling can help in showing what is the _function_ of
particular elements.

![Font styles example](https://i.imgur.com/xOpf1MG.png)

1.  use italic for “annotation-like” elements that supplement other tokens
    (self/this, decorators and other “metadata”)
2.  class and function names serve as natural section headings, so it makes
    sense to underline them
3.  bold allows to emphasize tokens in a different way - e.g. allows making
    keywords stand out without being overwhelming

Summary
-------

The result of all this is that part of the process of understanding the code
can happen before our brain actually parses the letters. When meaning is
conveyed with color and lightness, you no longer have to read the code to find
some information - it may be enough to just _look_ at it.
