# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        carry = 0
        dummy = curr = ListNode(0)

        while ptr1 or ptr2:
            ptr1_val = ptr1.val if ptr1 else 0
            ptr2_val = ptr2.val if ptr2 else 0
            result = ptr1_val + ptr2_val + carry
            if result >= 10:
                result %= 10
                carry = 1
            else:
                carry = 0
            
            newNode = ListNode(result)
            curr.next = newNode
            curr = curr.next
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
        
        if carry == 1:
            curr.next = ListNode(1)
            
        return dummy.next
        
            