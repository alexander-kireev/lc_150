# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root, cur_sum):
            if root is None:
                return 0

            cur_sum = cur_sum * 10 + root.val

            if root.left is None and root.right is None:
                return cur_sum
            
            return dfs(root.left, cur_sum) + dfs(root.right, cur_sum)

        return dfs(root, 0)
    


def T(val, left=None, right=None):
    return TreeNode(val, left, right)

sol = Solution()

root = T(1, T(2), T(3))
print(sol.sumNumbers(root))  # 25

root = T(4, T(9, T(5), T(1)), T(0))
print(sol.sumNumbers(root))  # 1026

root = T(7)
print(sol.sumNumbers(root))  # 7

root = T(1, T(2, T(3, T(4))))
print(sol.sumNumbers(root))  # 1234

root = T(1, T(0, T(5), T(0)), T(2))
print(sol.sumNumbers(root))  # 217