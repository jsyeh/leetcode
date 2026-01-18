# LeetCode 1372. Longest ZigZag Path in a Binary Tree
# 在 Binary Tree 裡，找到「左、右、左、右」這樣走動的 Path，最長的長度
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(root):  # return 左邊的長、右邊的長、曾出現的最長的
            if root==None: return [-1,-1,-1]  # 左邊的長、右邊的長、曾出現的最長的
            left1,right1,ans1 = helper(root.left)  # 左邊的孩子，要取右邊的值
            left2,right2,ans2 = helper(root.right) 
            left = right2+1  # 左邊的孩子，要取右邊的值
            right = left1+1
            return [left, right, max(left,right,ans1,ans2)]
        return helper(root)[2]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
