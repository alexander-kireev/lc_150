# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from math import inf

class BSTIterator:
    def __init__(self, root):
        self.head = TreeNode(-inf)
        self.stack = []
        smallest = self.find_smallest(root)
        self.head.right = smallest

    def find_smallest(self, root):
        if root.left is None:
            return root

        self.stack.append(root)
        return self.find_smallest(root.left)


    def next(self):
        if self.head.right is not None:
            self.head = self.find_smallest(self.head.right)
            return self.head.val

        else:
            self.head = self.stack.pop()
            return self.head.val

    def hasNext(self):
        if self.head.right is not None or self.stack:
            return True
        return False


# Build BST:
#
#           7
#         /   \
#        3     15
#             /  \
#            9    20
#
n7 = TreeNode(7)
n3 = TreeNode(3)
n15 = TreeNode(15)
n9 = TreeNode(9)
n20 = TreeNode(20)

n7.left = n3
n7.right = n15
n15.left = n9
n15.right = n20


iterator = BSTIterator(n7)

print(iterator.hasNext())   # Expected: True
print(iterator.next())      # Expected: 3
print(iterator.next())      # Expected: 7
print(iterator.hasNext())   # Expected: True
print(iterator.next())      # Expected: 9
print(iterator.hasNext())   # Expected: True
print(iterator.next())      # Expected: 15
print(iterator.next())      # Expected: 20
print(iterator.hasNext())   # Expected: False


print("\n--- single node ---")

single = TreeNode(1)
iterator = BSTIterator(single)

print(iterator.hasNext())   # Expected: True
print(iterator.next())      # Expected: 1
print(iterator.hasNext())   # Expected: False


print("\n--- left-heavy BST ---")

#       5
#      /
#     4
#    /
#   3
#  /
# 2
#
n5 = TreeNode(5)
n4 = TreeNode(4)
n3b = TreeNode(3)
n2 = TreeNode(2)

n5.left = n4
n4.left = n3b
n3b.left = n2

iterator = BSTIterator(n5)

while iterator.hasNext():
    print(iterator.next(), end=" ")

# Expected: 2 3 4 5
print()


print("\n--- right-heavy BST ---")

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#
r1 = TreeNode(1)
r2 = TreeNode(2)
r3 = TreeNode(3)
r4 = TreeNode(4)

r1.right = r2
r2.right = r3
r3.right = r4

iterator = BSTIterator(r1)

while iterator.hasNext():
    print(iterator.next(), end=" ")

# Expected: 1 2 3 4
print()