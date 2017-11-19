# LinkedIn Phone Interview
# Given a binary search tree and a target value, find k values in the binary search tree (BST) that are closest to the target.
#
# Given the following Binary Search Tree:
#                 10
#                /  \
#               5    20
#              /\    /\
#             1  6  15 30
#                 \
#                  7
# Given target=8, and k=3, it should return 6,7,10
#

def closest(root,target, k):
  val = all_values(root, [])
  # create a queue
  # insert the first 3 in the queue
  que = [0, 1, 2]
  for 3 in range(len(val)):
    if abs(get(que) - target) > abs(val[i] - target):
      dequeue()
      enqueue(val[i])
  return que



def all_values(root, val):
  # Base case:
  if root == None:
    return
  all_values(root.left, val)
  val.append(root.data)
  all_values(root.right, val)
  return val
