
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def p(head, x): 
    less_dummy = Node(0)
    greater_dummy = Node(0)
    less_tail = less_dummy
    greater_tail = greater_dummy

    cur = head

    while cur is not None:

        next_node = cur.next
        
        if cur.val < x:
            less_tail.next = cur
            less_tail = cur
        else:
            greater_tail.next = cur
            greater_tail = cur

        cur = next_node

    less_tail.next = greater_dummy.next
    greater_tail.next = None
    return less_dummy.next




n1 = Node(4)
n2 = Node(2)
n3 = Node(1)
n4 = Node(3)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


new_head = p(n1, 3)


cur = new_head

while cur is not None:
    print(cur.val)
    cur = cur.next