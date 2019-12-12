#!/usr/bin/env python3
import sys


# zalecane czytanie linii z stdin
def print_line_from_stdin_recommended():
    for line in sys.stdin:
        # line == 'a\n'
        line = line.rstrip('\n') # line == 'a'
        print(line) # lub rób coś innego z tą linią

# niezalecana wersja
def print_line_from_stdin_not_recommended():
    while True:
        try:
            line = input()
        except EOFError:
            break
        print(line)


def main():
    print_line_from_stdin_recommended()

if __name__ == '__main__':
    main()
