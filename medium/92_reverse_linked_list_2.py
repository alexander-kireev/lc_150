class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def rev(head, left, right):

    dummy = Node(None)
    dummy.next = head
    before_left = dummy

    cur = head
    count = 1

    while count < left:
        before_left = cur
        cur = cur.next
        count += 1

    tail_of_reversed = cur
    prev = None

    while count < right + 1:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
        count += 1

    before_left.next = prev
    tail_of_reversed.next = cur

    return dummy.next








n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

left = 2
right = 4

new_head = rev(n1, left, right)

cur = new_head

while cur is not None:
    print(cur.val)
    cur = cur.next