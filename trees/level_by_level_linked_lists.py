from queue import *
from tree import *
import sys

def level_by_level_linked_lists(root):
    queue = Queue()
    queue.enqueue(root)
    queue.enqueue(None)
    output_list = []
    # Till the queue has something, dequeue
    while not queue.isEmpty():
        # print "Queue ", queue.display()
        current = queue.dequeue()
        # print "Current: ", current
        if current is None:
            if queue.isEmpty():
                break
            # Do something
            queue.enqueue(None)
            sys.stdout.write("\n")
        else:
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
            sys.stdout.write(str(current.val) + " ")





if __name__ == "__main__":
    bt = TreeNode(1)
    bt.left = TreeNode(2)
    bt.right = TreeNode(3)
    bt.left.left = TreeNode(4)
    bt.left.right = TreeNode(5)
    bt.right.left = TreeNode(6)
    bt.right.right = TreeNode(7)
    level_by_level_linked_lists(bt)
