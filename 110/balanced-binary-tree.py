# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root) -> int:
            if root == None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            return 1 + max(left, right)
        
        if root == None: return True

        if not self.isBalanced(root.left): 
            return False
        if not self.isBalanced(root.right):
            return False

        left = depth(root.left)
        right = depth(root.right)
        if abs(left-right)<=1: return True
        else: return False
