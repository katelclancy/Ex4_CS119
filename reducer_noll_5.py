#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            word_str = str(current_word)
            if word_str.startswith("LongValueSum:"):
                word_str = word_str.replace("LongValueSum:","")
            print ('%s\t%s' % (word_str, current_count))
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    if word_str.startswith("LongValueSum:"):
        word_str = word_str.replace("LongValueSum:","")
    print ('%s\t%s' % (word_str, current_count))
