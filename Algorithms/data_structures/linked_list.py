class ListNode:
    def __init__(self, item, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

    def _delete(self):
        """ Internal delete method. Should not be
        called from outside LinkedList otherwise
        length of list will be inaccurate.
        """
        self.prev.next = self.next
        self.next.prev = self.prev

    def insertAfter(self, item):
        new = ListNode(item, self, self.next)
        self.next.prev = new
        self.next = new

class LinkedList:
    """ Doubly linked list """
    def __init__(self, lst=None):
        self.sentinel = ListNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.N = 0
        if lst:
            for item in lst:
                self.insertBack(item)

    def __len__(self):
        return self.N

    def __str__(self):
        return str([x for x in self])

    def __iter__(self):
        cur = self.sentinel.next
        while cur != self.sentinel:
            yield cur.item
            cur = cur.next

    def insertBack(self, item):
        """ Inserts item into the back of the list """
        self.sentinel.prev.insertAfter(item)
        self.N += 1

    def insertFront(self, item):
        """ Inserts item into the front of the list """
        self.sentinel.insertAfter(item)
        self.N += 1

    def delete(self, lstnode):
        """ Given a ListNode, remove it from the list """
        if lstnode is self.sentinel:
            raise Exception('Cannot delete the sentinel')
        lstnode._delete()
        self.N -= 1

    def find(self, item):
        """ Get the list node that contains item and return it.
        If the list node doesn't exist, return None
        """
        cur = self.sentinel.next
        while cur is not self.sentinel:
            if cur.item == item:
                return cur
            cur = cur.next
        return None

    def remove_item(self, item):
        """ Find and remove the first instance of item in the list.
        Returns the item if found, else None.
        """
        node = self.find(item)
        if node:
            self.delete(node)
            return node.item
        else:
            return None

    def front_node(self):
        """ Front node of the list """
        return self.sentinel.next if self.N != 0 else None

    def back_node(self):
        """ Back node of the list """
        return self.sentinel.prev if self.N != 0 else None

    def front(self):
        """ Front item of the list """
        return self.sentinel.next.item

    def back(self):
        """ Back item of the list """
        return self.sentinel.prev.item

class SListNode:
    def __init__(self, item, next=None):
        self.item, self.next = item, next

    def insert_after(self, item):
        self.next = SListNode(item, self.next)
        return self.next

    def delete_after(self):
        if self.next:
            self.next = self.next.next

class SLinkedList:
    """ Very basic singly linked list. Also has a tail pointer. """
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        if lst:
            for item in lst:
                self.insert_back(lst)

    def __len__(self):
        if not self.head:
            return 0
        if not self.head.next:
            return 1
        N, tort, hare = 1, self.head.next, self.head.next.next
        while tort and (tort is not hare):
            N += 1
            tort = tort.next
            if hare and hare.next:
                hare = hare.next.next
        return N

    def insert_back(self, item):
        if self.tail:
            self.tail = self.tail.insert_after(item)
        else:
            insert_front(self, item)

    def insert_front(self, item):
        self.head = SListNode(item, self.head)


