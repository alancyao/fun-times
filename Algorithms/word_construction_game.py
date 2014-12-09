#!/usr/bin/env python3
from data_structures.trie import *

""" Problem description:
Alice and Bob are playing the following game: they have a list of valid English words. They start with an initially empty word. First Alice adds a letter, then Bob adds a letter, and so on. At each step, the word must be a prefix of some valid English word. When one player is unable to add a letter, that player loses. Determine whether Alice can win the game.
"""

""" Some variables for testing """
words1 = ['excellent', 'excellings', 'exconvict', 'exist',
    'existance', 'exists', 'excellents']
words2 = ['hell', 'hello']
words3 = ['yo', 'yoyo']

def can_win_game(words):
    trie = Trie(words)
    def dp(node, depth):
        if not node.children:
            return depth%2
        return any([dp(c, depth+1) for c in node.children.values()])
    return dp(trie.root, 0)

def main():
    print("words: {}\ncan win: {}".format(words1, can_win_game(words1)))
    print("words: {}\ncan win: {}".format(words2, can_win_game(words2)))
    print("words: {}\ncan win: {}".format(words3, can_win_game(words3)))

if __name__ == '__main__':
  main()
