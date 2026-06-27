from collections import deque

def level_order(root):
    if root is None:
        return []

    out = []
    q = deque([root])

    while q:
        node = q.popleft()

        if node is None:
            out.append(None)
            continue

        out.append(node.val)
        q.append(node.left)
        q.append(node.right)

    while out and out[-1] is None:
        out.pop()

    return out



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        val = postorder.pop()
        root = TreeNode(val)
        mid = inorder.index(val)
        root.right = self.buildTree(inorder[mid + 1:], postorder)
        root.left = self.buildTree(inorder[:mid], postorder)
        return root



inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

root = Solution().buildTree(inorder, postorder.copy())
print(level_order(root))  # [3, 9, 20, None, None, 15, 7]