#!/usr/bin/env python3
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
    get_hearder_field(file_name)

def get_hearder_field(file_name):
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
                header_field = split_line[j-1]
                header_field = header_field.replace('\'','').replace('(','').replace(')','').replace(':','')
                if header_valid_check(header_field) is False:
                    continue
                print('%s +%d\t %s' % (file_name, i+1, header_field))
                # print(i, split_line[j-1], split_line[j], split_line[j+1])
    f.closed

def header_valid_check(keyword):
    not_allow_keyword = ['to', 'SIP', 'uri', 'tag', 'such', 'unknown', 
            'yes', 'the', 'that', 'of', 'these', 'following', 'this', 'other',
            'whole', 'some', 'those', 'a']

    if keyword in not_allow_keyword:
        return False
    else:
        return True

if __name__ == '__main__':
    main()
