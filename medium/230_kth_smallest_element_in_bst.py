from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """
    Builds a binary tree from LeetCode-style level-order input.
    Example: [3, 1, 4, None, 2]
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []

        def dfs(root):
            if root is None:
                return None
            
            if len(inorder) == k:
                return
            
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
        
        dfs(root)
        
        return inorder[k - 1]


tests = [
    # 1. Example 1
    ([3, 1, 4, None, 2], 1, 1),

    # 2. Example 2
    ([5, 3, 6, 2, 4, None, None, 1], 3, 3),

    # 3. Single node
    ([1], 1, 1),

    # 4. k is the smallest value
    ([8, 4, 12, 2, 6, 10, 14], 1, 2),

    # 5. k is the largest value
    ([8, 4, 12, 2, 6, 10, 14], 7, 14),

    # 6. Middle value in balanced BST
    ([8, 4, 12, 2, 6, 10, 14], 4, 8),

    # 7. Left-skewed BST
    ([5, 4, None, 3, None, 2, None, 1], 2, 2),

    # 8. Right-skewed BST
    ([1, None, 2, None, 3, None, 4, None, 5], 4, 4),

    # 9. Larger uneven BST
    ([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8], 6, 8),
]


solution = Solution()

for i, (tree_list, k, expected) in enumerate(tests, 1):
    root = build_tree(tree_list)
    output = solution.kthSmallest(root, k)

    print(f"Test {i}")
    print(f"Input tree: {tree_list}")
    print(f"k:          {k}")
    print(f"Output:     {output}")
    print(f"Expected:   {expected}")
    print(f"Pass:       {output == expected}")
    print("-" * 40)