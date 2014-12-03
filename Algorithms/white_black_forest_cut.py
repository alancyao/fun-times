#!/usr/bin/env python3
from data_structures.tree import *

""" Problem description:
You have a tree with n vertices, some white and some black. You would like to cut some of the tree edges so that each tree in the resulting forest will have exactly one black node. Count the number of ways to do so.
"""

def forest_cut(t):
    """ Counts the number of ways to cut a tree into a forest
    in which each component has exactly one black node
    """

def main():
    t = Tree('white')
    t.root.insert_child('white')
    t.root.insert_child('white')
    t.root.insert_child('white')
    t.root.insert_child('black')
    for child in t.root.children:
        child.insert_child('white')
        child.insert_child('black')

if __name__ == '__main__':
  main()
