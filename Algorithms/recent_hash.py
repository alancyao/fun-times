#!/usr/bin/env python3
from data_structures.linked_list import *

""" Problem description:
Provide a hash table-like data structure which supports the following queries in constant time: set(key, value), get(key), delete(key), and last(). The first three are self-explanatory. The last() query does not modify state, and returns the last key which was set or get, ignoring deleted keys.
"""

class RecentDict():
    def __init__(self):
        self.d = {}
        self.recent = LinkedList()

    def set(self, key, value):
        if key in self.d:
            self.recent.delete(self.d[key][1])
        new = self.recent.insertFront(key)
        self.d[key] = (value, new)

    def get(self, key):
        if key in self.d:
            self.recent.delete(self.d[key][1])
            self.recent.insertFront(key)
            return self.d[key][0]
        return None

    def delete(self, key):
        if key in self.d:
            self.recent.delete(self.d[key][1])
            del self.d[key]

    def last(self):
        return self.recent.front()

def main():
    """ Runs some basic sanity checks """
    d = RecentDict()
    d.set('a', 'b')
    d.set('c','d')



if __name__ == '__main__':
    main()
