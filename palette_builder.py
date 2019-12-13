from __future__ import division
from slugify import slugify
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color


class Palette(object):
    """Build a color palette from background, foreground and lightness data.

    Background and foreground should be coordinates in CIE Lab color space.
    The restult is a mapping of color names to tuples with their CIE Lab
    coordinates, stored in color_coords attribute.

    Naming conventions for colors:
    `bg_*` - shades used for background (e.g. cursor line or selection)
    `fg_*` - foreground and bright foreground
    `dim_*` - secondary shades (between bg and fg)
    """
    def __init__(self, name, background, foreground, shade_specs):
        self.name = name
        self.slug = slugify(name)
        self.bg = LabColor(*background)
        self.fg = LabColor(*foreground)
        self.contrast = self.fg.lab_l - self.bg.lab_l

        self.color_coords = {}
        self.color_coords["fg_0"] = foreground
        self.color_coords["bg_0"] = background

        self.build_shades(shade_specs)

    def build_shades(self, shade_specs):
        """Calculate supplemental shades according to their naming."""
        for name, lightness in shade_specs.items():
            if name.startswith("bg"):
                self.color_coords[name] = self.background_shade(lightness)
            elif name.startswith("fg"):
                self.color_coords[name] = self.foreground_shade(lightness)
            else:
                self.color_coords[name] = self.secondary_shade(lightness)

    def secondary_shade(self, relative_lightness):
        """Calculate a color that is a weighted average of bg and fg."""
        lightness = self.bg.lab_l + relative_lightness * self.contrast
        fg_weight = relative_lightness
        bg_weight = 1 - relative_lightness
        a = fg_weight * self.fg.lab_a + bg_weight * self.bg.lab_a
        b = fg_weight * self.fg.lab_b + bg_weight * self.bg.lab_b
        return (lightness, a, b)

    def foreground_shade(self, relative_lightness):
        """Calculate a color derived from foreground."""
        lightness = self.bg.lab_l + relative_lightness * self.contrast
        return (min(lightness, 100), self.fg.lab_a, self.fg.lab_b)

    def background_shade(self, relative_lightness):
        lightness = self.bg.lab_l + relative_lightness * self.contrast
        return (lightness, self.bg.lab_a, self.bg.lab_b)

    def lab_colors(self):
        return {
            name: LabColor(*coords, illuminant='d50')
            for name, coords in self.color_coords.items()
        }

    def rgb_values(self):
        return {
            name: convert_color(lab, sRGBColor).get_rgb_hex().replace('#', '')
            for name, lab in self.lab_colors().items()
        }


if __name__ == "__main__":
    """Print RGB coordinates calculated from palette_spec, for debugging."""
    import sys
    import pprint
    import palette_spec as config

    p = Palette(config.name,
                config.background,
                config.foreground,
                config.shades)
    pprint.pprint(p.rgb_values())
