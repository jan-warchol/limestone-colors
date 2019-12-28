Monochrome VScode
-----------------

Monochrome theme for Visual Studio Code. This is work in progress; currently it
supports styling of typical programming language tokens (like keywords,
strings, exceptions, etc.). Once the styling for these settle, I'll add support
for things like Markdown or XML.

Installation
------------

You need to put content of this directory in a subdir of `.vscode/extensions`.
The easiest way to do it is to clone the repo and setup a symlink like this
(tested on Linux):

    git clone https://github.com/jan-warchol/monochrome-syntax --branch devel
    ln -s $HOME/.vscode/extensions/mono-theme $PWD/monochrome-syntax/vscode

After that, reload window (Ctrl+Shift+P => search for "reload") or just restart
VScode.
