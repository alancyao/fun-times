#!/usr/bin/env python3

""" Problem description:
You have an array consisting of n integers. Count the number of ways to split all the elements of the array into three contiguous parts so that the sum of elements in each part is the same.
"""

""" Some variables for testing """
a = [1, 2, 3, 0, 3]
b = [0, -1, 1, 0]
c = [4, 1]

def contiguous_3sum(arr):
    l = len(arr)
    possible = [(x, y) for x in range(1,l) for y in range(1,l) if x < y]
    n = 0
    for x, y in possible:
        if sum(arr[:x]) == sum(arr[x:y]) == sum(arr[y:]):
            n += 1
    return n

def main():
    print('a: ', a, ' sum: ', contiguous_3sum(a))
    print('b: ', b, ' sum: ', contiguous_3sum(b))
    print('c: ', c, ' sum: ', contiguous_3sum(c))

if __name__ == '__main__':
  main()
