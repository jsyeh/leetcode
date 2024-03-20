# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ans = list1
        for i in range(a-1): # 先跳過a-1個
            list1 = list1.next
        # 接下來, 先手術, 把 b 接到 list1 的中間
        another = list1 # 另外一個
        # 把 list1 再跳掉 a...b 的部分
        for i in range(b-a+2): # 因為頭尾的部分都有少算,所以再多走2格
            list1 = list1.next

        another.next = list2 # 另一個的下一筆,接上 list2
        # list1 再往後跳開
        # 走完 list2
        while list2.next!=None: # 不是最後1個
            list2 = list2.next
        # 最後, 把 list2的結尾, 再接回 list1
        list2.next = list1
        # 成功接好了
        return ans
