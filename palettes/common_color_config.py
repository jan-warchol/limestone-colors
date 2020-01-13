from __future__ import division

# lightness of a shade on the scale from 0 (background) to 1 (foreground)
shades_lightness = {
    "bg_0":  0,
    "bg_1":  1/12,
    "bg_2":  1/6,
    "bg_3":  1/4,
    "dim_0": 4/8,
    "dim_1": 3/5,
    "dim_2": 6/8,
    "dim_3": 5/6,
    "fg_0":  1,
    "fg_1":  1 + 1/6,
    "fg_2":  1 + 1/4,
    "fg_3":  1 + 1/3,
}

# generate lots of variants until I decide which ones are most useful
accent_variants = {
    "2_3": (1, 2/3),
    "1_2": (1, 1/2),
    "1_3": (1, 1/3),
    "1_5": (1, 1/6),

    "dim1": (5/6, 1),
    "2_3_dim1": (5/6, 2/3),
    "1_2_dim1": (5/6, 1/2),
    "1_3_dim1": (5/6, 1/3),
    "1_5_dim1": (5/6, 1/5),

    "dim2": (3/5, 1),
    "2_3_dim2": (3/5, 2/3),
    "1_2_dim2": (3/5, 1/2),
    "1_3_dim2": (3/5, 1/3),
    "1_5_dim2": (3/5, 1/5),

    "br1": (1 + 1/6, 1),
    "2_3_br1": (1 + 1/6, 2/3),
    "1_2_br1": (1 + 1/6, 1/2),
    "1_3_br1": (1 + 1/6, 1/3),
    "1_5_br1": (1 + 1/6, 1/5),

    "br2": (1 + 1/4, 1),
    "2_3_br2": (1 + 1/4, 2/3),
    "1_2_br2": (1 + 1/4, 1/2),
    "1_3_br2": (1 + 1/4, 1/3),
    "1_5_br2": (1 + 1/4, 1/5),
}
