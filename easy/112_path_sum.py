# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def followPath(root, sum):
            if root is None:
                return False
            
            sum += root.val

            if root.left is None and root.right is None:
                return sum == targetSum
            
            return followPath(root.left, sum) or followPath(root.right, sum)


        

        return followPath(root, 0)