from tree import *

def check_bst_inorder(root):
    if not root:
        return True
    global previous
    if not check_bst_inorder(root.left): return False
    if root.val < previous: return False
    previous = root.val
    if not check_bst_inorder(root.right): return False
    return True


if __name__ == "__main__":
    previous = float('-inf')
    bt = generate_bst()
    print check_bst_inorder(bt)


    # bt
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
