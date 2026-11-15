#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        for word in line.split():
            word = word.lower().rstrip(',.')
            if word:
                print(f"{word}\t1")

if __name__ == "__main__":
    main()
