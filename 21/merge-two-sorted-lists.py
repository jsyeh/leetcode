# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        next = ans
        while list1!=None and list2!=None:
            if list1.val < list2.val:
                next.next = list1
                list1 = list1.next
                next = next.next
            else:
                next.next = list2
                list2 = list2.next
                next = next.next
        if list1==None:
            next.next = list2
        else:
            next.next = list1
        return ans.next
