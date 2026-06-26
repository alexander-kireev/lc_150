
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):

        if p is None or q is None:
            return p == q
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
    



def T(val, left=None, right=None):
    return TreeNode(val, left, right)


sol = Solution()

# Same simple tree: [1,2,3] vs [1,2,3]
p = T(1, T(2), T(3))
q = T(1, T(2), T(3))
print(sol.isSameTree(p, q))  # True


# Different structure: [1,2] vs [1,null,2]
p = T(1, T(2), None)
q = T(1, None, T(2))
print(sol.isSameTree(p, q))  # False


# Same structure, different values: [1,2,1] vs [1,1,2]
p = T(1, T(2), T(1))
q = T(1, T(1), T(2))
print(sol.isSameTree(p, q))  # False


# Both empty
p = None
q = None
print(sol.isSameTree(p, q))  # True


# One empty, one not
p = T(1)
q = None
print(sol.isSameTree(p, q))  # False


# Larger same tree
p = T(5, T(3, T(2), T(4)), T(8, T(7), T(9)))
q = T(5, T(3, T(2), T(4)), T(8, T(7), T(9)))
print(sol.isSameTree(p, q))  # True


# Larger tree with one deep structural difference
p = T(5, T(3, T(2), T(4)), T(8, T(7), T(9)))
q = T(5, T(3, T(2), T(4)), T(8, None, T(9)))
print(sol.isSameTree(p, q))  # False