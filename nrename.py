#!/usr/bin/env python3
import os
import re
from optparse import OptionParser


if __name__ == '__main__':
    parser = OptionParser(usage="%prog [options] [files]")
    parser.add_option('-p', '--prefix', dest='prefix', default='', help='specify the prefix of new names.')
    parser.add_option('-s', '--suffix', dest='suffix', default='', help='specify the suffix of new names.')
    (options, args) = parser.parse_args()

    REGEX_NAME = re.compile(r"\.?([^/\.\n]+)[^/\n]*?$")
    renamed = 0
    for i, name in enumerate(args):
        match = REGEX_NAME.search(name)
        parent = name[:match.start(1)]
        extension = name[match.end(1):]
        new_name = parent + options.prefix + str(i) + options.suffix + extension
        try:
            os.rename(name, new_name)
            print('Renamed: ', name, '->', new_name)
            renamed += 1
        except:
            print('Failed: ', name, '->', new_name)
    print('Renamed', renamed, 'of', len(args), 'file(s) or directorie(s).')
