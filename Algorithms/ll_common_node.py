#!/usr/bin/env python3
from data_structures.linked_list import *

""" Problem description:
Provide an algorithm that determines whether two singly linked lists (perhaps cyclic) share any node in common.
"""

""" Some variables for testing """
a = LinkedList([1, 2, 3, 5, 7])
b = LinkedList([4, 6, 8, 9, 0, 10])
c = LinkedList([9, 9, 9, 9, 1])
s1 = SLinkedList([1, 2, 3, 4, 5])
s2 = SLinkedList([9, 8, 7, 7])
s2.tail.next = s1.head.next.next

def find_merge_node(lst1, lst2):
    """ Walk both lists to determine length.
    Then advance the longer list to the difference between the lengths.
    Advance both pointers at the same time, until a merge or the end
    is reached.
    Since this violates the LL invariants, we cannot use LL methods.
    """
    M, N = len(lst1), len(lst2)
    adv = abs(M-N)
    p1, p2 = lst1.head, lst2.head
    if M>N:
        for _ in range(adv):
            p1 = p1.next
    else:
        for _ in range(adv):
            p2 = p2.next
    while p1 and p2:
        if p1 is p2:
            return p1
        p1, p2 = p1.next, p2.next
    return None

def find_common_item_node(lst1, lst2):
  s = set([lst1.front()])
  tort = lst1.front_node().next
  hare = lst1.front_node().next.next
  while tort is not hare:
    s.add(tort.item)
    tort = tort.next
    hare = hare.next.next
  if lst2.front() in s:
    return lst2.front()
  tort = lst2.front_node().next
  hare = lst2.front_node().next.next
  while tort is not hare:
    if tort.item in s:
      return tort.item
    tort = tort.next
    hare = hare.next.next
  return None

def main():
  print('a: ', a)
  print('b: ', b)
  print('c: ', c)
  print('a, b: ', find_common_item_node(a, b))
  print('a, c: ', find_common_item_node(a, c))
  print('merge node [should be 3]: ', find_merge_node(s1, s2))

if __name__ == '__main__':
  main()
