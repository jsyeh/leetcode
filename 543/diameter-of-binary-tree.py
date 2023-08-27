# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 想長出 diameter, 就把 length = depth(root.left)+depth(root.right)+2 找最長的 length
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0
        def depth(root):
            if root==None:
                return 0 # 提早結束的終止條件
                
            left, right = 0, 0
            if root.left != None:
                left = depth(root.left) + 1
            if root.right != None:
                right = depth(root.right) + 1
            length = left + right
            if length > self.maxLength:
                self.maxLength = length
            return max(left, right)
        
        depth(root) # 整個 tree 都測過一次
        return self.maxLength
        
