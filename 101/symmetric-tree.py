# LeetCode 101. Symmetric Tree
# 可以用「函式呼叫函式」查看左、右的樹，是否相同。不相同，就失敗。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left, right):
            if left==None and right==None: return True # 剛好都是 None, 很好
            if left==None or right==None: return False # 有人空、有人不空，糟
            if left.val != right.val: return False # 兩邊不相同，糟
            return helper(left.left, right.right) and helper(left.right, right.left) # 左右對稱的比較
        return helper(root.left, root.right)
