# 先數 M 個 node 後，再將 N 個 node 刪掉。一直重覆。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        head2 = head
        while head2 != None: # 持續一直重覆
            for i in range(m-1): # 先數 m 個點，保留
                # 為何m-1，是輸出後，發現有多留1個node，所以修正
                if head2 == None: break # 遇到結束時，就不再處理
                head2 = head2.next # 簡單右移
            if head2 == None: break # 再測一次，遇到結束，就不再處理

            prev = head2 # 還使用的前一項，等一下要用來接到後面
            for i in range(n+1): # 要逐項跳過哦
                # 為何 n+1，是輸出後，發現少刪1個node，所以修正
                if head2 == None: break #  遇到結束時，就不再處理
                head2 = head2.next # 簡單右移
            # 不break跳掉，才能將 None 接上
            prev.next = head2
            
        return head # 處理過的 lined list 回傳
