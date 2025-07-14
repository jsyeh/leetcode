# LeetCode 1290. Convert Binary Number in a Linked List to Integer
# 把二進位的 Linked List，轉換成整數。可使用迴圈 ans = ans * 2 + head.val
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        while head != None:  # 針對 Linked List 可用 while 迴圈「逐一走過」
            ans = ans * 2 + head.val  # 組合出「二進位」的答案
            head = head.next  # 「下面一位」
        return ans
