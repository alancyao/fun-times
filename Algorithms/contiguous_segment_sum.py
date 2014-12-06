#!/usr/bin/env python3

""" Problem description:
Provide an algorithm to determine whether any contiguous segment of an array sums to a particular target value.
"""

""" Some variables for testing """
a = [5, 6, 2, 3, 4, 7, 9, 10]

def cumsum(arr):
  tot, out = 0, []
  for x in arr:
    tot += x
    out.append(tot)
  return out

def contiguous_subset_sum(arr, n):
  """ Returns whether there is a segment that sums to n if
  they exist. Otherwise, returns False """
  c = cumsum(arr)
  s = set(c)
  sub = [x-n for x in c]
  return any([x in s for x in sub])

def main():
  print('a: ', a)
  print('sum to 30: ', contiguous_subset_sum(a, 30))
  print('sum to 5: ', contiguous_subset_sum(a, 5))
  print('sum to 12: ', contiguous_subset_sum(a, 12))

if __name__ == '__main__':
  main()
