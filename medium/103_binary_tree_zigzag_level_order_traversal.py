# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        level = []

        if root is not None:
            level.append(root)

        left = True

        while level:
            
            values = []
            next_level = []

            for node in level:
                values.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            
            if left:
                output.append(values)
                left = False
            else:
                output.append(values[::-1])
                left = True
            
            level = next_level
            
        return output