# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # 要找到 BST 樹裡，與 target 最接近的數
        # 每次左右，要決定往那個方向找
        ans = root.val # 先隨便挑 root 的值當答案
        now = root # 現在從 root 開始往下走
        while now != None: # 只要 now 還沒撞到底，就繼續做
            if abs(now.val-target)<abs(ans-target): # 答案更接近
                ans = now.val # 就更新
            elif abs(now.val-target)==abs(ans-target) and now.val < ans:
                ans = now.val # 答案一樣接近，但數字更小，就更新

            if target < now.val: # 目標在左邊，就找左半邊
                now = now.left
            else: # 目標在右邊，就找右半邊
                now = now.right
                
        return ans
