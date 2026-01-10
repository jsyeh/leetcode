# LeetCode 2130. Maximum Twin Sum of a Linked List
# 問「頭尾相加」的組合，加起來「最大值」有多大？
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        # 把 Linked List 先複製成 array 即可
        a = []
        head2 = head
        while head != None:
            a.append(head.val)
            head = head.next
        # 複製好後，再用「倒過來的 for 迴圈，逐一檢查頭尾
        for i in range(len(a)-1, -1, -1):
            ans = max(ans, head2.val + a[i])
            head2 = head2.next
        return ans
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
