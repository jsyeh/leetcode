# LeetCode 1038. Binary Search Tree to Greater Sum Tree
# 把 Binary Search Tree 轉換成 「每個node的值」再加「右半邊的總和」
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0  # 這很像 global 變數, 函式裡用 self.sum 來變動
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root==None: return None  # 空的就直接回傳

        self.bstToGst(root.right) # 函式呼叫函式, 右邊先處理
        self.sum += root.val # 處理完右邊後, 把自己的值, 加入 self.sum 裡, 等下再交棒給左邊
        root.val = self.sum # 裡面的值, 改成「右半邊的sum」
        self.bstToGst(root.left)  # 交棒給左邊
        return root
