# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        next = ans
        carry = 0
        while l1!=None or l2!=None:
            next.next = ListNode()
            next = next.next
            if l1!=None: 
                carry += l1.val
                l1 = l1.next
            if l2!=None: 
                carry += l2.val
                l2 = l2.next
            next.val = carry % 10
            carry //= 10  # 若超過10會進位
        if carry>0:
            next.next = ListNode(carry)
        return ans.next

