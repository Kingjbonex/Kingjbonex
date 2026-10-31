"""GitHub profile art in the Night shift brand: README header (Night and Day) and a footer strip.

    python3 gh_profile.py          # writes header-night.png, header-day.png, footer-*.png here

Native 400x100, scaled 4x to 1600x400 (shown at width 800 in the README, an exact 2:1).
Everything comes from brand.py: palette, fonts, scenes, portrait tile.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(HERE, "..", "brand")]
import brand as b  # noqa: E402
import x_profile as xp  # noqa: E402

W, H, BAR, SCALE = 400, 100, 18, 4


def header(mode="night", kicker="Software engineer"):
    m = b.MODES[mode]
    im, d = b.canvas(W, H, m["bg"])
    ground = H - BAR - 8
    tx = 20
    if mode == "night":
        b.night_scene(im, ground, keep_clear=[(tx - 2, 12, 300, 66)], moon_at=(W - 96, 20))
        d.rectangle([0, ground, W, H], fill=xp.WALL[0])
        d.line([(0, ground), (W, ground)], fill=xp.WALL[2])
    else:
        b.day_scene(im, d, ground)
    sh = b.INK if mode == "night" else None
    b.text(d, tx, 18, kicker.upper(), b.LABEL, m["kicker"], shadow=sh)
    b.wordmark(im, d, tx, 30, mode)
    b.text(d, tx, 56, "BUILDING IN PUBLIC. ONE LEVEL AT A TIME.", b.LABEL, m["text"], shadow=sh)
    b.portrait(im, d, W - 20 - 50, ground - 50 + 4)
    d.rectangle([0, H - BAR, W, H], fill=b.INK)
    foot = b.LILAC if mode == "night" else b.PAPER[2]
    b.text(d, tx, H - BAR + 6, "JAMESPENNING.DEV", b.LABEL, foot)
    right = "CI/CD  AI  TESTING"
    b.text(d, W - 34 - b.tw(d, right, b.LABEL), H - BAR + 6, right, b.LABEL, foot)
    (b.moon if mode == "night" else b.star)(d, W - 22, H - BAR + 5)
    d.rectangle([0, 0, W - 1, H - 1], outline=b.INK)
    return b.up(im, SCALE)


def footer(mode="night"):
    strip = b.skyline_strip(mode, w=W, h=24)
    return b.up(strip, SCALE)


if __name__ == "__main__":
    for mode in ("night", "day"):
        header(mode).save(os.path.join(HERE, f"header-{mode}.png"))
        footer(mode).save(os.path.join(HERE, f"footer-{mode}.png"))
    print("wrote", HERE)
