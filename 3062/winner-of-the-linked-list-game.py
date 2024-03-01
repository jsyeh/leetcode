# head 裡, even, odd, even, odd 這樣兩兩比較, 分數高的得分。
# 最最後是 Odd 還是 Even 還是平手 Tie
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even, odd = 0, 0 # 一開始都晬0
        while head!=None: # 只要還有數字, 就繼續測
            if head.val > head.next.val: # 偶數較大
                even += 1
            else: # 奇數較大(因為奇偶不可能相同)
                odd += 1
            head = head.next.next # 跳兩格, 看下一組
        if even>odd: return "Even" # 偶數大 的多
        elif odd>even: return "Odd" # 奇數大 的多
        else: return "Tie" # 一樣多
