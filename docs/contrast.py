"""WCAG 2 contrast checker for the site palette.

Run:  C:/Users/tevin/anaconda3/python.exe docs/contrast.py

Edit PALETTE and PAIRS below when colors change, re-run, paste the table
into decisions.md. AA needs 4.5:1 for body text, 3:1 for large text
(>= 24px, or >= 19px bold) and for UI borders/icons.

How the math works: each channel is linearised (sRGB gamma removed), the
three are weighted into a luminance L, then contrast = (L1+0.05)/(L2+0.05)
with the lighter color on top. 1:1 is identical, 21:1 is black on white.
"""

PALETTE = {
    # sampled from the logo
    "navy":       "#0a1e27",   # outer ground
    "navy-teal":  "#12343e",   # inner circle; card surfaces
    "mint":       "#559d7d",   # ring
    "sage":       "#518258",   # turtle skin
    "shell":      "#29563f",   # shell
    "strap":      "#7c765e",   # strap highlight
    # derived: same hues, pushed lighter so text can sit on navy
    "mint-light": "#8fd1b0",   # headings, links
    "cream":      "#e9efe9",   # body text on navy
    "cream-dim":  "#b7c4bd",   # secondary text on navy
    "tan":        "#c9b58a",   # warm accent from the strap
}

# (foreground, background, role, needs_large_only)
PAIRS = [
    ("cream",      "navy",      "body text",               False),
    ("cream",      "navy-teal", "body text on a card",     False),
    ("cream-dim",  "navy",      "secondary / footer text", False),
    ("cream-dim",  "navy-teal", "secondary text on card",  False),
    ("mint-light", "navy",      "headings, links",         False),
    ("mint-light", "navy-teal", "headings on card",        False),
    ("mint",       "navy",      "logo-mint as text",       False),
    ("mint",       "navy",      "logo-mint as large text", True),
    ("tan",        "navy",      "warm accent text",        False),
    ("tan",        "navy-teal", "warm accent on card",     False),
    ("navy",       "mint-light","text on a mint button",   False),
    ("navy",       "tan",       "text on a tan button",    False),
    ("mint",       "navy-teal", "border / icon on card",   True),
    ("sage",       "navy",      "sage as decoration",      True),
]


def _lin(c):
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexcolor):
    h = hexcolor.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(fg, bg):
    l1, l2 = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


if __name__ == "__main__":
    print(f"{'pair':28s} {'ratio':>6s}  AA(4.5)  AA-large(3)")
    for fg, bg, role, large_only in PAIRS:
        r = contrast(PALETTE[fg], PALETTE[bg])
        aa = "pass" if r >= 4.5 else "FAIL"
        aal = "pass" if r >= 3 else "FAIL"
        need = aal if large_only else aa
        flag = "" if need == "pass" else "   <-- fix"
        print(f"{fg + ' on ' + bg:28s} {r:5.1f}:1   {aa:5s}    {aal:5s}  {role}{flag}")
