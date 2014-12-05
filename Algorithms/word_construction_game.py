#!/usr/bin/env python3
from data_structures.trie import *

""" Problem description:
Alice and Bob are playing the following game: they have a list of valid English words. They start with an initially empty word. First Alice adds a letter, then Bob adds a letter, and so on. At each step, the word must be a prefix of some valid English word. When one player is unable to add a letter, that player loses. Determine whether Alice can win the game.
"""

""" Some variables for testing """
words1 = ['excellent', 'excellings', 'exconvict', 'exist',
    'existance', 'exists', 'excellents']

def can_win_game(words):
  trie = Trie(words)


def main():
  pass

if __name__ == '__main__':
  main()
