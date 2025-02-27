#!/usr/bin/env python
# -*- coding: utf-8 -*-
#"""
#Created on Tue Feb 25 16:05:35 2025

#@author: KateClancy
#"""

import sys
import re

def main(argv):
    pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')
    for line in sys.stdin:
        match = pattern.findall(line)
        if match:
            for word in pattern.findall(line):
                print(word + "\t1")

if __name__ == "__main__":
    main(sys.argv)