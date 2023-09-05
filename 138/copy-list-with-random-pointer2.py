"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# 完成 1490. Clone N-ary Tree 後，想到另外一種寫法
class Solution:
    table = {} # 建立 Hash Table
    def build(self, head):
        if head==None: return None
        ans = Node(head.val)
        self.table[head] = ans # 建立 Hash Table
        ans.next = self.build(head.next)
        return ans

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None: return None
        
        ans = self.build(head)
        self.table[None] = None # 補建 None -> None 對照

        ans2, head2 = ans, head
        while ans2 != None:
            ans2.random = self.table[head2.random]
            ans2, head2 = ans2.next, head2.next

        return ans
