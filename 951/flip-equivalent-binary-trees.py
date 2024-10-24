# LeetCode 951. Flip Equivalent Binary Trees
# 兩個 tree 是否是「任意左右 flip」後，做得出來
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1==None and root2==None: return True  # 兩邊都是空的
        if root1==None or root2==None: return False  # 一邊空、一邊不空
        if root1.val != root2.val: return False  # 左右不相同

        # 接下來有2種可能，一種是「左右沒flip」，一種是「左右有flip」都可以
        if self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right):
            return True
        if self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left):
            return True
        return False  # 如果都沒成功，就失敗

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
