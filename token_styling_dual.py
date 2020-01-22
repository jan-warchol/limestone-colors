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
    "todo_comment":    ("dim_0", "italic"),
    "doc_comment":     ("dim_0", "normal"),
    "doc_special":     ("dim_1", "bold"),

    # literals and constants
    "string":          ("secondary", "normal"),
    "str_special":     ("fg_2",  "normal"),
    "number":          ("secondary",  "normal"),
    "boolean":         ("secondary",  "italic"),
    "constant":        ("dim_3", "bold"),

    # language reserved words
    "keyword":         ("primary",  "bold"),
    "import":          ("primary",  "bold"),
    "operator":        ("primary",  "normal"),

    # "meta" tokens that supplement other elements
    "type":            ("dim_1", "bold italic"),
    "keyword_arg":     ("dim_3", "italic"),
    "special_var":     ("dim_1", "bold italic"),

    # elements that are usually predefined
    "built_in":        ("primary_2_3",  "normal"),
    "exception":       ("fg_2",  "bold"),
    "decorator":       ("primary_2_3",  "italic"),

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
