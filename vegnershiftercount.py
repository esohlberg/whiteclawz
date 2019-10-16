import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = 'ctxts/' + args.filename
    x = open(filename, 'r').read()

    besti = 0
    maxmatches = 0

    secondbesti = 0
    secondmax = 0

    thirdbesti = 0
    thirdmax = 0

    y = ''
    for carz in x:
        if carz.isalnum():
            y += carz
    
    x = y

    for i in range (1, len(x)):
        currmax = 0
        shiftedx = x
        paddedx = x
        for j in range(0, i):
            shiftedx = '0' + shiftedx 
            paddedx = paddedx + '0'
        #print(shiftedx)
        #print(paddedx)
        for k in range (0, len(shiftedx)):
            if shiftedx[k] == paddedx[k]:
                currmax += 1
        if currmax > thirdmax:
            if currmax > secondmax:
                if currmax > maxmatches:
                    maxmatches = currmax
                    besti = i
                else:
                    secondmax = currmax
                    secondbesti = i
            else:
                thirdmax = currmax
                thirdbesti = i
    print("Matches: " + str(maxmatches) + "Shift number: " + str(besti))
    print("Matches: " + str(secondmax) + "Shift number: " + str(secondbesti))
    print("Matches: " + str(thirdmax) + "Shift number: " + str(thirdbesti))

        

