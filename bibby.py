import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    parser.add_argument("original")
    args = parser.parse_args()
    output = ord(args.output) - 96
    original = ord(args.original) - 96
    if output < original:
        output += 26
    key = output - original + 96
    print(chr(key))

