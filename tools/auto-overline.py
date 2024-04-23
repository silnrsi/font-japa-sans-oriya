#!/usr/bin/python3

from nameslist import *
import sys


matras.insert(0, '')

with open(sys.argv[1], 'w') as output:
    output.write('vowels\n')
    chars = list()
    for char in vowels:
        chars.append(char + o)
    line = ' '.join(chars) + '\n'
    output.write(line)

    # output.write('consonants\n')
    # chars = list()
    # for char in consonants:
    #     chars.append(char + o)
    # line = ' '.join(chars) + '\n'
    # output.write(line)

    output.write('consonant + virama + ra + matras\n')
    for c in consonants:
        chars = list()
        for v in matras:
            chars.append(c + h + ra + v + o)
        line = ' '.join(chars) + '\n'
        output.write(line)

    output.write('ta + virama + sa + virama + consonant + matras\n')
    for c in consonants:
        chars = list()
        for v in matras:
            chars.append(ta + h + sa + h + c + v + o)
        line = ' '.join(chars) + '\n'
        output.write(line)
