import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="ciphertext file")
    args = parser.parse_args()

    filename = args.filename
    f = open("ctxts/" + filename, "r")
    if f.mode == 'r':
        contents = f.read()
    f.close()

    filepath = 'output/results' + filename[:2] + '.txt'
    if not os.path.exists('output'):
        os.mkdir('output')
    f = open(filepath, 'w+')
    
    for i in range(1, len(contents)):
       f.write(contents[i:]) 
    f.close()

    max_matches = 0
    max_line = 0
    with open(filepath) as fp:
        for i, line in enumerate(fp):
            matches = 0
            for j in range(len(line)):
                if line[j] == contents[j]:
                    matches += 1
                    if matches > max_matches:
                        max_matches = matches
                        max_line = j
    print(max_line)
    # compare everything to contents 
