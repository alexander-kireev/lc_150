
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        val = preorder[0]
        root = TreeNode(val)
        mid = inorder.index(val)
        root.left = self.buildTree(preorder[1:], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
    



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



preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = Solution().buildTree(preorder, inorder)
print(level_order(root))  # [3, 9, 20, None, None, 15, 7]