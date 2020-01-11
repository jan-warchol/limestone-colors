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
    get_rgb_values(): returns a dict mapping color names to hex sRGB coords.

    Naming conventions for base_shades:
    `bg_*` - shades used for background (e.g. cursor line or selection)
    `fg_*` - foreground and bright foreground
    `dim_*` - secondary shades (between bg and fg)
    """

    def __init__(self, name, background, foreground, shade_specs=None):
        """Initialize with base shades. Accent colors may remain empty."""
        self.name = name
        self.slug = slugify(name)
        self.bg = LabColor(*background, illuminant="d50")
        self.fg = LabColor(*foreground, illuminant="d50")
        self.contrast = self.fg.lab_l - self.bg.lab_l

        self.base_shades = {}
        self.accent_colors = {}

        if shade_specs:
            self.build_shades(shade_specs)

    @classmethod
    def load_from_path(cls, path):
        """Init from module containig specs, with accent colors if present."""
        from utils import import_module_from_path
        config = import_module_from_path(path)

        print("Creating palette \"{}\"...".format(config.name))
        result = cls(config.name,
                     config.background,
                     config.foreground,
                     config.shades)
        print("Generated {} base shades.".format(len(config.shades)))

        try:  # accent colors are optional
            result.build_variants(config.colors, config.color_variants)
            print("Generated {} accent colors with {} variant(s) each.".format(
                len(config.colors),
                len(config.color_variants) + 1))
        except AttributeError:
            print("No information about accent colors, skipping.")

        return result

    def build_variants(self, colors, variant_specs):
        """Add accent colors + variants with different lightness/saturation."""
        for name, coords in colors.items():
            self.accent_colors[name] = coords
            orig_l, orig_a, orig_b = coords
            for suffix, (brightness, saturation) in variant_specs.items():
                a = orig_a * saturation
                b = orig_b * saturation
                # Accents may have different lightness than foreground. Adjust
                # lightness of desaturated variants to ensure smooth transition.
                l = orig_l * saturation + self.fg.lab_l * (1-saturation)
                l = min(l * brightness, 100)
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
        fg_weight = relative_lightness
        bg_weight = 1 - relative_lightness
        l = self.bg.lab_l + relative_lightness * self.contrast
        a = fg_weight * self.fg.lab_a + bg_weight * self.bg.lab_a
        b = fg_weight * self.fg.lab_b + bg_weight * self.bg.lab_b
        return (l, a, b)

    def foreground_shade(self, relative_lightness):
        """Calculate a color derived from foreground."""
        l = self.bg.lab_l + relative_lightness * self.contrast
        return (min(l, 100), self.fg.lab_a, self.fg.lab_b)

    def background_shade(self, relative_lightness):
        """Calculate a color derived from background."""
        l = self.bg.lab_l + relative_lightness * self.contrast
        return (l, self.bg.lab_a, self.bg.lab_b)

    def get_all_colors(self):
        """Return a dictionary with all color coordinates."""
        result = {}
        result.update(self.base_shades)
        result.update(self.accent_colors)
        return result

    def get_lab_colors(self):
        """Return a dictionary of Lab color objects (not just coordinates)."""
        return {
            name: LabColor(*coords, illuminant='d50')
            for name, coords in self.get_all_colors().items()
        }

    def get_rgb_colors(self):
        """Return a dictionary of sRGB color objects (not just coordinates)."""
        return {
            name: convert_color(lab, sRGBColor)
            for name, lab in self.get_lab_colors().items()
        }

    def get_rgb_values(self):
        return {
            name: rgb.get_rgb_hex().replace('#', '')
            for name, rgb in self.get_rgb_colors().items()
        }


if __name__ == "__main__":
    """Print RGB coordinates of the resulting palette for debugging."""
    import sys
    import pprint

    if len(sys.argv) < 2:
        print("Missing argument: path to the module with palette specification")
        sys.exit()

    p = Palette.load_from_path(sys.argv[1])
    pprint.pprint(p.get_rgb_values())
