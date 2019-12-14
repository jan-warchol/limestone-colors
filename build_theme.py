"""Generate a theme file from palette and config template."""

from __future__ import division
from jinja2 import Template
from pprint import pprint
import sys
import palette_builder as builder

if len(sys.argv) < 2:
    print("Missing argument: path to the module with palette specification")
    sys.exit()

# calculate values for templating from palette
palette = builder.Palette.load_from_path(sys.argv[1])

values = {"name": palette.name}
values.update(palette.rgb_values())

with open("VERSION", "r") as f:
    values["version"] = f.read().strip()

# run templating
with open("template.j2", "r") as f:
    template = Template(f.read())

output_path = "{}-{}".format(palette.slug, values["version"])
with open(output_path, "w") as f:
    f.write(template.render(**values))
    print("Output written to {}".format(output_path))
