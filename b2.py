import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    args = parser.parse_args()
    outpuy = ord(args.output) - 96
    for x in ['e', 't', 'a', 'o', 'i']:
        output = outpuy
        original = ord(x) - 96
        if output < original:
            output += 26
        key = output - original + 96
        if key == 96:
            print('z')
        else:
            print(chr(key))

