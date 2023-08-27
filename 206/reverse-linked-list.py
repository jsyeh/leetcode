# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None: return None # 完全都沒有
        if head.next==None: return head # 只有1個

        ans = self.reverseList(head.next)
        # 因為做完 reverseList後，head.next就會是最後1個
        head.next.next = head # 所以最後1個的下一筆，指到head
        head.next = None # head再接地結束
        return ans
