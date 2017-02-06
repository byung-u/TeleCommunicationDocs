#!/usr/bin/env python3.5
# encoding: utf-8
import sys
import io


def main():
    if len(sys.argv) != 2:
        # Example
        # 1. ./xxxx.py 2327
        print('Usage: %s $file_name' % sys.argv[0])
        sys.exit(2)

    file_name = sys.argv[1]
    out_file_name = '%s.modi' % file_name
    fw = open(out_file_name, 'w')
    with io.open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            # Python unicode error occurred.
            # I don't wanna waste time for debugging.
            # Unicode error -> replace to similar ascii char.
            line = line.replace(u'\xa0', u' ').replace(u'\u2013', u'-').replace(u'\u2122', u'TM').replace(u'\xae', u'(R)').replace(u'\xb0', u' ').replace(u'\u2019', u'\'').replace(u'\u201d', u'\'').replace(u'\xb4', u'\'').replace(u'\u2028', u'\\n').replace(u'\xb1', '+-').replace(u'\u2026', u'...')
            # .replace(u'\u2122', u'TM')
            # .replace(u'\xb4', u'TM')
            fw.write(line)
    fw.close()
    f.closed


if __name__ == '__main__':
    main()
