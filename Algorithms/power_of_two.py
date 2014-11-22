#!/usr/bin/env python3
import sys

""" Problem description:
Calculate whether an integer is a power of 2 in at most 5 operations.
"""

def power_of_two(n):
  return (n != 0) and not ((n-1) & n )

def main():
  if len(sys.argv) == 1:
    print("Give an integer.")
    return
  try:
    print(power_of_two(int(sys.argv[1])))
  except:
    print("Invalid integer")

if __name__ == '__main__':
  main()
