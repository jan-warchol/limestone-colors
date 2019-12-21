"""Define styling (color and formatting) for common token types.

Color should be a name available in Palette.color_coords dictionary.
Formatting should be either "normal" or a combination of
- boid
- italic
- underline
(order doesn't matter)."""

rules = {
    "comment":         ("dim_0", "italic"),
    "doc_comment":     ("dim_0", "normal"),
    "doc_special":     ("dim_1", "bold italic"),

    "keyword":         ("fg_1",  "bold"),

    "constant":        ("fg_0",  "italic"),
    "number":          ("fg_0",  "bold"),
    "string":          ("dim_1", "bold"),
    "str_special":     ("fg_2",  "normal"),

    "class_def":       ("fg_1",  "underline"),
    "function_def":    ("fg_1",  "underline"),
    "function_call":   ("fg_0",  "normal"),
    "variable":        ("fg_0",  "normal"),

    "type":            ("dim_1", "bold italic"),
    "special_var":     ("dim_1", "bold italic"),
    "annotation":      ("fg_0",  "italic"),

    "punctuation":     ("fg_2",  "normal"),

    "keyword_arg":     ("dim_3", "italic"),
    "built_in":        ("fg_0",  "italic"),
    "exception":       ("fg_2",  "bold"),
}
