# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helper(root, level:int):
            if root != None:
                helper(root.left, level+1)
                helper(root.right, level+1)
            if level>self.ans:
                self.ans = level
        helper(root, 0)
        return self.ans
