class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_node(head, n):
    dummy = ListNode()
    dummy.next = head
    before = dummy
    cur = head

    for _ in range(n):
        cur = cur.next

    while cur is not None:
        cur = cur.next
        before = before.next

    before.next = before.next.next

    return dummy.next






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
new_head = remove_node(head, 2)
print(list_to_array(new_head))  # [1, 2, 3, 5]

head = build_list([1])
new_head = remove_node(head, 1)
print(list_to_array(new_head))  # []

head = build_list([1, 2])
new_head = remove_node(head, 1)
print(list_to_array(new_head))  # [1]

head = build_list([1, 2])
new_head = remove_node(head, 2)
print(list_to_array(new_head))  # [2]

head = build_list([1, 2, 3])
new_head = remove_node(head, 3)
print(list_to_array(new_head))  # [2, 3]

head = build_list([1, 2, 3])
new_head = remove_node(head, 1)
print(list_to_array(new_head))  # [1, 2]

head = build_list([1, 2, 3, 4, 5])
new_head = remove_node(head, 5)
print(list_to_array(new_head))  # [2, 3, 4, 5]