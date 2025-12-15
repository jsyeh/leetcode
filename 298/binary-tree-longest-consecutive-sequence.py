# LeetCode 298. Binary Tree Longest Consecutive Sequence
# 在 tree 裡，找到「最長的加1的path」
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 1
        def helper(root):  # 回傳2個值：包含 node 的最大值
            if root==None: return 0
            ans = 1
            if root.left != None and root.left.val == root.val + 1:
                ans = 1 + helper(root.left)
            else:  # 沒辦法接起來，就「光說不練」讓它自己去試吧！
                helper(root.left)
            if root.right != None and root.right.val == root.val + 1:
                ans = max(ans, 1 + helper(root.right))
            else:  # 沒辦法接起來，就「光說不練」讓它自己去試吧！
                helper(root.right)
            self.ans = max(self.ans, ans)
            return ans
        helper(root)
        return self.ans
