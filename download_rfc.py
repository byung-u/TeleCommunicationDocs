#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# Use 'https://tools.ietf.org' instead of this script.
import sys
from requests import get
from bs4 import BeautifulSoup

import glob
import os
import re


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

    rename_rfc_txt()

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


def rename_rfc_txt():
    r = re.compile(r'\./rfc[0-9][0-9][0-9][0-9]\.txt')  # ./rfc3261.txt

    entries = glob.glob('./*.txt')
    for entry in entries:
        m = r.match(entry)
        if m is None:
            continue

        rfc_num, title = get_rfc_title(entry)
        if title is None:
            print('get_rfc_title failed, file=', entry)
            continue
        new_file_name = 'rfc%s_%s.txt' % (rfc_num, title)
        os.rename(entry, new_file_name)
        print('[rename] %s -> %s' % (entry, new_file_name))


def get_rfc_title(file_name):

    r = re.compile(r'[1-2][0-9][0-9][0-9]')  # 1000~2999
    title = []
    with open(file_name) as f:
        for line in f:
            if line.strip().startswith('RFC '):
                raw_title = line.split(' ')
                m = r.match(raw_title[-1])
                if m is None:
                    title.clear()
                    continue

                for t in raw_title[2:-2]:
                    if len(t) > 0:
                        title.append(t.replace('/', '__'))

                if len(title) == 0:
                    title.clear()
                    continue
                f.closed
                return raw_title[1], '_'.join(title)
    f.closed
    return None


if __name__ == '__main__':
    main()
