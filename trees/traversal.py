from tree import *

# Traversing the tree root first
def preorder(root):
    if root == None:
        return None
    print root.val
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print root.val
    inorder(root.right)

def postorder(root):
    if root == None:
        return None
    postorder(root.left)
    postorder(root.right)
    print root.val

if __name__ == "__main__":
    bst = generate_bst()
    inorder(bst)
