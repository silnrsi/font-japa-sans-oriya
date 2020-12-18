#!/usr/bin/python3

from nameslist import *
from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)
print(f'Add anchors for {ufo}')

# Modify UFO

# overline character
overline = font['overline-oriya']
for anchor in overline.anchors:
    if anchor.name == '_top':
        anchor.name = '_ol'

for glyph in font:
    # vowels
    if glyph.unicode in Vowels + Matras:
        bounds = glyph.bounds
        if bounds is None:
            print('vowel does not have bounding box')
            continue
        (xmin, ymin, xmax, ymax) = bounds
        for anchor in glyph.anchors:
            if anchor.name == 'topright':
                xcenter = (xmin + xmax) / 2
                y = anchor.y
                glyph.appendAnchor('ol', (xcenter, y))

    # consonants
    if glyph.unicode in Consonants:
        for anchor in glyph.anchors:
            if anchor.name == 'top':
                x = anchor.x
                y = anchor.y
                glyph.appendAnchor('ol', (x, y))

# Save UFO
font.changed()
font.save()
font.close()
