#!/usr/bin/env python3
import sys

def run_max_subarray():
  """Input:
  First line of the input has an integer T. T cases follow Each test case begins with an integer N. In the next line, N integers follow.
  Output:
  2 space separated integers denoting the maximum contiguous and non-contiguous subarray. At least one integer should be selected and put into the subarrays (this may be required in cases where all elements are negative).
  """
  for line in sys.stdin.readlines()[2::2]:
    arr = [int(x) for x in line.split(' ')]
    print(max_contiguous_subarray(arr), max_subarray(arr))

def max_contiguous_subarray(arr):
  m_i, m, pos = 0, 0, False
  for x in arr:
    if x >= 0: pos = True
    m_i = max(0, m_i+x)
    m = max(m, m_i)
  if not pos:
    return max(arr)
  return m

def max_subarray(arr):
  tot, pos = 0, False
  for x in arr:
    if x >= 0:
      pos = True
      tot += x
  if not pos:
    return max(arr)
  return tot

def closest_numbers(arr):
  s = sorted(arr)
  diffs = [abs(s[x] - s[x+1]) for x in range(len(s)-1)]
  ind, val = min(enumerate(diffs), key=lambda x:x[1])
  return s[ind], s[ind+1]

def main():
  #run_max_subarray()

if __name__ == '__main__':
  main()
