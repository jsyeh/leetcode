# LeetCode 1339. Maximum Product of Splitted Binary Tree
# 將 Binary Tree 斷成2個，裡面相加，再兩個 tree 相乘，要「最大」
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # 兩塊加總，等於「先把加總」再減掉「某個subtree」便是剩下那塊
        def sumAll(root):  # 用「函式呼叫函式」將整個 Tree 加總
            if root==None: return 0
            return root.val + sumAll(root.left) + sumAll(root.right)
        total = sumAll(root)  #用「函式呼叫函式」將整個 Tree 加總
        self.ans = 0  # 要找到「相乘」最大
        MOD = 10**9+7  # 因為數很大，需要「取餘數」
        def helper(root):  # 用「函式呼叫函式」找答案
            if root==None: return 0  # 終止條件
            left = helper(root.left)  # 左邊 subtree 的加總「函式呼叫函式」
            right = helper(root.right)  # 右邊 subtree 的加總「函式呼叫函式」
            # 把某個 subTree * (total - subTree) 找最大
            self.ans = max(self.ans, left * (total-left), right * (total-right))
            return root.val + left + right  # 這個 subtree 的加總
        helper(root)  # 函式呼叫函式，以更新 self.ans
        return self.ans % MOD  # 要「取餘數」

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
