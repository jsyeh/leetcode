# 這題我寫了很多次。這次想用 Python 來解, 配合 fast, slow 的技巧:
# fast 走2倍, slow 走1倍。如果 fast 遇到 None, 那 slow 剛好是一半。
# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head # 一開始 fast slow 都在頭的位置,準備出發

        while fast != None and fast.next != None: # 還沒有走到盡頭
            fast = fast.next.next # 兩倍速跑
            slow = slow.next      # 一倍速跑
        # 離開迴圈時, fast走到終點, 那 slow 剛好在一半的位置
        return slow

