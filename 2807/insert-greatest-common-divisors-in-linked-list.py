# LeetCode 2807. Insert Greatest Common Divisors in Linked List
# 在 Linked List 裡，兩兩相鄰的 node 間，插入「兩人」的最大公因數
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, now = head, head.next  # 左、右 兩項
        while now != None:  # 還有右邊項，就可計算gcd()最大公因數
            prev.next = ListNode(gcd(prev.val,now.val), now)
            prev, now = now, now.next  # 接好指標後，右移下一組
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
