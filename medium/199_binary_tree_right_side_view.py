from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """
    Builds a binary tree from LeetCode-style level-order list.
    Example: [1, 2, 3, None, 5, None, 4]
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        level = []
        
        if root is not None:
            level.append(root)

        while level:
            new_level = []
            output.append(level[-1].val)

            for node in level:
                if node.left is not None:
                    new_level.append(node.left)
                if node.right is not None:
                    new_level.append(node.right)

            level = new_level

        return output



tests = [
    ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
    ([], []),
    ([1], [1]),
    ([1, None, 2, None, 3], [1, 2, 3]),
    ([1, 2, None, 3, None, 4], [1, 2, 3, 4]),
    ([1, 2, 3, 4], [1, 3, 4]),
    ([1, 2, 3, 4, 5], [1, 3, 5]),
    ([1, 2, 3, None, 5, 6, None, None, 7], [1, 3, 6, 7]),
]


solution = Solution()

for i, (tree_list, expected) in enumerate(tests, 1):
    root = build_tree(tree_list)
    output = solution.rightSideView(root)

    print(f"Test {i}")
    print(f"Input:    {tree_list}")
    print(f"Output:   {output}")
    print(f"Expected: {expected}")
    print(f"Pass:     {output == expected}")
    print("-" * 40)