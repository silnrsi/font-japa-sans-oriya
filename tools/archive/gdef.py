#!/usr/bin/python3

import fontParts.world as fontparts
import sys

# Open UFO
ufo = sys.argv[1]
font = fontparts.OpenFont(ufo)

# Modify UFO
marks = (
    # '_part.ra.below',
    # 'ra-oriya.single',
    'taalt-oriya.below',
    # 'tara-oriya.below',
    )

for glyph in font:
    if glyph.name in marks:
        glyph.width = 0

# Save UFO
font.changed()
font.save()
font.close()
