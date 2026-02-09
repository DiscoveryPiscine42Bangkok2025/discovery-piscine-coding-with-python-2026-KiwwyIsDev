#!/usr/bin/env python3

import sys, re

argv = sys.argv
argc = len(argv) - 1

if argc >= 2:
    print(len(re.findall(argv[1], argv[2])))
else:
    print("none")