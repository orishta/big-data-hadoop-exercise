#!/usr/bin/env python3
import sys
import heapq
from itertools import groupby
from operator import itemgetter

def main():
    data = (line.rstrip('\n').split('\t', 1) for line in sys.stdin)
    top_words = []

    for word, group in groupby(data, itemgetter(0)):
        count = sum(int(value) for _, value in group)
        heapq.heappush(top_words, (count, word))

        if len(top_words) > 3:
            heapq.heappop(top_words)

    for count, word in sorted(top_words, reverse=True):
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()
