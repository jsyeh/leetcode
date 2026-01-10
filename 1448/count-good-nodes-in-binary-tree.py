# LeetCode 1448. Count Good Nodes in Binary Tree
# 「從root到node」的node是最大的值，叫 Good Node，有幾個？
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, currentMax):
            if root==None: return 0
            if root.val < currentMax:  # 現在的 node 不是 good
                return helper(root.left, currentMax) + helper(root.right, currentMax)
            # 現在的 node 是 good 的話，要再 +1
            return 1 + helper(root.left, root.val) + helper(root.right, root.val)
        return helper(root, root.val)
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
