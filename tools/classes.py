#!/usr/bin/python3

from nameslist import *
from fontParts.world import *
import sys

# open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# create a mapping of codepoints to glyph names
cmap = dict()
for glyph in font:
    cmap[glyph.unicode] = glyph.name

# create a list of glyph names of the consonants
glyph_names = list()
for codepoint in Consonants:
    glyph_name = cmap[codepoint]
    glyph_names.append(glyph_name)
line = ' '.join(glyph_names) + '\n'
print(line)
