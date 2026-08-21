def inorder_traversal(root):
    output = []

    def dfs(root):
        if root is None:
            return

        dfs(root.left)
        output.append(root.val)
        dfs(root.right)
    
    dfs(root)
    return output