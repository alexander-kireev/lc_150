class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []

        def dfs(root):
            if root is None:
                return None
            
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)

        dfs(root)

        for i in range(len(inorder) - 1):
            if inorder[i] >= inorder[i + 1]:
                return False
                
        return True