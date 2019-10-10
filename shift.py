import argparse
import os
import sys
import base64

def shift(bytear, f):
    for i in range(1, 26):
        decoded = ''
        for num in bytear:
            if num in range(65, 91):
                new = num + i
                if new > 90:
                    new = 65 + (new - 91)
                decoded += chr(new)
                # shift, append str(int) to decoded
            elif num in range(97, 123):
                new = num + i
                if new > 122:
                    new = 97 + (new - 123)
                decoded += chr(new)
                # shift, append str(int) to decoded
            else:
                decoded += chr(num)
        f.write(decoded)
    f.close()

def file_to_ascii(filename, mode):
    f = open("ctxts/" + filename, "r")    
    if f.mode == 'r':
        contents = f.read()
    
    bytear = []
    if mode == 0:
        for c in contents:
            bytear.append(ord(c))
    elif mode == 1:
        # base64 to decimal
        print('base64')
    elif mode == 2:
        # hex to decimal
        contents = str(int(contents, 16))
        for i in range(0, len(contents), 2):
            bytear.append(int(contents[i:i+2]))
        print(bytear)
    return bytear

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="ciphertext file")
    parser.add_argument("mode", help="0 - string, 1 - binary, 2 - hex")
    args = parser.parse_args()

    filename = args.filename
    mode = int(args.mode)
    bytear = file_to_ascii(filename, mode)
    
    if not os.path.exists('output'):
        os.mkdir('output')
    log = 'results' + filename[:2] + '.txt'
    f = open('output/' + log, 'w+')

    shift(bytear, f)
