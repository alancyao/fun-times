#!/usr/bin/env python3
import sys
a = [int(x) for x in sys.stdin.readlines()[1:]]

""" Problem description:
The task is to find the length of the longest subsequence in a given array of integers such that all elements of the subsequence are sorted in ascending order.
In the first line of input, there is a single number N
In the next N lines input the value of a[i]
"""

def longest_increasing_subsequence(arr):
  if not arr:
    return 0
  l = [1]*len(arr)
  for i in range(1,len(arr)):
    for j in range(i):
      if arr[j]<arr[i] and l[j]+1>l[i]:
        l[i] = l[j]+1
  return max(l)

print(longest_increasing_subsequence(a))
