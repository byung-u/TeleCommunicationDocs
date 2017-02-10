#!/usr/bin/env python3.5
# encoding: utf-8
import sys

import re

def lreplace(pattern, sub, string):
    """
    Replaces 'pattern' in 'string' with 'sub' if 'pattern' starts 'string'.
    """
    return re.sub('^%s' % pattern, sub, string)


def rreplace(pattern, sub, string):
    """
    Replaces 'pattern' in 'string' with 'sub' if 'pattern' ends 'string'.
    """
    return re.sub('%s$' % pattern, sub, string)


def main():
    if len(sys.argv) != 2:
        # Example
        # 1. ./xxxx.py 2327
        # 2. ./xxxx.py "2327,2343,3261,1343"
        print('Usage: %s $file_name' % sys.argv[0])
        sys.exit(2)

    file_name = sys.argv[1]
    out_file_name = '%s.modi.txt' % file_name
    fw = open(out_file_name, 'w')
    print(file_name)
    temp_buf = []
    with open(file_name) as f:
        for i, line in enumerate(f):
            if line.startswith('      '):
                line = lreplace('      ', '', line)
            elif line.startswith('   '):
                line = lreplace('   ', '', line)
            line =  line[:-1]
            temp_buf.append(line)

    fw.write(''.join(temp_buf))
    fw.close()
    f.closed


if __name__ == '__main__':
    main()
