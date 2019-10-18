import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    filename = 'ctxts/' + args.filename
    x = open(filename, 'r').read()
    n = 3
    nospaces = x.split()
    x = ''.join(nospaces)
    final = [x[i * n:(i+1) * n] for i in range((len(x) + n - 1) // n)]
    print(final)
    allchunks = {}
    for x in final:
        if x not in allchunks:
            allchunks[x] = 1
        else:
            allchunks[x] += 1
    while allchunks:
        highest = 0
        highestkey = None
        for key, value in allchunks.items():
            if value > highest:
                highest = value
                highestkey = key
        if (highestkey.isalnum()):
            percent = highest/len(final) * 100
            print(highestkey + ': ' + str(highest) + " " + "{0:.2f}".format(percent) + "%")

        allchunks.pop(highestkey, None)         