# 數一數, 有幾個點符合「它的值,是子孫值的和」
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helper(root):
            if root==None: return 0
            children = helper(root.left) + helper(root.right)
            if children == root.val: 
                self.ans += 1 # 多找到一個答案
            return children + root.val # 之下的答案
        helper(root)
        return self.ans
