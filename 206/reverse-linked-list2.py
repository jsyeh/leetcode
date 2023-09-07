# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 想照 Editorial 的 iteration 的方法，重寫看看
        prev = None
        curr = head
        while curr != None:
            next = curr.next # 先備份 next
            curr.next = prev # 本來 curr.next「往後接」，現在改成「往回接」

            prev = curr # 往下移
            curr = next # 往下移（再把 next 塞回 curr）
        # 離開迴圈時，curr會是 None, 所以 prev 會是原本的最後node,也就是答案要的reversed的頭
        return prev # 將會是最後一筆
