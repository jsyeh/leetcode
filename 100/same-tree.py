# 兩個樹是否相同，可用「函式呼叫函式」的方法解決
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None: return True # 兩個都是 None 是相同
        if p==None or q==None: return False # 但只有1個是 None 便失敗
        # 現在確認 p 和 q 都不是 None, 可細細分析
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True # 全部都相同（函式呼叫函式）
        else:
            return False
# case 55/65: p=[10,5,15] q=[10,5,null,null,15] 原來我程式裡 p q 有打錯
