#!/usr/bin/env python
# -*- coding: utf-8 -*-
#"""
#Created on Tue Feb 25 16:05:35 2025

#@author: KateClancy
#"""

import sys
import re

def main(argv):
    pattern = re.compile(r"\b([A-Z]{1,9})\b\s/")
    for line in sys.stdin:
        # For each line, find all matches of the HTTP method followed by space and '/'
        for word in pattern.findall(line):
            # Print only the captured HTTP method with the desired prefix and count 1
            print("LongValueSum:" + word + "\t1")

if __name__ == "__main__":
    main(sys.argv)