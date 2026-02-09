#!/usr/bin/env python3

import sys

def downcase_it(text: str):
    return text.lower()

argv = sys.argv
argv.pop(0)
argc = len(argv)

if argc == 0:
    print("none")
else:
    for arg in argv:
        print(downcase_it(arg))