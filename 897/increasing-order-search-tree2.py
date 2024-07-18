# LeetCode 897. Increasing Order Search Tree
# 想建出一個「往右偏斜」的tree，可把 BST Tree 先變成 array 再建 tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        array = []
        self.now = self.ans = TreeNode()
        def helper(root):
            if root==None: return
            helper(root.left)
            self.now.right = TreeNode(root.val) # 往右建 tree
            self.now = self.now.right
            helper(root.right)
        
        helper(root)
        return self.ans.right
