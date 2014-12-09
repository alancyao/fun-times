from collections import deque

class TreeNode:
    def __init__(self, item=None, parent=None, children=[]):
        self.item = item
        self.parent = parent
        self.children = [TreeNode(x) for x in children]

    def insert_child(self, item):
        self.children.append(TreeNode(item, self))
        return self.children[-1]

    def __str__(self):
        return "TreeNode: {}".format(self.item)

class Tree:
    """ Tree with no sorting structure """
    def __init__(self, rootitem=None):
        self.root = TreeNode(rootitem)

    def __str__(self):
        """ Prints rows of tree with no connections """
        s = ""
        q, lvl = deque([(self.root, 0)]), 0
        while q:
            node, nlvl = q.popleft()
            if nlvl > lvl:
                lvl = nlvl
                s += "\n"
            s += str(node) + " "
            for child in node.children:
                q.append((child, lvl+1))
        return s

    def bfs(self):
        """ Yields nodes in BFS order """
        q = deque([self.root])
        while q:
            n = q.popleft()
            yield n
            for c in n.children:
                q.append(c)

    def dfs(self):
        """ Yields nodes in DFS order """
        q = deque([self.root])
        while q:
            n = q.pop()
            yield n
            for c in n.children:
                q.append(c)




