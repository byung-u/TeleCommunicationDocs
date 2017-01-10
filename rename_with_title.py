#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import os
import re
import sys
import glob


def main():
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
        print('rename %s -> %s' % (entry, new_file_name))
    sys.exit(0)


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
