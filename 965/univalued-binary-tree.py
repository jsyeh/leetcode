# 想確認tree裡每個node的值都相同，就用 verifyAll 配上val值來檢查
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def verifyAll(root, val): # 是否值符合？
            if root==None: return True # 順利走到結束
            if root.val != val: return False # 遇到不相同
            return verifyAll(root.left, val) and verifyAll(root.right, val)
            # 是否左右都同時符合？
        
        return verifyAll(root, root.val)
