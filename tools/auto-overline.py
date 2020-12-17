#!/usr/bin/python3

from nameslist import *
import sys


with open(sys.argv[1], 'w') as output:
    output.write('vowels\n')
    chars = list()
    for char in vowels:
        chars.append(char + o)
    line = ' '.join(chars) + '\n'
    output.write(line)

    output.write('consonants\n')
    chars = list()
    for char in consonants:
        chars.append(char + o)
    line = ' '.join(chars) + '\n'
    output.write(line)

    output.write('consonants + matras\n')
    for c in consonants:
        chars = list()
        for v in matras:
            chars.append(c + v + o)
        line = ' '.join(chars) + '\n'
        output.write(line)
