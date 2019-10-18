import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    parser.add_argument("original")
    args = parser.parse_args()
    output = ord(args.output) - 96
    if args.original == '$':
        original = 27
    else:
        original = ord(args.original) - 96
    if output < original:
        output += 27
    if output - original == 27:
        print('$')
    else:
        key = output - original + 96
        print(chr(key))

