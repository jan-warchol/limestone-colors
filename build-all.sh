#!/bin/bash

# Simple helper for generating all configs for all theme variants.

mono="-p palettes/monochrome.py -s token_styling_mono.py"
two_color="-p palettes/limestone.py -s token_styling_dual.py"

for template in vscode-template.json.j2 pycharm-template.icls.j2; do
  for style in "$mono" "$two_color"; do
    python3 build_theme.py -t $template $style
  done
done
