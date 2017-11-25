from traversal import *
from lca import *

class TreeNode:
    # Binary Tree
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val

def generate_bt():
    bt = TreeNode(1)
    bt.left = TreeNode(2)
    bt.right = TreeNode(3)
    bt.left.left = TreeNode(4)
    bt.left.right = TreeNode(5)
    bt.right.left = TreeNode(6)
    bt.right.right = TreeNode(7)
    return bt

def generate_bst():
    bst = TreeNode(4)
    bst.left = TreeNode(2)
    bst.right = TreeNode(6)
    bst.left.left = TreeNode(1)
    bst.left.right = TreeNode(3)
    bst.right.left = TreeNode(5)
    bst.right.right = TreeNode(7)
    return bst

if __name__ == "__main__":
    bt = generate_bt()
    # postorder(root)

    bst = generate_bst()
    postorder(bst)
    # print lca(root, 4, 2).val

    # bt
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7

    # bst
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7
