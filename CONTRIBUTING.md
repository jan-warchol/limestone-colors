Developer documentation
-----------------------

You're welcome to contribute improvements to the themes. Please just make sure
to only use the colors from the corresponding palette (see above), and avoid
any non-standard formatting styles (bold, italic and underline are fine).


## Theme builder usage

Theme files are generated from templates. Overall flow is:

- color specification (modules in `palettes/`) -> palette
- palette + styling rules (`token_styling_*`) + template (`*.j2`) -> theme file

First install dependencies:

    pip3 install --user -r requirements.txt

Build a palette and output its colors:

    python3 palette_builder.py palettes/limestone.py

Generate a config file from a palette and template:

    python3 build_theme.py \
        --palette palettes/limestone.py \
        --template example-template.j2 \
        --styling token_styling_dual.py
