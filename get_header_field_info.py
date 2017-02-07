#!/usr/bin/env python3.5
# encoding: utf-8
import sys


def main():
    if len(sys.argv) != 2:
        # Example
        # 1. ./xxxx.py 2327
        # 2. ./xxxx.py "2327,2343,3261,1343"
        print('Usage: %s $file_name' % sys.argv[0])
        sys.exit(2)

    file_name = sys.argv[1]
    print(file_name)
    print('[Line]\t Header Field')
    with open(file_name) as f:
        for i, line in enumerate(f):
            if line.find('header field') == -1:
                continue

            split_line = line.split()

            for j, hf in enumerate(split_line):
                if hf != 'header':
                    continue
                if split_line[j+1].startswith('field') is False:
                    continue
                print('[%d]\t %s' % (i+1, split_line[j-1]))
                # print(i, split_line[j-1], split_line[j], split_line[j+1])
    f.closed


if __name__ == '__main__':
    main()
