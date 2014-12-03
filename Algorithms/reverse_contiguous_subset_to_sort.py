#!/usr/bin/env python3

""" Problem description:
You have an array of n distinct integers. Determine whether it is possible to sort the array by reversing exactly one contiguous segment of the array. For example, 1 [4 3 2] 5 => 1 [2 3 4] 5.
"""

""" Some variables for testing """
possible = [1, 2, 6, 5, 4, 3, 7, 8]
impossible = [1, 2, 6, 3, 4, 5, 7, 8]

def sort_by_reversing_subsegment(arr):
  pass

def main():
  print("Array: {}\n Possible: {}".format(possible,
    sort_by_reversing_subsegment(possible)))
  print("Array: {}\n Possible: {}".format(impossible,
    sort_by_reversing_subsegment(impossible)))

if __name__ == '__main__':
  main()
