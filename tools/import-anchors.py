#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFOs
dst_ufo = sys.argv[1]
src_ufo = dst_ufo.replace('source/masters/Japa', '../noto/sources/Noto').replace('Extra', '')
dst_font = OpenFont(dst_ufo)
src_font = OpenFont(src_ufo)
print(f'Import anchors for {dst_ufo}')

# Query UFO for alt nukta info
nukta_alt = src_font['nukta-oriya.alt']
(xmin, ymin, xmax, ymax) = nukta_alt.bounds
xcenter = (xmin + xmax) / 2
ycenter = (ymin + ymax) / 2
for anchor in nukta_alt.anchors:
    if anchor.name == '_nukta':
        offset_x = anchor.x - xcenter
        offset_y = anchor.y - ycenter
        # print(f'x: {offset_x} y: {offset_y}')

# Import alt nukta
# print(f'psfcopyglyphs -f --rename rename --unicode usv -i tools/impogsut.csv -s {src_ufo} {dst_ufo}')

# Modify UFO
def get_anchors(glyph):
    anchors = set()
    for anchor in glyph.anchors:
        anchors.add(anchor.name)
    return anchors

for dst in dst_font:
    if dst.name not in src_font:
        continue
    src = src_font[dst.name]
    dst_anchors = get_anchors(dst)
    for anchor in src.anchors:
        # if anchor.name != 'nukta':
        #     continue
        if anchor.name not in dst_anchors:
            print(f'import {src.name}: {anchor.name}')
            dst.appendAnchor(anchor.name, (anchor.x, anchor.y))

# Save UFO
dst_font.changed()
dst_font.save()
dst_font.close()
