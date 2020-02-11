"""Define styling (color and formatting) for common token types.

Color should be a name available in Palette.color_coords dictionary.
Formatting should be either "normal" or a combination of
- boid
- italic
- underline
(order doesn't matter)."""

rules = {
    # non-code (information and metadata)
    "comment":         ("dim_1", "italic"),
    "todo_comment":    ("dim_1", "italic"),
    "doc_comment":     ("dim_1", "normal"),
    "doc_special":     ("dim_2", "bold"),

    # literals and constants
    "string":          ("secondary_soft", "normal"),
    "str_special":     ("fg_2",  "normal"),
    "number":          ("secondary",  "normal"),
    "boolean":         ("secondary",  "italic"),
    "constant":        ("dim_3", "bold"),

    # language reserved words
    "keyword":         ("primary_softer",  "bold"),
    "import":          ("primary_softer",  "bold"),
    "operator":        ("primary",  "normal"),

    # "meta" tokens that supplement other elements
    "type":            ("dim_1", "bold italic"),
    "keyword_arg":     ("dim_3", "italic"),
    "special_var":     ("dim_1", "bold italic"),

    # elements that are usually predefined
    "built_in":        ("primary_soft",  "normal"),
    "exception":       ("fg_2",  "bold"),
    "decorator":       ("primary_soft",  "italic"),

    # elements that are usually user-defined
    "class_def":       ("fg_1",  "bold underline"),
    "function_def":    ("fg_1",  "underline"),
    "function_call":   ("fg_0",  "normal"),
    # some grammars use one scope for function definitions and calls
    "function":        ("fg_0",  "normal"),
    "parameter":       ("fg_0",  "normal"),

    # other
    "punctuation":     ("fg_2",  "normal"),
}
