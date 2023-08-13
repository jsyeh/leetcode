# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # 建個 HashTable 便可知道有重覆的了
        # 先全部巡過一次，找出任何有重覆的
        hashset = set() # 全部的
        dup = set() # 重覆的
        next = head
        while next != None:
            if next.val in hashset:
                dup.add(next.val) # 只有重覆的才加
            hashset.add(next.val) # 全部都加
            next = next.next # 繼續下一筆
        # 現在知道誰是 dup 了
        print(dup)
        ans = ListNode(0, head)
        prev, next = ans, head
        while next != None:
            if next.val in dup:
                next = next.next # 跳過這一筆，直接下一筆
            else: # 不是重覆的項
                prev.next = next # 裝上不重覆的node
                prev = prev.next # 順順的移動
                next = next.next # 繼續下一筆
        prev.next = None
        return ans.next


