# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        last = [None]

        def dfs(root, found):
            if root is None:
                return False

            if root == p:
                found.add(p)
            
            if root == q:
                found.add(q)

            if p in found and q in found:
                return

            dfs(root.left, found)
            dfs(root.right, found)

            if p in found and q in found:
                last[0] = root

        dfs(root, set())
        return last[0]
        


from collections import deque

def build_tree(values):
    if not values:
        return None, {}

    root = TreeNode(values[0])
    nodes = {values[0]: root}
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            nodes[values[i]] = node.left
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            nodes[values[i]] = node.right
            queue.append(node.right)
        i += 1

    return root, nodes


tests = [
    (
        [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
        5,
        1,
        3,
    ),
    (
        [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
        5,
        4,
        5,
    ),
    (
        [1, 2],
        1,
        2,
        1,
    ),
    (
        [1, 2, 3],
        2,
        3,
        1,
    ),
    (
        [1, 2, 3, 4, 5],
        4,
        5,
        2,
    ),
    (
        [1, 2, 3, 4, 5],
        4,
        3,
        1,
    ),
    (
        [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8],
        6,
        8,
        7,
    ),
    (
        [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8],
        1,
        8,
        5,
    ),
    (
        [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8],
        1,
        18,
        10,
    ),
]

sol = Solution()

for values, p_val, q_val, expected_val in tests:
    root, nodes = build_tree(values)

    p = nodes[p_val]
    q = nodes[q_val]

    result = sol.lowestCommonAncestor(root, p, q)

    print(f"Tree:      {values}")
    print(f"p:         {p_val}")
    print(f"q:         {q_val}")
    print(f"Expected:  {expected_val}")
    print(f"Got:       {result.val if result else None}")
    print("PASS" if result and result.val == expected_val else "FAIL")
    print("-" * 40)