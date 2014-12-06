#!/usr/bin/env python3
from data_structures.linked_list import *

""" Problem description:
Reverse a singly linked list.
"""

""" Some variables for testing """
a = SLinkedList([1,2,3,4,5,6])

def reverse_ll(lst):
  """ Constructive reverse. """
  stack = []
  for item in lst:
    stack.append(item)
  return SLinkedList([stack.pop() for _ in range(len(stack))])

def reverse_ll_inplace(lst):
  """ In place. """
  if not lst.head:
    return lst
  stack, cur = [], lst.head
  while cur.next:
    stack.append(cur)
    cur = cur.next
  lst.head = cur
  while stack:
    cur.next = stack.pop()
    cur = cur.next
  lst.tail = cur
  cur.next = None
  return lst

def main():
  print('a: ', a)
  print('Constructive reverse: ', reverse_ll(a))
  print('In place reverse: ', reverse_ll_inplace(a))
  pass

if __name__ == '__main__':
  main()
