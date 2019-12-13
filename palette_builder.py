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

    @classmethod
    def load_from_module(cls, module_name):
        import importlib
        config = importlib.import_module(module_name)
        return cls(config.name,
                   config.background,
                   config.foreground,
                   config.shades)

    @classmethod
    def load_from_path(cls, path):
        """Dynamically import module with specifications from path."""
        import os, sys
        module_dir = os.path.dirname(path)
        if module_dir not in sys.path:
            sys.path.insert(0, module_dir)

        file_name = os.path.basename(path)
        module_name = file_name.replace(".py", "")
        return cls.load_from_module(module_name)

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
    """Print RGB coordinates of the resulting palette for debugging."""
    import sys
    import pprint

    if len(sys.argv) < 2:
        print("Missing argument: path to the module with palette specification")
        sys.exit()

    p = Palette.load_from_path(sys.argv[1])
    pprint.pprint(p.rgb_values())
