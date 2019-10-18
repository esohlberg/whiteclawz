import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("old")
    parser.add_argument("new")
    args = parser.parse_args()

    old = args.old
    new = args.new

    filename = 'test.txt'
    x = open(filename, 'r').read()
    n = 3
    nospaces = x.split()
    x = ''.join(nospaces)
    chunked = [] 
    while len(x) > 3:
        curr = x[0]
        if curr.isalpha():
            chunked.append(curr)
            x = x[1:]
        else:
            chunked.append(x[0:3])
            x = x[3:]
    
    print(chunked)
    f = open('test.txt', 'w')
    final = []
    for c in chunked:
        if c == old:
            final.append(new)
        else:
            final.append(c)

    final = ''.join(final)
    print(final)
    f.write(final)