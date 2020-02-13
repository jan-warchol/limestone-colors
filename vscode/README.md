Monochrome VScode
-----------------

Monochrome theme for Visual Studio Code. This is work in progress; currently it
supports styling of typical programming language tokens (like keywords,
strings, exceptions, etc.). Once the styling for these settle, I'll add support
for things like Markdown or XML.

Installation
------------

1.  Put content of this directory (including `package.json`) in a subdir of
    `$HOME/.vscode/extensions`.  The easiest way to do it is to clone the repo
    and setup a symlink like this (tested on Linux):

        git clone https://github.com/jan-warchol/limestone-colors
        ln -sf $PWD/limestone-colors/vscode $HOME/.vscode/extensions/limestone

1.  reload the window (`Ctrl+Shift+P` => search for `reload`; sometimes it's
    necessary to reload the window twice) or just restart VScode.

1.  Open `Color Theme` picker from preferences (shortcut: `Ctrl+K Ctrl+T`) and
    search for `Monochrome`.
