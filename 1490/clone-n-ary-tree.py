"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root==None: # 空指標另外處理
            return None
        ans = Node(root.val)
        for child in root.children:
            one = self.cloneTree(child)
            ans.children.append(one)

        return ans

