class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    inorder = []

    def dfs(root):
        if root is None:
            return

        dfs(root.left)
        inorder.append(root.val)
        dfs(root.right)

    dfs(root)

    for i in range(1, len(inorder)):
        if inorder[i - 1] >= inorder[i]:
            return False

    return True

def build_tree(values):
    if not values:
        return

    nodes = [
        None if value is None else TreeNode(value)
        for value in values
    ]

    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node is not None:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


tests = [
    ([2, 1, 3], True),

    ([5, 1, 4, None, None, 3, 6], False),

    ([1], True),

    ([2, 2, 3], False),

    ([2, 1, 2], False),

    ([5, 4, 6, None, None, 3, 7], False),

    ([10, 5, 15, None, None, 6, 20], False),

    ([10, 5, 15, 2, 7, 12, 20], True),

    ([3, 1, 5, 0, 2, 4, 6], True),

    ([3, 1, 5, 0, 4, 2, 6], False),

    ([0, -1, 1], True),

    ([2147483647], True),

    ([-2147483648, None, 2147483647], True),
]


for values, expected in tests:
    root = build_tree(values)
    result = isValidBST(root)

    print(f"root={values}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()