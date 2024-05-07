# 這題用 Linked List 表示 10000 位大數，要模擬進位。
# 原本我用「大數加法」先「反過來」變成「個位數」到「高位數」以便兩數對齊
# 但這題更簡單：變成兩倍，自己加自己，本來就對齊。可省下反過來、反過去的步驟。
# 比較特別的地方，是「多1位」最高位。像 500+500=1000 要多1位
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val >= 5:  # 「四捨五入」概念： 500+500 會進位，499+499不會進位
            head = ListNode(0, head)  # 因有進位，需要多1位
        now = head
        while now is not None:  # 還沒走到最後
            now.val = (now.val + now.val) % 10  # 看這個位數，在加法後，會變多少
            if now.next is not None and now.next.val >= 5:  # 下一位，有進位時
                now.val += 1  # 答案就 +1
            now = now.next
        return head  # 直接使用 head 來放答案

