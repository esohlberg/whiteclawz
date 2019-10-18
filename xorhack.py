import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename1")
    parser.add_argument("filename2")
    parser.add_argument("currkey")
    args = parser.parse_args()
    filename1 = 'ctxts/' + args.filename1
    filename2 = 'ctxts/' + args.filename2

