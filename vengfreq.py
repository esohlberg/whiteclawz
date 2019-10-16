import argparse
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("mode")
    args = parser.parse_args()
    filename = 'ctxts/' + args.filename
    mode = int(args.mode)
    x = open(filename, 'r').read()
    alldicts = []
    for i in range(mode):
        alldicts.append({})

    print(alldicts)
    
    keyspot = 0
    for char in x:
        if char in alldicts[keyspot]:
            alldicts[keyspot][char] += 1
        else: 
            alldicts[keyspot][char] = 1
        keyspot += 1
        if keyspot == mode:
            keyspot = 0
    
    for babydict in alldicts:
        while babydict:
            highest = 0
            highestkey = None
            for key, value in babydict.items():
                if value > highest:
                    highest = value
                    highestkey = key
            if (highestkey.isalnum()):
                print(highestkey + ': ' + str(highest))
            babydict.pop(highestkey, None)
        print('\n')