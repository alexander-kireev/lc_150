
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = []
        if root:
            queue.append(root)
        

        while queue:
            new_queue = []

            prev = None

            for node in queue:
                
                if prev:
                    prev.next = node

                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)

                prev = node

            queue = new_queue

        return root
    




class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def print_levels_with_next(root):
    level_start = root

    while level_start:
        cur = level_start
        vals = []

        next_level_start = None

        while cur:
            vals.append(cur.val)

            if next_level_start is None:
                if cur.left:
                    next_level_start = cur.left
                elif cur.right:
                    next_level_start = cur.right

            cur = cur.next

        vals.append("#")
        print(vals)

        level_start = next_level_start




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
root = Solution().connect(root)
print_levels_with_next(root)


print()


root = None
root = Solution().connect(root)
print(root)  # None


print()


root = Node(1)
root = Solution().connect(root)
print_levels_with_next(root)


print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root = Solution().connect(root)
print_levels_with_next(root)


print()


root = Node(1)
root.left = Node(2)
root.left.right = Node(4)
root.left.right.left = Node(8)
root.right = Node(3)
root.right.right = Node(7)
root = Solution().connect(root)
print_levels_with_next(root)