# LeetCode 549. Binary Tree Longest Consecutive Sequence II
# 在 binary tree 裡，找到「連續數字」的 path，即「任兩node間的path」
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helper(root):  # 回傳 [inc,dec]
            if root==None: return [0, 0]
            inc = dec = 1
            if root.left != None:
                inc1, dec1 = helper(root.left)
                if root.val == root.left.val + 1:
                    dec = max(dec, dec1 + 1)
                if root.val == root.left.val - 1:
                    inc = max(inc, inc1 + 1)
            if root.right != None:
                inc2, dec2 = helper(root.right)
                if root.val == root.right.val + 1:
                    dec = max(dec, dec2 + 1)
                if root.val == root.right.val - 1:
                    inc = max(inc, inc2 + 1)
            self.ans = max(self.ans, inc + dec - 1)
            return [inc, dec]
        helper(root)
        return self.ans
