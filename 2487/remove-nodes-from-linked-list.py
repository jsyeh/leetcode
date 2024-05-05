# 給個 Linked List，如果node的右邊有更大的值，就把node刪掉
# 感覺很像 mono stack 的題目
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果右邊有任何人比你大，你就不能存在
        # 但 10^5 太多node,沒辦法暴力逐一往右測試。
        # 使用 mono stack 來解即可。
        stack = []  # mono stack, 如果有更大的值，就pop()
        while head is not None:
            while stack and head.val > stack[-1]:  # 更大，要一直清
                stack.pop()
            stack.append(head.val)
            head = head.next
        # print(stack) # 印出來看，還不錯！
        # 再建出 linked list
        ans = None
        for i in range(len(stack) - 1, -1, -1):
            ans = ListNode(stack[i], ans)
        return ans

