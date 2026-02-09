#!/usr/bin/env python3

import sys


argv = sys.argv
argc = len(sys.argv) - 1
if argc != 1:
    print("none")
else:
    print(argv[1].upper())