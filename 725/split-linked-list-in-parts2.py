# LeetCode 725. Split Linked List in Parts
# 將 Linked List 切割為k組，不夠k組要補[]，儘量均分，有多的話，逐一放左邊
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        now, N = head, 0  # 從頭開始處理，已經過 N 個 node
        while now!=None: # 要先知道 Linked List 裡有幾個node，才好斷開
            now, N = now.next, N + 1
        avg, m = N//k, N%k  # 分成 k 組，平均每組 avg 個, 剩下 m 個

        ans = []  # 用來裝 k 個答案
        
        for g in range(m):  # 剩下的 m 個，放在前面 m 組（每組 avg+1 個）
            part = prev = ListNode(0)  # 前一項
            prev.next = head
            for i in range(avg+1):  # 裡面放 avg+1個 node
                prev, head = prev.next, head.next  # 指到下一筆
            prev.next = None  # 此段結束時，斷開
            ans.append(part.next)

        for g in range(m,k):  # 後面的組，每組 avg 個
            part = prev = ListNode(0)  # 前一項
            prev.next = head
            for i2 in range(avg):  # 裡面放 avg 個 node
                prev, head = prev.next, head.next  # 指到下一筆
            prev.next = None  # 此段結束時，斷開
            ans.append(part.next)
        return ans
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

