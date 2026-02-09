#!/usr/bin/env python3

import sys 

argv = sys.argv
argv.pop(0)
argc = len(argv)

def shrink(text: str):
    print(text[:8])

def enlarge(text: str):
    Z = "Z" * (8 - len(text))
    print(text + Z)

if argc > 0:
    for arg in argv:
        if len(arg) > 8:
            shrink(arg)
        else:
            enlarge(arg)
else:
    print("none")