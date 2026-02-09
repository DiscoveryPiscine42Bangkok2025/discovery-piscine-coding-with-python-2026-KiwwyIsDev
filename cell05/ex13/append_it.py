#!/usr/bin/env python3


import sys

argv = sys.argv
argv.pop(0)
argc = len(argv)

if argc > 0:
    for arg in argv:
        if arg.endswith("ism"):
            continue
        print(f"{arg}ism")
else:
    print("none")