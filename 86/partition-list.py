# 題目給個值，要讓「比它小的」保持原有順序，在左邊
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head==None: return head

        smaller, bigger = ListNode(), ListNode() # 會依序裝2群（小、大）
        nextS, nextB = smaller, bigger # 兩個指標，指到下個要裝的東西
        while head != None:
            if head.val < x:
                nextS.next = head
                head = head.next
                nextS = nextS.next
            else:
                nextB.next = head
                head = head.next
                nextB = nextB.next
        # 離開迴圈後，把 smaller 和 bigger接起來
        nextS.next = bigger.next # 接起來
        nextB.next = None # 最後接地、收尾
        return smaller.next
