#!/usr/bin/env python3
from data_structures.trie import *

"""Provide an algorithm to efficiently answer queries as follows: you are given a dictionary of legal English words. Each query provides a 4x4 grid of letters. Find the longest English word which forms a path in the grid (moving orthogonally and diagonally, possibly using the same space multiple times).

The given example should output "neatness"
"""

words_file = '/usr/share/dict/words'
word_string = """ness
tabd
shgf
aird"""

with open(words_file) as f:
  words = f.read().split()[::100] + ['neatness']

def find_longest_path(word_trie, grid):
  fringe = [(x, y, grid[x][y]) for x in range(4) for y in range(4)]
  longest = ""
  while fringe:
    x, y, current_word = fringe.pop()
    if current_word in word_trie:
      if word_trie.find(current_word, True) and (len(current_word) > len(longest)):
        longest = current_word
      for neighbor in neighbors(x,y,current_word,grid):
        fringe.append(neighbor)
  return longest

def neighbors(x, y, current_word, grid):
  n = len(grid)
  arr = []
  for i in range(x-1,x+2):
    for j in range(y-1,y+2):
      if i >= 0 and i < n and j >= 0 and j < n and (i,j) != (x,y):
        arr.append((i,j,current_word+grid[i][j]))
  return arr

def main():
  grid = word_string.split('\n')
  trie = Trie(words)
  print(find_longest_path(trie, grid))

if __name__ == '__main__':
  main()
