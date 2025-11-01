# LeetCode 3217. Delete Nodes From Linked List Present in Array
# nums 陣列裡，有「壞掉的值」要把它們在 Linked List 裡頭「避開」
# 可用 set() 快速比對「壞掉的值」，再利用 now 來處理資料，ans裡有「最後的結果」
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        bad = set(nums)  # 利用 set() 集合，可快速判斷「某數是否壞掉/不能用」
        now = ans = ListNode(0, head)  # 建出 ans node, 是 dummy head
        while now.next:  # 只要還有下一筆，就繼續處理
            if now.next.val in bad:  # 如果有壞掉，就避開
                now.next = now.next.next  # 站在原地，換處理更遠的「下一筆」
            else:  # 沒有壞掉，那這裡就不把關，直接順著「滑到」下一筆，再往下處理
                now = now.next
        return ans.next  # ans 是 dummy head，它的下一筆，便是真的答案

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
