# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 想算 diameter, 就把 left+right 每個都測，找最大值
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def depth(root):
            if root==None: return 0 # 長度為0
            left = depth(root.left)
            right = depth(root.right)
            self.ans = max(self.ans, left+right) # 是否有更好的答案
            return max(left, right) + 1 # 長度+1

        depth(root) # 測一輪
        return self.ans
