# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):

    if root is None:
        return None

    if root == p or root == q:
        return root

    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root


    


# Build BST:
#
#           6
#         /   \
#        2     8
#       / \   / \
#      0   4 7   9
#         / \
#        3   5
#
n6 = TreeNode(6)
n2 = TreeNode(2)
n8 = TreeNode(8)
n0 = TreeNode(0)
n4 = TreeNode(4)
n7 = TreeNode(7)
n9 = TreeNode(9)
n3 = TreeNode(3)
n5 = TreeNode(5)

n6.left = n2
n6.right = n8

n2.left = n0
n2.right = n4

n8.left = n7
n8.right = n9

n4.left = n3
n4.right = n5


tests = [
    (n6, n2, n8, 6),   # split at root
    (n6, n2, n4, 2),   # p is ancestor of q
    (n6, n3, n5, 4),   # split deeper in left subtree
    (n6, n0, n5, 2),   # both in left subtree
    (n6, n7, n9, 8),   # split in right subtree
    (n6, n3, n9, 6),   # opposite sides of root
    (n6, n4, n5, 4),   # p is ancestor of q
    (n6, n6, n3, 6),   # root itself is one target
]

for root, p, q, expected in tests:
    result = lowestCommonAncestor(root, p, q)

    print(
        f"p={p.val}, q={q.val} -> "
        f"{result.val if result else None} "
        f"(expected {expected})"
    )


    