"""Define styling (color and formatting) for common token types.

Color should be a name available in Palette.color_coords dictionary.
Formatting should be either "normal" or a combination of
- boid
- italic
- underline
(order doesn't matter)."""

rules = {
    # non-code (information and metadata)
    "comment":         ("dim_0", "italic"),
    "doc_comment":     ("dim_0", "normal"),
    "doc_special":     ("dim_1", "bold italic"),

    # literals and constants
    "string":          ("dim_1", "bold"),
    "str_special":     ("fg_2",  "normal"),
    "number":          ("fg_2",  "normal"),
    "constant":        ("fg_0",  "italic"),

    # language reserved words
    "keyword":         ("fg_1",  "bold"),

    # "meta" tokens that supplement other elements
    "type":            ("dim_2", "italic"),
    "keyword_arg":     ("dim_3", "italic"),
    "special_var":     ("dim_1", "bold italic"),

    # elements that are usually predefined
    "built_in":        ("dim_3", "italic"),
    "exception":       ("fg_2",  "bold"),
    "decorator":       ("dim_3", "italic"),

    # elements that are usually user-defined
    "class_def":       ("fg_2",  "bold underline"),
    "function_def":    ("fg_2",  "underline"),
    "function_call":   ("dim_3", "bold"),
    "variable":        ("fg_0",  "normal"),

    # other
    "punctuation":     ("fg_2",  "normal"),
}
