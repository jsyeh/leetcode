# LeetCode 2130. Maximum Twin Sum of a Linked List
# 問「頭尾相加」的組合，加起來「最大值」有多大？
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        a = []
        while head != None:
            a.append(head.val)
            head = head.next
        N = len(a)
        for i in range(N//2):
            ans = max(ans, a[i]+a[N-1-i])
        return ans
