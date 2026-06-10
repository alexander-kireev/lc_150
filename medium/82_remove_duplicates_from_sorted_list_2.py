class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def p(head):
    dummy = Node(None)
    dummy.next = head
    prev = dummy

    cur = head

    while cur is not None:
        
        if cur.next is not None and cur.val == cur.next.val:
            duplicate_val = cur.val

            while cur is not None and cur.val == duplicate_val:
                cur = cur.next
            
            prev.next = cur
        else:
            prev = cur
            cur = cur.next
    
    return dummy.next



#val = 1


# Sorted input:
# 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 5
# Expected output:
# 2 -> 4

n1 = Node(1)
n2 = Node(1)
n3 = Node(2)
n4 = Node(2)
n5 = Node(3)
n6 = Node(4)
n7 = Node(5)
n8 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

head = n1


# Input:
# 1 -> 1 -> 2 -> 2 -> 3
#
# Expected output:
# 3

n1 = Node(1)
n2 = Node(1)
n3 = Node(2)
n4 = Node(2)
n5 = Node(3)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = n1



new_head = p(n1)


cur = new_head

while cur is not None:
    print(cur.val)
    cur = cur.next