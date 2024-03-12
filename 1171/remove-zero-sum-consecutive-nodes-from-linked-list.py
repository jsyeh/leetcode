# 把 linked list 裡面，某段「連續加總是0」的部分刪掉
# 我看了 Description 裡的 Hint 1,2,3 覺得沒什麼用
# lee215的解法，我覺得有點難理解。
# 意外發現 zzhuaixin 的解法還不錯，把解題概念講的很清楚
# 就照著這個思緒來解題
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0, head) # 做 head 的前一個Node，便不用擔心移除的問題
        prefix = 0 # prefix sum
        pos = defaultdict(ListNode) # pos[prefix]記錄對應位置
        pos[0] = ans # 最頭頭的位置
        now = head
        while now != None:
            prefix += now.val # prefix sum
            pos[prefix] = now # 對應的位置
            now = now.next # 繼續往下走
        # 迴圈走完後，prevPos[加總值] 更新成「最後面」出現位置
        now = ans # 從頭再做一次，但需要更前面的ans node
        prefix = 0
        while now != None:
            prefix += now.val
            now.next = pos[prefix].next # 避開 前一次出現的位置
            # 所以中間很大一段，都被剪掉了
            now = now.next
        return ans.next
