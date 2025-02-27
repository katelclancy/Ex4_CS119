#!/usr/bin/env python
# -*- coding: utf-8 -*-
#"""
#Created on Tue Feb 25 16:05:35 2025

#@author: KateClancy
#"""

import sys
import re

def main(argv):
    pattern = re.compile(r'"\s(\d)\d{2}\s')
    for line in sys.stdin:
        if not line:
            continue
        match = pattern.findall(line)
        if match:
            for word in match:
                response_cat = str(word)
                print(f"{response_cat}**\t1")
        else:
            sys.stderr.write(f"Warning: No response code found in line: {line}\n")

if __name__ == "__main__":
    main(sys.argv)