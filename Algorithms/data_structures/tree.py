class TreeNode:
    def __init__(self, item=None, parent=None, children=[]):
        self.item = item
        self.parent = parent
        self.children = [TreeNode(x) for x in children]

    def insert_child(self, item):
        self.children.append(TreeNode(item, self))

class Tree:
    """ Tree with no sorting structure """
    def __init__(self, rootitem=None):
        self.root = TreeNode(rootitem)


