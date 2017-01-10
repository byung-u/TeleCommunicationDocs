#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sys
from requests import get
from bs4 import BeautifulSoup


def main():
    if len(sys.argv) != 2:
        # Example
        # 1. ./xxxx.py 2327
        # 2. ./xxxx.py "2327,2343,3261,1343" 
        print('Usage: %s RFC_NUM' % sys.argv[0])
        sys.exit(2)

    rfc_num = sys.argv[1].split(',')
    total = len(rfc_num)
    for i, num in enumerate(rfc_num):
        num = num.strip()
        rfc_text = get_rfc_info(num)
        write_rfc_file(num, rfc_text)
        print("[%d/%d] rfc%s.txt" % (i+1, total, num))
    sys.exit(0)


def get_rfc_info(rfc_num):
    rfc_url = 'https://www.ietf.org/rfc/rfc%s.txt' % rfc_num

    r = get(rfc_url)
    if r.status_code != 200:
        print('get url failed, ' + rfc_url)
        sys.exit(2)

    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.text


def write_rfc_file(rfc_num, text):
    out_file = 'rfc%s.txt' % rfc_num
    fw = open(out_file, 'w')
    fw.write(text)
    fw.close()


'''
def parse_options():
    args = sys.argv[1:]
    rfc_number_from_file = False
    rfc_number = '0'

    while args and args[0].startswith('-'):
        if args[0] == '-r':
            rfc_number_from_file = True
            args = args[1:]
        elif args[0] == '-n':
            rfc_number = args[1]
            args = args[1:]
        elif args[0] in ('-h', '--help'):
            usage()
        else:
            raise SystemExit('Unrecognized options %s' % args[0])
        args = args[1:]

    if not args:
        usage()

    if rfc_number == '0' and rfc_number_from_file == False:
        usage()

    return Options(rfc_number_from_file = rfc_number_from_file,
                   rfc_number = rfc_number)

'''

if __name__ == '__main__':
    main()
