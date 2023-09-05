"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# 使用 HashMap 來找到 Random pointer 的對應關係
# two-pass，第一次建出連接架構 & 建 hash table
# 第二次（查表）填好random資訊
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        table = {} # table[舊] = 新
        ans = Node(0) # 從 ans.next 開始放值
        head2 = head # 不想破壞 head, 所以複製成 head2
        now = ans
        while head2 != None:
            now.next = Node(head2.val)
            table[head2] = now.next # 最重要，建立「舊-新關係」
            head2 = head2.next
            now = now.next

        head2 = head
        now = ans.next
        while head2 != None:
            if head2.random == None:
                now.random = None # 因前面漏建 table[None] = None
            else:
                now.random = table[head2.random]
            now = now.next
            head2 = head2.next
        return ans.next
