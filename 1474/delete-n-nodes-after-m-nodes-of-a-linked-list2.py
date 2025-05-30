# LeetCode 1474. Delete N Nodes After M Nodes of a Linked List
# 在 Linked List 裡，依照「留 M 個、刪 N 個」的規則重建
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        ans = head  # 最後會回傳的答案
        while head != None:  # head 開始往右走
            for i in range(m-1):  # 留 M 個
                # 為何 m-1？是輸出後，發現有多留1個node，所以修正
                if head == None: break  # 沒辦法走，就跳掉
                head = head.next  # 往右走 M 個
            if head == None: break  # 沒辦法走，就跳掉
            keep = head  # 記下現在這個位置

            for i in range(n+1):  # 刪 N 個
                # 為何 n-1？是輸出後，發現有少刪1個node，所以修正
                if head == None: break  # 沒辦法走，就跳掉
                head = head.next  # 往右走 N 個
            keep.next = head
        return ans
