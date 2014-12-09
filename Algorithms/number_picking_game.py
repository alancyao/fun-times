#!/usr/bin/env python3
from operator import itemgetter
""" Problem description:
You have a list of positive integers, and you're playing a game with your friend. Unfortunately, your friend isn't too enthusiastic, so whenever it is his turn, he just takes the first number in the list. On your turn, you can take any arbitrary number in the list. Given that you go first, what is the maximum sum you can take?
"""

""" Some variables for testing """
a = [1, 9, 3, 8, 6, 6, 10, 11]

def index_max(arr):
  return max(range(len(arr)),key=arr.__getitem__)

def find_max_game_sum(a):
  """ Greedy approach. First notice that on our turn, we will
  either take the array maximum, or the first number in the list.
  Maximize the point differential between these two choices.
  """
  total = 0
  while len(a) > 1:
    m = index_max(a)
    if a[m]-a[0] > a[0]-a[1]: #Take the max
      print('taking {}'.format(a[m]))
      total += a[m]
      del a[m]
    else:
      print('taking {}'.format(a[0]))
      total += a[0]
      del a[0]
    del a[0]
  if a:
    total += a.pop()
  return total

def main():
  print('a: ', a)
  print('max game sum: ', find_max_game_sum(a))

if __name__ == '__main__':
  main()
