# 樹的 leaf: 0:False, 1:True
# 其他 node: 2:OR, 3:AND
# 想要模擬結果，就照著規則模擬即可
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left==None and root.right==None: # leaf node
            return root.val==1 # 1就True, 0就False
        # 接下來，就是 non-leaf node
        if root.val==2: # OR
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else: # AND
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
