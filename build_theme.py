"""Generate a theme file from palette, styling and config template."""

from __future__ import division
from jinja2 import Template
from pprint import pprint
from os import path
import sys
import palette_builder as builder
from utils import import_module_from_path
import argparse
import re


def calc_output_path(values, input_path):
    """Build config filename from palette info and template name."""
    directory = path.dirname(input_path)
    template_fname = path.basename(input_path).replace(".j2", "")
    extension = re.sub(re.compile(r'.*template\.'), '', template_fname)
    filename = values["slug"] + "-" + values["version"] + "." + extension
    return path.join(directory, filename)


def build_pycharm_snippet(color, style):
    """Wrap styling information in format appropriate for PyCharm config."""
    attributes = set(style.split())
    result = ['<option name="FOREGROUND" value="{}" />'.format(color)]

    if "bold" in attributes and "italic" in attributes:
        result.append('<option name="FONT_TYPE" value="3" />')
    elif "bold" in attributes:
        result.append('<option name="FONT_TYPE" value="1" />')
    elif "italic" in attributes:
        result.append('<option name="FONT_TYPE" value="2" />')

    if "underline" in attributes:
        result.append('<option name="EFFECT_COLOR" value="{}" />'.format(color))
        result.append('<option name="EFFECT_TYPE" value="1" />')

    return '\n        '.join(result)


def build_vscode_snippet(color, style):
    """Wrap styling information in format appropriate for VScode config."""
    result = [
        '"fontStyle": "{}",'.format(style),
        '"foreground": "#{}"'.format(color)
    ]
    return '\n				'.join(result)


def build_templating_values(palette, styling_rules):
    """Create a dict with all attributes that can be used in a template."""
    mapping = {
        "name": palette.name,
        "slug": palette.slug,
    }
    with open("VERSION", "r") as f:
        mapping["version"] = f.read().strip()

    for token, (color_name, style) in styling_rules.items():
        rgb_color = palette.get_rgb_values()[color_name]
        mapping[token] = {
            "color": rgb_color,
            "style": style,
            "pycharm": build_pycharm_snippet(rgb_color, style),
            "vscode": build_vscode_snippet(rgb_color, style),
        }

    # we want to use color names directly e.g. for editor-specific settings
    mapping.update(palette.get_rgb_values())

    return mapping


# Parse options and run templating.

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--palette", "-p", required=True)
parser.add_argument("--template", "-t", required=True)
parser.add_argument("--styling", "-s", required=True)
args = parser.parse_args()

palette = builder.Palette.load_from_path(args.palette)
token_styling = import_module_from_path(args.styling)
values = build_templating_values(palette, token_styling.rules)

with open(args.template, "r") as f:
    template = Template(f.read())

output_path = calc_output_path(values, args.template)
with open(output_path, "w") as f:
    f.write(template.render(**values))
    print("Output written to {}".format(output_path))
