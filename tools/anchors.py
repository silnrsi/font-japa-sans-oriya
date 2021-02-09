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
# offset = 50
# overline = font['overline-oriya']
# for anchor in overline.anchors:
#     if anchor.name == '_ol':
#         anchor.name = '_top'
#         anchor.y -= offset

# the height of the overline above the regular iMatra has been adjusted,
# so copy that height to the other iMatra type glyphs
imatra = font['iMatra-oriya']
imatra_top_y = 0
for anchor in imatra.anchors:
    if anchor.name == 'top':
        imatra_top_y = anchor.y

for glyph in font:
    # vowels and matras (and a few consonants)
    bounds = glyph.bounds
    if bounds is None:
        print('glyph does not have bounding box')
        continue
    (xmin, ymin, xmax, ymax) = bounds
    xcenter = (xmin + xmax) / 2
    if glyph.unicode in Vowels + Matras:
        for anchor in glyph.anchors:
            if anchor.name == 'topright':
                y = anchor.y
                glyph.appendAnchor('top', (xcenter, y))

    # glyphs that do not have a topright (or top) anchor to model on
    bare = ('eMatra-oriya', 'rrVocalic-oriya', 'llVocalic-oriya', 'rra-oriya', 'rha-oriya')
    if glyph.name in bare:
        glyph.appendAnchor('top', (xcenter, 658))

    # might need an overline on top of iMatras
    if glyph.name.startswith('iMatra'):
        for anchor in glyph.anchors:
            if anchor.name == '_top':
                x = anchor.x
                # anchor.y = imatra_top_y
                y = anchor.y
                glyph.appendAnchor('top', (x, y+150))

    # consonants
    # if glyph.unicode in Consonants:
    #     for anchor in glyph.anchors:
    #         if anchor.name == 'top':
    #             x = anchor.x
    #             y = anchor.y
    #             glyph.appendAnchor('ol', (x, y+offset))

    # move ol anchor up so that it is not at the same point as the anchor top
    # for anchor in glyph.anchors:
    #     if anchor.name.endswith('ol'):
    #         anchor.y += offset

    # remove ol anchor since we can use the anchor top
    for anchor in glyph.anchors:
        if anchor.name == 'ol':
            glyph.removeAnchor(anchor)


# Save UFO
font.changed()
font.save()
font.close()
