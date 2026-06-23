class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_group_k(head, k):

    dummy = Node(None)
    dummy.next = head
    prev = dummy
    cur = head

    while cur is not None:

        # pointer to check if chunk >= k
        temp = cur

        # try to get last node of chunk
        for _ in range(k):
            
            if temp is not None:
                temp = temp.next
            # if available chunk < k
            else:
                # attach prev to start of this chunk
                prev.next = cur
                return dummy.next
        

        # REVERSE NODES OF CHUNK

        # make local dummy
        local_prev = Node(None)

        # this node is the cur first node, so after reverse, will be tail of chunk
        tail = cur

        for _ in range(k):
            next_node = cur.next
            cur.next = local_prev
            local_prev = cur
            cur = next_node
        
        # attach GLOBAL prev to new head of chunk
        prev.next = local_prev

        # attach tail of new chunk to next start
        tail.next = cur

        # update GLOBAL prev for next chunk
        prev = tail
        
    return dummy.next



def build_list(values):
    dummy = Node(0)
    cur = dummy

    for v in values:
        cur.next = Node(v)
        cur = cur.next

    return dummy.next


def list_to_array(head):
    output = []

    while head:
        output.append(head.val)
        head = head.next

    return output


head = build_list([1, 2, 3, 4, 5])
new_head = reverse_group_k(head, 2)
print(list_to_array(new_head))  # [2, 1, 4, 3, 5]

head = build_list([1, 2, 3, 4, 5])
new_head = reverse_group_k(head, 3)
print(list_to_array(new_head))  # [3, 2, 1, 4, 5]

head = build_list([1, 2, 3, 4, 5])
new_head = reverse_group_k(head, 1)
print(list_to_array(new_head))  # [1, 2, 3, 4, 5]

head = build_list([1, 2])
new_head = reverse_group_k(head, 2)
print(list_to_array(new_head))  # [2, 1]

head = build_list([1, 2, 3])
new_head = reverse_group_k(head, 2)
print(list_to_array(new_head))  # [2, 1, 3]

head = build_list([1, 2, 3, 4, 5, 6])
new_head = reverse_group_k(head, 3)
print(list_to_array(new_head))  # [3, 2, 1, 6, 5, 4]