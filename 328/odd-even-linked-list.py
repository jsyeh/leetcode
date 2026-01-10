# LeetCode 328. Odd Even Linked List
# 把 Linked List 裡「第奇數個」放前面，「第偶數個」放後面
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd2 = odd = ListNode()  # 處理「第奇數個」
        even2 = even = ListNode()  # 處理「第偶數個」
        N = 1  # 現在處理第幾個數呢？
        while head:
            if N%2==1:
                head, odd2.next = head.next, head
                odd2, odd2.next = odd2.next, None
            else:
                head, even2.next = head.next, head
                even2, even2.next = even2.next, None
            N += 1  # 換下一個數
        odd2.next = even.next
        return odd.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
