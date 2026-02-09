#!/usr/bin/env python3

import sys

argv = sys.argv
argc = len(argv) - 1

if argc <= 0:
    print("none")
else:
    # print(" ".join(argv[1:]))
    print(argv[1])