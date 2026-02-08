# LeetCode 110. Balanced Binary Tree
# 請問 Binary Tree 「每個node」的左右深度，是否都相同or差一。
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True  # 在出錯之前，是 True
        def helper(root):  # 用「函式呼叫函式」判斷tree的深度
            if root==None: return 0
            left = helper(root.left)  # 用「函式呼叫函式」解左邊
            right = helper(root.right)  # 用「函式呼叫函式」解右邊
            if abs(left-right) > 1:  # 任何時候，發現「左右差太多」
                self.ans = False  # 就變為 False
            return max(left,right) + 1  # 回覆這層的深度
        helper(root)  # 啟動「函式呼叫函式」
        return self.ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
