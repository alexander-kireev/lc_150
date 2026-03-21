"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        cur = head
        nodes = {}
        nodes[None] = None

        while cur is not None:
            new_node = Node(cur.val)
            nodes[cur] = new_node
            cur = cur.next

        cur = head

        while cur is not None:
            cur_copy = nodes[cur]
            cur_copy.next = nodes[cur.next]
            cur_copy.random = nodes[cur.random]
            cur = cur.next

        return nodes[head]