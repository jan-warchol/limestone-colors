"""Generate a theme file from palette, styling and config template."""

from __future__ import division
from jinja2 import Template
from pprint import pprint
from os import path
import sys
import palette_builder as builder
import token_styling
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


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--palette", "-p", required=True)
parser.add_argument("--template", "-t", required=True)
args = parser.parse_args()

palette = builder.Palette.load_from_path(args.palette)

pycharm_styling = {
    token: build_pycharm_snippet(palette.rgb_values()[color_name], style)
    for token, (color_name, style) in token_styling.rules.items()
}

values = {
    "name": palette.name,
    "slug": palette.slug,
}
values.update(palette.rgb_values())
values.update(pycharm_styling)

with open("VERSION", "r") as f:
    values["version"] = f.read().strip()

with open(args.template, "r") as f:
    template = Template(f.read())

output_path = calc_output_path(values, args.template)
with open(output_path, "w") as f:
    f.write(template.render(**values))
    print("Output written to {}".format(output_path))
