#!/usr/bin/env python3

import sys

argv = sys.argv
argv.pop(0)
argc = len(argv)


if argc == 2:
    argv = list(map(int, argv))
    arr = [x for x in range(argv[0], argv[1] + 1)]
    print(arr)
else:
    print("none")