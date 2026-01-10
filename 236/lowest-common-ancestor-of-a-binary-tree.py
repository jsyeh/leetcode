# LeetCode 236. Lowest Common Ancestor of a Binary Tree
# 在 Binary tree 裡，找到 p 和 q 的共同祖先
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def helper(root, p, q): # 看「中幾個」
            if self.ans != None: return 2  # 找到答案，直接結束
            if root==None: return 0  # 終止條件
            found = 0
            if root==p or root==q: found += 1
            found += helper(root.left, p, q) + helper(root.right, p, q)
            if found==2 and self.ans == None:
                self.ans = root
            return found
        helper(root, p, q)
        if self.ans==None: return root
        return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
