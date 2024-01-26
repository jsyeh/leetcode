# 想找出 p q 的共同祖先
# 因為都有 self.parent 往上一層，所以把「往上一層」加入set()即可找到
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        path = set()
        while p != None:
            path.add(p) # 持續建「往祖先的path」
            p = p.parent # 往上一層
        # 建好 p 的 parent path 後，再讓 q 去撞
        while q != None:
            if q in path: # 有撞到 path
                return q # 就是找到「共同的祖先」
            q = q.parent # 往上一層
