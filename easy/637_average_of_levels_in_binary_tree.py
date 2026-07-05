# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        # level averages
        averages = []

        # current level
        level = [root]

        # while a level exists
        while level:

            # for children of nodes of current level
            next_level = []

            # total level sum
            total = 0

            # iterate over nodes in level
            for i in range(len(level)):

                # get node
                node = level[i]

                # sum
                total += node.val

                # add children is they exist to the next level
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            
            # get average
            averages.append(total / len(level) * 1.0)

            level = next_level
        
        return averages