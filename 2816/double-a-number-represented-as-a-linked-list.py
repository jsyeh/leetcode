# 這題用 Linked List 表示 10000 位大數，要模擬進位。
# 但進位要從右到左，有點麻煩。可先 reverse 算完再 reverse 回去。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):  # 利用「函式呼叫函式」來反轉
            if head is None or head.next is None:
                return head  # 簡單的終止條件

            second = head.next  # 第2個，在reverse()後，將變最後1個
            ans = reverse(head.next)  # 倒過來後
            second.next = head  # 最後1個的next指到原本第1個
            head.next = None  # 斷開最後的連結
            return ans  # 就全部翻轉了

        head = reverse(head)  # 先翻轉，個位數 就在最前面

        next, prev = head, head
        carry = 0  # 進位的那個變數
        while next is not None:
            next.val = next.val * 2 + carry  # 變兩倍
            carry = next.val // 10  # 新的進位的值
            next.val %= 10  # 保留的個位數
            prev = next  # 保留前一項
            next = next.next  # 下一個
        if carry > 0:  # 還有剩進位的話
            prev.next = ListNode(carry)  # 就再多一位數

        return reverse(head)  # 最後的答案，要再轉回來一次

