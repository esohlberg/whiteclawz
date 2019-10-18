import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    filename = 'ctxts/' + args.filename
    x = open(filename, 'r').read()
    n = 3
    chunked = [x[i * n:(i+1) * n] for i in range((len(x) + n - 1) // n)]

    key = {
        '107': ' ',
        '221': 'E',
        '997': 'A',
        '440': 'H',
        '016': 'T',
        '636': 'O',
        '744': 'R',
        '231': 'I',
        '652': 'S',
        '401': 'W',
        '746': 'C',
        '575': 'P',
        '950': 'L',
        '447': 'Y',
        '181': 'D',
        '923': 'K',
        '483': 'Q',
        '006': 'U',
        '485': 'F',
        '474': 'V',
        '331': 'B',
        '985': 'M',
        '325': 'N',
        '521': 'G',
        '199': 'J',
        '241': 'X',
        '372': 'Z'
    }

    final = ''
    for c in chunked:
        if c in key:
            final += key[c]
    
    print(final)