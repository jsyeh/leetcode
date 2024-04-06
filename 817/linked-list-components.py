# head 對應的 linked list 裡，有許多相鄰、不重覆的數
# nums 裡的數，有幾組是 linked list 裡相鄰的數（就是相連）
# 策略：先把 nums 變成 set s，接著巡視 linked list 時，看有否在set 裡。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s = set(nums) # 建出 set, 以便在 linked list 裡查「有無出現」
        ans = 0
        connected = False
        while head != None:
            if not connected and head.val in s:
                connected = True # 從無到有
                ans += 1
            elif connected and head.val not in s:
                connected = False # 從有到無
            head = head.next # 下一筆
        return ans
