# 把倒數第n個node，從 head 的 list 裡移除
# 所以需要先數一下 head 這個 list 的長度N有多長，再數到 (N-n) 的位置，以便移除
# 移除時，要有prev以便接到next
# 小心邊界條件
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head2 = head # 備份，以免操作時，影響到原本的 head
        N = 0 # head list 的長度
        while head2 != None:
            head2 = head2.next
            N += 1
        
        if n==N: #剛好要移除「倒數的倒數」也就是第一個 node
            return head.next # 就直接避開最前面那個

        head2 = head # 再備份一次
        for i in range(N-n): # 現在再好好數
            prev = head2 # 前一項
            head2 = head2.next # 要消除的項
        prev.next = head2.next # 將 head2 移除，也就是「前一項」避開head2「直接接後面」
        return head
