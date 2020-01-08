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
        --template vscode-template.json.j2 \
        --styling token_styling_dual.py


Tips & Tricks
-------------

Sometimes built-in color themes get in the way (e.g. when you're making changes
in the theme and constantly switching between the old and new version to
compare them), so you may want to disable some of them.

In **VScode**, open _Extensions_ view (`Ctrl+Shift+X`), search for `@builtin`
extensions and look in the `Themes` section. To disable a theme, use the gear
menu. ([Link to the
docs.](https://code.visualstudio.com/docs/getstarted/themes#_remove-default-themes))

Unfortunately it seems that disabling built-in themes in Intellij IDEs is not
possible.


Bulk install of IntelliJ scheme files
setup a symlink from `~/.PyCharmCE2019.3/config/colors` to the directory with color schemes. Note that updating a theme requires IDE restart.

Quick switcher for pycharm themes: 

    Ctrl + `
    1
    <select theme>


To quickly iterate over a color scheme in VScode, use local overrides

    {
            "folders": [
                    {
                            "path": "/home/jan/src/code-samples"
                    }
            ],
            "settings": {
                    "editor.tokenColorCustomizations": {
                            "textMateRules": [
                                    {
                                            "scope": "variable.other.normal",
                                            "settings": {
                                                    "foreground": "#FF0000",
                                                    "fontStyle": "bold"
                                            },
                                    }
                            ],
                    }
            }
    }
