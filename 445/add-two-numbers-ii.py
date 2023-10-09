# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(listA: Optional[ListNode]) -> Optional[ListNode]:
            if listA==None or listA.next==None: return listA
            end = listA.next # 要整個反轉，所以 第2個的下一個，要返回去 A
            ans = reverse(listA.next)
            end.next = listA # 要整個反轉，所以 第2個的下一個，要返回去 A
            listA.next = None # 新的結尾
            return ans 

        l1, l2 = reverse(l1), reverse(l2) # 兩個 list 都反過來
        ans = ListNode()
        next = ans
        carry = 0
        while l1!=None or l2!=None:
            next.next = ListNode()
            next = next.next
            if l1!=None:
                carry += l1.val
                l1 = l1.next
            if l2!=None:
                carry += l2.val
                l2 = l2.next
            next.val = carry % 10
            carry //= 10
        if carry>0:
            next.next = ListNode(carry)

        return reverse(ans.next) # 最後答案再反過來
# case 1113/1563: [5] [5] 要得到 [1, 0]
