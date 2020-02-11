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

accent_variants = {
    "dim": (3/4,   1),
    "br":  (1+1/6, 1),

    "soft":      (1,     0.618),
    "soft_dim":  (3/4,   0.618),
    "soft_br":   (1+1/6, 0.618),

    "softer":      (1.062, 0.382),
    "softer_dim":  (3/4,   0.382),
    "softer_br":   (1+1/6, 0.382),
}
