# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = ListNode(0, head) # ans.next 是最後要resturn的答案
        old = ans # 安妮亞 Anya 的前一個、舊的安妮亞，用來監督安妮亞
        anya = head # 安妮亞 Anya，從 head 開始走
        while anya != None: # 安妮亞 Anya 還不是空的話，便能逐一比較
            if anya.val == val: # 遇到要刪除的點
                old.next = anya.next # 跳過這筆，接手安妮亞 Anya 的下一代
                anya = anya.next # 安妮亞 Anya 的下一代
            else: # 正常、要保留的點
                old = anya # 往下滑
                anya = anya.next # 往下滑
        return ans.next
