import argparse
import os

def adjustchar(currchar, keychar):
    if(keychar == '9'):
        return(currchar)
    if currchar == ' ':
        currnum = 27
    else:
        currnum = ord(currchar) - 96
    keynum = ord(keychar) - 96
    newnum = currnum - keynum
    if newnum <= 0:
        newnum += 27
    if(newnum == 27):
        return ' '
    newnum = newnum + 96
    return chr(newnum)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("key")
    args = parser.parse_args()
    filename = 'ctxts/' + args.filename
    key = args.key
    print(key)
    x = open(filename, 'r').read()
    answer = ''
    keyspot = 0
    while len(x) > 1:
        currchar = x[0]
        x = x[1:]
        answer += adjustchar(currchar, key[keyspot])
        keyspot += 1
        if keyspot == len(key):
            keyspot = 0
    print(answer)