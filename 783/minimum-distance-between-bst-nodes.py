# 想找到 BST 樹裡，最小的距離。其實就用 in-order 的方式，
# 可依序「從小到大」找到每一個數。因此，就可找到最小距離的值
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 200000 # 先設「正很多」
        self.prev = -100000 # 先設「負很多」

        def helper(root):
            if root==None:
                return
            helper(root.left) # 左半樹

            if root.val - self.prev < self.ans:
                self.ans = root.val - self.prev
            self.prev = root.val # 更新 prev
            
            helper(root.right) # 右半樹

        helper(root) # 整個樹去處理
        return self.ans
