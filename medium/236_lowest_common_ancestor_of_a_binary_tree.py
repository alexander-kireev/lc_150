# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    if not root:
        return None

    if root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right

# Build tree:
#
#           3
#         /   \
#        5     1
#       / \   / \
#      6   2 0   8
#         / \
#        7   4
#
n3 = TreeNode(3)
n5 = TreeNode(5)
n1 = TreeNode(1)
n6 = TreeNode(6)
n2 = TreeNode(2)
n0 = TreeNode(0)
n8 = TreeNode(8)
n7 = TreeNode(7)
n4 = TreeNode(4)

n3.left = n5
n3.right = n1

n5.left = n6
n5.right = n2

n1.left = n0
n1.right = n8

n2.left = n7
n2.right = n4


tests = [
    (n3, n5, n1, 3),   # split across root
    (n3, n5, n4, 5),   # p is ancestor of q
    (n3, n6, n4, 5),   # both inside left subtree
    (n3, n7, n4, 2),   # siblings under same parent
    (n3, n0, n8, 1),   # siblings in right subtree
    (n3, n6, n8, 3),   # deep nodes on opposite sides
    (n3, n2, n7, 2),   # p is ancestor of q
    (n3, n3, n4, 3),   # root itself is one target
]

for root, p, q, expected in tests:
    result = lowestCommonAncestor(root, p, q)
    print(
        f"p={p.val}, q={q.val} -> "
        f"{result.val if result else None} "
        f"(expected {expected})"
    )




























def lowestCommonAncestor(root, p, q):
    p_path = []
    q_path = []

    def dfs(root, target):
        if root is None:
            return
        
        if target == p:
            path = p_path
            if path and path[-1] == p:
                return
        else:
            path = q_path
            if path and path[-1] == q:
                return

        path.append(root)

        dfs(root.left, target)
        dfs(root.right, target)

        if target == p:
            path = p_path
            if path and path[-1] == p:
                return
            path.pop()
        else:
            path = q_path
            if path and path[-1] == q:
                return
            path.pop()
    
    dfs(root, p)
    dfs(root, q)

    last_common = 0
    while last_common < len(p_path) and last_common < len(q_path) and p_path[last_common] == q_path[last_common]:
        last_common += 1
    
    return p_path[last_common - 1]