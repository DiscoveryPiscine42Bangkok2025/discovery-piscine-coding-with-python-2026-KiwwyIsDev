#!/usr/bin/env python3

import sys

argv = sys.argv
argc = len(argv) - 1

# print(argv[1].count("z"))

if argc == 1 and argv[1].count("z") > 0:
    print("z" * argv[1].count("z"))
else:
    print("none")