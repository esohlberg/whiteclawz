import argparse


if __name__ == '__main__':
  files = [f for f in os.listdir('.') if os.path.isfile(f)]
  for f in files:
    print(f)
  parser = argparse.ArgumentParser()
  parser.add_argument("filename")
  args = parser.parse_args()
  #f = open('ctxts\' + args.filename, 'r')
  #print(f.read())