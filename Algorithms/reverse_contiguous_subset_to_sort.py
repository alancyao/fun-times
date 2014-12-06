#!/usr/bin/env python3

""" Problem description:
You have an array of n distinct integers. Determine whether it is possible to sort the array by reversing exactly one contiguous segment of the array. For example, 1 [4 3 2] 5 => 1 [2 3 4] 5.
"""

""" Some variables for testing """
possible = [1, 2, 6, 5, 4, 3, 7, 8]
impossible = [1, 2, 6, 3, 4, 5, 7, 8]

def can_sort_by_reversing_subsegment(arr):
  s = sorted(arr)
  oop = [x for x in enumerate(arr) if (x[1] != s[x[0]])]
  return [x[1] for x in oop[::-1]] == s[oop[0][0]:oop[-1][0]+1]

def main():
  print("Array: {}\n Possible: {}".format(possible,
    can_sort_by_reversing_subsegment(possible)))
  print("Array: {}\n Possible: {}".format(impossible,
    can_sort_by_reversing_subsegment(impossible)))

if __name__ == '__main__':
  main()
