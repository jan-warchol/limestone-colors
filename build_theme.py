"""Generate a theme file from palette, styling and config template."""

from __future__ import division
from jinja2 import Template
from pprint import pprint
import sys
import palette_builder as builder
import token_styling


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


if len(sys.argv) < 3:
    print("Usage: build_theme <palette> <template>")
    sys.exit()

# calculate values for templating from palette
palette = builder.Palette.load_from_path(sys.argv[1])

pycharm_styling = {
    token: build_pycharm_snippet(palette.rgb_values()[color_name], style)
    for token, (color_name, style) in token_styling.rules.items()
}

values = {"name": palette.name}
values.update(palette.rgb_values())
values.update(pycharm_styling)

with open("VERSION", "r") as f:
    values["version"] = f.read().strip()

with open(sys.argv[2], "r") as f:
    template = Template(f.read())

output_path = sys.argv[2].replace(
    ".j2",
    "-{}-{}.icls".format(palette.slug, values["version"])
)
with open(output_path, "w") as f:
    f.write(template.render(**values))
    print("Output written to {}".format(output_path))
