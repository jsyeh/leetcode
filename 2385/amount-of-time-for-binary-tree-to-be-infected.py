# 有點像病毒感染, 先在 start 的位置開始, 然後往外漫延
# 什麼時候全部 infect 也就是要算「開始」到每一個點的「最大距離」
# 我們在 helper()呼叫時，要回傳2個資料：有毒的深度、沒有毒的最長深度
#  如果現在是毒，那先用child的最大長度來更新 ans
#  如果左邊有毒，那毒的深度 + 右邊 safe 的長度起來來，更新ans
#  如果右邊有毒，那毒的深度 + 左邊 safe 的長度起來來，更新ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def helper(root, start)->(int,int): # 回傳有毒的深度、沒有毒的最大深度（如果兩邊都沒毒，就是最大深度）
            if root==None: return (-1, -1) # 遇到末端,就確定長度
            virus1, safe1 = helper(root.left, start) # 左邊問
            virus2, safe2 = helper(root.right, start) # 右邊問
            if root.val == start: # 我自己就是毒
                self.ans = max(self.ans, safe1+1, safe2+1) # 下面的長度最大值
                return (1, 0) # 有毒、沒有乾淨的child
            if virus1==-1 and virus2==-1: # 左右都沒毒
                return (-1, max(safe1,safe2)+1) # 沒毒、長度+1
            elif virus1>-1: # 左邊有毒
                self.ans = max(self.ans, virus1+safe2+1) # 毒的深度+沒有毒的深度
                return (virus1+1, 0) # 回傳毒的深度
            elif virus2>-1: # 右邊有毒
                self.ans = max(self.ans, virus2+safe1+1) # 毒的深度+沒有毒的深度
                return (virus2+1, 0) # 回傳毒的深度
        self.ans = 0
        helper(root, start) # 請 helper() 來找答案
        return self.ans
