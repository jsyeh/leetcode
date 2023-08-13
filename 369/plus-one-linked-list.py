# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 要將「很長的數字」加1時，可先檢查「是否全是9」
# 如果全是9，就再加1位。不然只要把不是9的那一位準備+1即可
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        next = head
        N, nine = 0, 0
        while next!=None:
            if next.val == 9:
                nine += 1
            next = next.next
            N += 1
        # 離開迴圈後，便能知：有幾位數、有幾個9
        if N == nine: # 全部都是9的話
            ans = ListNode(1,head) # 只有第1位留1
            next = head
            while next != None:
                next.val = 0 # 後面每1位都是0
                next = next.next
            return ans
        else: # 裡面有摻不是 9 的數，最後1個非9的數，要加1
            nonNine = N - nine
            next = head
            while nonNine>0: # 剩下「非9的數」有幾個
                if next.val!=9: # 非9的數
                    nonNine -= 1
                    prev = next
                    next = next.next
                else: next = next.next
            # 離開迴圈，表示現在這位要變1，後面變0
            print(prev.val)
            prev.val = prev.val + 1
            next = prev.next
            while next!=None:
                next.val = 0
                next = next.next
            return head

