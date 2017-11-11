
class TreeNode:
    # Binary Tree
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


# Compute the lowest common ancestor for a binary tree for two given nodes

###### CONDITION ########:
# Assuming that both the ndoes are present in the tree
def lca(root, n1, n2):
    # Recursive approach
    # The function tries to return the pointer to the lca
    # Base case:
    if root == None:
        return None

    # When a TreeNode gets invoked, it first checks whether its value matches any of the two given nodes
    # If the TreeNode is one of the nodes itself, then it has to be the ancestor of the other (Assuming itself as the root)
    if root.val == n1 or root.val == n2:
        return root

    # Otherwise, it delegates the work to figure out the lca to its children
    left_output = lca(root.left, n1, n2)
    right_output = lca(root.right, n1, n2)

    # If both the children return some pointer, the node knows that the lca is the node itself so it returns itself
    if left_output and right_output:
        return root

    # Or else it passes on the pointer returned by one of its children or else returns None
    if left_output:
        return left_output
    elif right_output:
        return right_output
    else:
        return None










# Traversing the tree root first
def preorder(root):
    if root == None:
        return None
    print root.val
    preorder(root.left)
    preorder(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    # preorder(root)
    print lca(root, 4, 2).val
