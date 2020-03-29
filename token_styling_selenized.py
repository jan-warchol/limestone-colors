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
    "todo_comment":    ("magenta", "bold italic"),
    "doc_comment":     ("dim_1", "normal"),
    "doc_special":     ("dim_2", "bold"),

    # literals and constants
    "string":          ("cyan", "normal"),
    "str_special":     ("red",  "normal"),
    "number":          ("cyan",  "normal"),
    "boolean":         ("cyan",  "normal"),
    "constant":        ("cyan", "normal"),

    # language reserved words
    "keyword":         ("yellow",  "normal"),
    "keyword_def":     ("yellow",  "normal"),
    "import":          ("orange",  "normal"),
    "operator":        ("yellow",  "normal"),

    # "meta" tokens that supplement other elements
    "type":            ("green", "normal"),
    "type_modifier":   ("green", "italic"),
    "keyword_arg":     ("fg_0", "normal"),
    "special_var":     ("red", "normal"),

    # elements that are usually predefined
    "built_in":        ("blue",  "normal"),
    "exception":       ("yellow",  "normal"),
    "decorator":       ("blue",  "normal"),

    # elements that are usually user-defined
    "class_def":       ("blue",  "normal"),
    "function_def":    ("blue",  "normal"),
    "function_call":   ("fg_0",  "normal"),
    # some grammars use one scope for function definitions and calls
    "function":        ("blue",  "normal"),
    "parameter":       ("fg_0",  "normal"),
    "shell_var":       ("orange", "normal"),
    "shell_special":   ("red", "normal"),

    # other
    "punctuation":     ("fg_0",  "normal"),
}
