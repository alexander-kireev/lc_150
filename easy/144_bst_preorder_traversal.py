def preorder_traversal(root):
    output = []

    def dfs(root):
        if root is None:
            return
        
        output.append(root.val)
        dfs(root.left)
        dfs(root.right)
    
    dfs(root)
    return output