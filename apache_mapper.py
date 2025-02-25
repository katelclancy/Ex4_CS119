# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:05:35 2025

@author: KateClancy
"""
#!/usr/bin/env python
"""apache_mapper.py"""

import sys, re

def main(argv):
    requestdict = {}
    line = sys.stdin.readline()
    pattern = re.compile(r"\b([A-Z]{1,9})\b\s/")
    try:
        while line:
            for word in pattern.findall(line):
                print("LongValueSum:" + word + "\t" + "1")
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)