import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("mode")
    args = parser.parse_args()
    filename = 'ctxts/' + args.filename
    x = open(filename, 'r').read()
    mode = int(args.mode)
    grams = {}

    for i in range (0, len(x) - mode):
        curr = x[i:i+mode]
        if curr in grams:
            grams[curr] += 1
        else:
            grams[curr] = 1
    

    print(sorted(grams.items(), key = lambda x : x[1], reverse=True))