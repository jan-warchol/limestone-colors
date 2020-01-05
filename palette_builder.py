from __future__ import division
from slugify import slugify
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color


class Palette(object):
    """Build a palette from bg, fg, lightness data and optional accent colors.

    Background and foreground should be coordinates in CIE Lab color space.
    The restult is a mapping of color names to tuples with their CIE Lab
    and sRGB coordinates.

    Important attributes:
    base_shades: colors derived from background and foreground (in CIE Lab).
    accent_colors: "special" colors like "blue", with variants (in CIE Lab).

    Important methods:
    rgb_values(): returns a dict mapping color names to hex sRGB coords.

    Naming conventions for base_shades:
    `bg_*` - shades used for background (e.g. cursor line or selection)
    `fg_*` - foreground and bright foreground
    `dim_*` - secondary shades (between bg and fg)
    """

    def __init__(self, name, background, foreground, shade_specs):
        """Initialize with base shades. Accent colors may remain empty."""
        self.name = name
        self.slug = slugify(name)
        self.bg = LabColor(*background)
        self.fg = LabColor(*foreground)
        self.contrast = self.fg.lab_l - self.bg.lab_l

        self.base_shades = {}
        self.accent_colors = {}

        self.build_shades(shade_specs)

    @classmethod
    def load_from_module(cls, module_name):
        """Init from module containig specs, with accent colors if present."""
        import importlib
        config = importlib.import_module(module_name)

        result = cls(config.name,
                     config.background,
                     config.foreground,
                     config.shades)
        print("Generated {} base shades.".format(len(config.shades)))

        try:
            result.build_variants(config.colors, config.color_variants)
            print("Generated {} accent colors with {} variant(s) each.".format(
                len(config.colors),
                len(config.color_variants) + 1))
        except AttributeError:
            print("No information about accent colors, skipping.")

        return result

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

    def build_variants(self, colors, variant_specs):
        """Add accent colors + variants with different lightness/saturation."""
        for name, coords in colors.items():
            self.accent_colors[name] = coords
            orig_l, orig_a, orig_b = coords
            for suffix, (lightness_factor, saturation) in variant_specs.items():
                a = orig_a * saturation
                b = orig_b * saturation
                # Accents may have different lightness than foreground. Adjust
                # lightness of desaturated variants to ensure smooth transition.
                adjusted = orig_l * saturation + self.fg.lab_l * (1-saturation)
                l = min(adjusted * lightness_factor, 100)
                self.accent_colors[name + "_" + suffix] = (l, a, b)

    def build_shades(self, shade_specs):
        """Add supplemental base colors calculated according to their naming."""
        for name, lightness in shade_specs.items():
            if name.startswith("bg"):
                self.base_shades[name] = self.background_shade(lightness)
            elif name.startswith("fg"):
                self.base_shades[name] = self.foreground_shade(lightness)
            else:
                self.base_shades[name] = self.secondary_shade(lightness)

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
        """Calculate a color derived from background."""
        lightness = self.bg.lab_l + relative_lightness * self.contrast
        return (lightness, self.bg.lab_a, self.bg.lab_b)

    def all_colors(self):
        result = {}
        result.update(self.base_shades)
        result.update(self.accent_colors)
        return result

    def lab_colors(self):
        """Return a dictionary of Lab color objects (not just coordinates)."""
        return {
            name: LabColor(*coords, illuminant='d50')
            for name, coords in self.all_colors().items()
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
