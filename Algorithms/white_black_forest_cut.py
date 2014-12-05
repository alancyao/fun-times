#!/usr/bin/env python3
from data_structures.tree import *

""" Problem description:
You have a tree with n vertices, some white and some black. You would like to cut some of the tree edges so that each tree in the resulting forest will have exactly one black node. Count the number of ways to do so.
"""

def forest_cut(t):
  """ Counts the number of ways to cut a tree into a forest
  in which each component has exactly one black node
  """
  def cut(node, black_parent):
    if node.item == 'white':
      if not node.children:
        return black_parent
      if black_parent:
        return (sum([cut(c, False) for c in node.children]) +
            sum([cut(c, True) for c in node.children if c.item != 'black']))
      else:
        return sum([cut(c, False) for c in node.children])
    else: #black_parent must be false
      if not node.children:
        return 1
      return (sum([cut(c, False) for c in node.children]) +
          sum([cut(c, True) for c in node.children if c.item != 'black']))
  return cut(t.root, False)

def main():
  t1 = Tree('black')
  t1.root.insert_child('white')
  for child in t1.root.children:
    child.insert_child('white')
    child.insert_child('black')
  #t1.root.children[0].children[0].insert_child('black')
  print(t1)
  print('Num cuts: {}'.format(forest_cut(t1)))

if __name__ == '__main__':
  main()
