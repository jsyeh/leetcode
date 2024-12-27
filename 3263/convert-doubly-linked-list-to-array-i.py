# LeetCode 3263. Convert Doubly Linked List to Array I
# 把 Doubly Linked List 變成陣列
class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        ans = []
        while root != None:  # 直接用 while 迴圈，一直往右巡即可
            ans.append(root.val)
            root = root.next
        return ans
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
