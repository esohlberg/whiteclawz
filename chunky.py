import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("keylen")
    args = parser.parse_args()

    filename = 'ctxts/' + args.filename
    keylen = int(args.keylen)

    x = open(filename, 'r').read()
    n = keylen
    nospaces = x.split()
    x = ''.join(nospaces)
    final = [x[i * n:(i+1) * n] for i in range((len(x) + n - 1) // n)]
    f = open('test.txt', 'w')
    for chunk in final:
        f.write(chunk)
        f.write('\n')
    print(final)