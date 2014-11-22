#!/usr/bin/env python3

int_list = [1,2,3,5,6,9,13,16,61,34,33,25,57,35,12]

def two_sum(lst, n):
  """ Finds the two integers in lst that sum to n """
  s = set(lst)
  for i in lst:
    if (n-i) in s:
      if i == n-i:
        return lst.count(i) > 1
      return i, (n-i)

def three_sum(lst, n):
  """ Finds the three integers in lst that sum to n """
  for i, num in enumerate(lst):
    two = two_sum(lst[:i] + lst[i+1:], n-num)
    if two:
      return two + (num,)

def main():
  print('List: ' + str(int_list))
  print('Two sum of 50:')
  print(two_sum(int_list, 50))
  print('Three sum of 53:')
  print(three_sum(int_list, 53))

if __name__ == '__main__':
  main()
