class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = []

        while root is not None or stack:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                output.append(root.val)
                root = root.right

        
        
        return output