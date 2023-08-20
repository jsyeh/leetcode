# 這個題目比較麻煩，因若第1個node被刪除的話，不知道要怎麼刪、刪的話就沒有head了
# "You will not be given access to the first node of head."
# 這樣就沒辦法由 head 繞過「要刪除的node」
# 不過有個巧妙的解法，是 copy 下一筆的值，再「繞過」下一筆，就可以了
# 那最後一筆怎麼辦？ 測資 [4,5,1,9] 9 告訴我們 "cannot delete the tail."
# 所以太好了，不用管這個狀況。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next = node.next
        node.val = next.val # 把下一筆的值 copy 過來
        node.next = next.next # 把下一筆的 next 指標 copy 過來。
        # 也就是「要刪除的值」不見了，變身下一筆。
        # 自己當成「下一筆」的替身，再殺「下一筆」的本尊
