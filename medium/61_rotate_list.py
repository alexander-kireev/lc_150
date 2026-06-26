class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate_list(head, k):
    if head is None:
        return head
    
    length = 1

    old_tail = head

    while old_tail.next is not None:
        old_tail = old_tail.next
        length += 1

    k = k % length

    if k == 0:
        return head
    
    before = head

    steps = length - k - 1
    while steps > 0:
        before = before.next
        steps -= 1

    new_head = before.next
    before.next = None
    old_tail.next = head
    head = new_head

    return head








def build_list(values):
    dummy = ListNode()
    cur = dummy

    for v in values:
        cur.next = ListNode(v)
        cur = cur.next

    return dummy.next


def list_to_array(head):
    output = []

    while head:
        output.append(head.val)
        head = head.next

    return output



head = build_list([1, 2, 3, 4, 5])
new_head = rotate_list(head, 2)
print(list_to_array(new_head))  # [4, 5, 1, 2, 3]

head = build_list([0, 1, 2])
new_head = rotate_list(head, 4)
print(list_to_array(new_head))  # [2, 0, 1]

head = build_list([1])
new_head = rotate_list(head, 0)
print(list_to_array(new_head))  # [1]

head = build_list([1])
new_head = rotate_list(head, 99)
print(list_to_array(new_head))  # [1]

head = build_list([])
new_head = rotate_list(head, 3)
print(list_to_array(new_head))  # []

head = build_list([1, 2])
new_head = rotate_list(head, 1)
print(list_to_array(new_head))  # [2, 1]

head = build_list([1, 2])
new_head = rotate_list(head, 2)
print(list_to_array(new_head))  # [1, 2]

head = build_list([1, 2, 3, 4, 5])
new_head = rotate_list(head, 5)
print(list_to_array(new_head))  # [1, 2, 3, 4, 5]

head = build_list([1, 2, 3, 4, 5])
new_head = rotate_list(head, 7)
print(list_to_array(new_head))  # [4, 5, 1, 2, 3]