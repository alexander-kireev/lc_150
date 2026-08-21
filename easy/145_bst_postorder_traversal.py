def postorder_traversal(root):
    output = []

    def dfs(root):
        if root is None:
            return
        
        dfs(root.left)
        dfs(root.right)
        output.append(root.val)
    
    dfs(root)
    return output