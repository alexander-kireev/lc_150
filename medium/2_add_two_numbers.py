# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        carry_over = 0
        
        output_head = ListNode(0)
        prev = output_head
 
        while cur1 is not None and cur2 is not None:
            cur_sum = cur1.val + cur2.val + carry_over

            if carry_over == 1:
                carry_over = 0

            if cur_sum >= 10:
                carry_over = 1
                cur_sum -= 10
            
            new_node = ListNode(cur_sum)
            prev.next = new_node
            prev = prev.next

            cur1 = cur1.next
            cur2 = cur2.next
        
        cur = None

        if cur1 is not None:
            cur = cur1
        elif cur2 is not None:
            cur = cur2

        while cur is not None:
            cur_sum = cur.val + carry_over

            if carry_over == 1:
                carry_over = 0
            if cur_sum >= 10:
                carry_over = 1
                cur_sum -= 10

            cur = cur.next
            new_node = ListNode(cur_sum)
            prev.next = new_node
            prev = prev.next

        if carry_over == 1:
            new_node = ListNode(1)
            prev.next = new_node

        return output_head.next