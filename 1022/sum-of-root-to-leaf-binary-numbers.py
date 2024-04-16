# 從 root 到 leaf 以「二進位」來表現
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(root, prev): # 幫忙「函式呼叫函式」處理。prev 記錄之前走過的2進位數
            if root==None: return 0 # 空指標，不處理

            now = prev*2 + root.val
            if root.left==None and root.right==None: return now # 遇到葉子，才回傳
            return helper(root.left, now) + helper(root.right,now) # 不是葉子，就繼續

        return helper(root, 0) 
