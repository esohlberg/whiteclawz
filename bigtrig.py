import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("bigtrig")
    args = parser.parse_args()
    filename = 'ctxts/' + args.filename
    bigtrig = args.bigtrig

    s = open(filename, 'r').read()
    btwn = s.split(bigtrig)
    notbigtrig = []
    for x in btwn:
        notbigtrig.append(len(x))
    print("bigtrig occurs " + str(len(notbigtrig) - 1) + " times")
    print(notbigtrig)
