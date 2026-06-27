
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        nodes = []

        def dfs(root):
            if root is None:
                return None
            nodes.append(root)
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)

        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]

        if nodes:
            nodes[-1].left = None
            nodes[-1].right = None

    



# Helpers
def T(val, left=None, right=None):
    return TreeNode(val, left, right)


def flattened_values(root):
    vals = []
    cur = root

    while cur:
        if cur.left is not None:
            return f"ERROR: node {cur.val} still has left child {cur.left.val}"

        vals.append(cur.val)
        cur = cur.right

    return vals


sol = Solution()


# Test 1 — LeetCode example
root = T(
    1,
    T(2, T(3), T(4)),
    T(5, None, T(6))
)
sol.flatten(root)
print(flattened_values(root))  # [1, 2, 3, 4, 5, 6]


# Test 2 — empty tree
root = None
sol.flatten(root)
print(flattened_values(root))  # []


# Test 3 — single node
root = T(0)
sol.flatten(root)
print(flattened_values(root))  # [0]


# Test 4 — left-heavy tree
root = T(1, T(2, T(3, T(4))))
sol.flatten(root)
print(flattened_values(root))  # [1, 2, 3, 4]


# Test 5 — right-heavy tree
root = T(1, None, T(2, None, T(3, None, T(4))))
sol.flatten(root)
print(flattened_values(root))  # [1, 2, 3, 4]


# Test 6 — mixed uneven tree
root = T(
    1,
    T(2, None, T(3)),
    T(4, T(5), T(6))
)
sol.flatten(root)
print(flattened_values(root))  # [1, 2, 3, 4, 5, 6]