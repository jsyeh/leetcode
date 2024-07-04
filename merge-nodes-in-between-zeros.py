# LeetCode 2181. Merge Nodes in Between Zeros
# 在 LinkedList 的「資料結構」裡，要把「兩相鄰的0」之間的數，都加起來
# 最後，又再變回 LinkedList 來回傳（開始、結束，都是0）
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans, dst, src = head.next, head, head.next  # ans, dst共用原本linked list
        total = 0  # 用來放加總的結果
        while src != None:  # src 持續往右走，直到撞牆
            if src.val==0: # 要將加總結果，合併到dst
                dst = dst.next  # dst是用原來的linked list
                dst.val = total  # 把答案塞入
                total = 0  # 新的開始
            else: # 還沒遇到終止的0，繼續加
                total += src.val
            src = src.next  # 又用到1格src，再往右移
        dst.next = None  # 最後終止
        return ans
