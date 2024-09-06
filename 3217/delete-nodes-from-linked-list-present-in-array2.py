# LeetCode 3217. Delete Nodes From Linked List Present in Array
# 把 Linked List 裡 val 是 nums 的，都刪掉。因 nums <= 10^5 需要 HashSet 加速
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        bad = set(nums)  # 做出對照表，讓 nums[i] 都放到 bad 裡
        # 因 head.val 可能也要刪掉，所以要用另一個ans來幫忙放答案
        prev = ans = ListNode(0, head)  # ans.next 會放真的答案
        now = prev.next  # prev 是前一項，now 是下一項
        while now != None:  # 下一項還有的話，才做檢查
            if now.val in bad: # 如果需要把 now 刪掉
                prev.next, now = now.next, now.next  
                # prev不動，prev.next 避開這一筆, now 換下一筆
            else: # 沒事、要保留的話
                prev, now = now, now.next  # 正常走到下一筆
        return ans.next
