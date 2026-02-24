# LeetCode 1022. Sum of Root To Leaf Binary Numbers
# 將 Binary Tree「從root到葉子」的二進位數字「全部加起來」
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(root, code):  # 利用「函式呼叫函式」來解 tree 問題
            # code 對應「之前」二進位累積的值
            if root==None: return 0  # 終止條件：沒有 node 沒有值
            now = code * 2 + root.val  # 二進位「累積」到現在的值
            if root.left==None and root.right==None:  # leaf node
                return now  # 把「累積」的二進位的值，傳回去
            # 下面用「函式呼叫函式」來解 tree 的問題
            return helper(root.left, now) + helper(root.right, now)
        return helper(root, 0)  # 從頭開始呼叫函式「函式呼叫函式」

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
