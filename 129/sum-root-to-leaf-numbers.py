# 把root走到leaf的數值，全部加起來，簡單「函式呼叫函式」即可！
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def pathSum(root, prev): # prev代表「之前累積的數」
            if root==None: return 0
            if root.left==None and root.right==None:
                return root.val + prev*10 # 遇到葉子，就可以回傳
            return pathSum(root.left, root.val+prev*10) + pathSum(root.right, root.val+prev*10)
        return pathSum(root, 0)
