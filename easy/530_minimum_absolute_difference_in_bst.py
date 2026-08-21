def kthSmallest(root, k):
    ans = None

    def dfs(root):
        nonlocal ans, k

        if ans is not None:
            return

        if root is None:
            return
        
        dfs(root.left)

        k -= 1

        if k == 0:
            ans = root.val

        dfs(root.right)
    
    dfs(root)
    return ans