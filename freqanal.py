import argparse
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = 'ctxts/' + args.filename
    x = open(filename, 'r').read()
    print(x)
    allchars = {}
    print(x)
    for char in x:
        if char in allchars:
            allchars[char] += 1
        else: 
            allchars[char] = 1
    while allchars:
        highest = 0
        highestkey = None
        for key, value in allchars.items():
            if value > highest:
                highest = value
                highestkey = key
        if (highestkey.isalnum()):
            percent = highest/len(x) * 100
            print(highestkey + ': ' + str(highest) + " " + "{0:.2f}".format(percent) + "%")

        allchars.pop(highestkey, None)        
