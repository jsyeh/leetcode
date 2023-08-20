# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: # 特殊狀況：只有1個的話
            return None # 那就要殺掉它，剩下 None

        # 正常情況會比較長，所以要先數一下長度哦
        N = 0 # 一開始是 0 
        anya = head # 安妮亞的手，指向第1個node
        while anya!=None: # 只要安妮亞還沒變成空的，就是還能繼續比
            anya = anya.next # 安妮亞 變成 下一個安妮亞
            N += 1 # 數數，多一個
        # 離開迴圈時，就能知道現在到底有幾個安妮亞

        anya = head # 重新來過，安妮亞的手，指向第1個node
        old = anya # 這個「舊的」安妮亞，會尾隨在後面。
        # 因為在刪除某個安妮亞時，需要由尾隨的「舊的」安妮亞來發動
        for i in range(N//2):
            old = anya # 「舊的」安妮亞
            anya = anya.next # 現在安妮亞指到新的安妮亞的位置了
        # 離開迴圈時，安妮亞是正中間、等待刪除的那一個
        
        # 因為在刪除某個安妮亞時，需要由尾隨的「舊的」安妮亞來發動、「執行」
        old.next = anya.next # 要被殺死的那個安妮亞，她的下一代，交給舊的安妮亞來撫養
        return head
