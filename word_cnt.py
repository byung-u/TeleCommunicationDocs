#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Use 'https://tools.ietf.org' instead of this script.
import sys
import glob
from collections import Counter

not_check = [
        "from", "on", "If", "if", "this", "by", "RFC", "with",
        "are", "as", "an", "not", "or", "it", "The", "be", "for", "that",
        "and", "is", "in", "of", "to", "a", "A", "the", "at",
        "will", "no", "which", "when", "does", "but",
        "June", "2002", 'et.', 'al.', 'Rosenberg,', "SIP:"  # rfc3261
        'those', 'would', 'It',
        ]


def main():
    if len(sys.argv) != 2:
        # Example
        # 1. ./xxxx.py 2327
        # 2. ./xxxx.py "2327,2343,3261,1343"
        print('Usage: %s RFC_NUM' % sys.argv[0])
        sys.exit(2)

    input_file_name = './rfc%s' % sys.argv[1]
    entries = glob.glob('./*.txt')
    for file_name in entries:
        if input_file_name in file_name:
            conunt_word(file_name)
            break

    sys.exit(0)


def conunt_word(file_name):
    f = open(file_name, 'r')
    wc = Counter(f.read().split())
    for item in sorted(wc.items(), key=lambda pair: pair[1], reverse=False):
        if any(x in item[0] for x in not_check):
            continue
        print("{}\t{}".format(*item))

    print('----------------------')
    print('Total: ', len(list(wc)))
    f.close()


if __name__ == "__main__":
    main()
