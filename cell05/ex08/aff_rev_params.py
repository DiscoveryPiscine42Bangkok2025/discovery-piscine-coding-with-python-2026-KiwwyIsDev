#!/usr/bin/env python3

import sys

argv = sys.argv
argv.pop(0)

if len(argv) >= 2:
    for i in reversed(argv):
        print(i)
else:
    print("none")