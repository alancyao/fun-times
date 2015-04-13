#!/usr/bin/env python3
from data_structures.trie import *

""" Problem description:
You are given a permutation of the english alphabet (all lowercase) and a list of words. Sort the list of words alphabetically according to the permutation of the english alphabet.
"""

""" Some variables for testing """
permutation = "agdbecfhijklmnopqrstuvwxyz"
arr = ['zzzzz', 'goodday', 'goodbye', 'death', 'hello', 'hcllo']

def trie_sort(perm, arr):
  trie = Trie(arr)
  fringe = [('', trie.root)]
  out = []
  while fringe:
    cur_word, node = fringe.pop()
    if node.is_word:
      out.append(cur_word)
    for letter in permutation:
      if letter in node.children:
        fringe.append((cur_word + letter, node.children[letter]))
  return out[::-1]

def main():
  print(trie_sort(permutation, arr))

if __name__ == '__main__':
  main()
