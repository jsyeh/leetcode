# LeetCode 2583. Kth Largest Sum in a Binary Tree
# 找到「第k大」的 level sum (同一層的和)，可用「函式呼叫函式」可逐層分析
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelSum = []  # 用來存每一層的 sum
        def helper(root, level):  # 函式呼叫函式
            if root==None:  # 終止條件
                return
            if len(levelSum)<=level:  # 如果目前層數不夠
                levelSum.append(root.val)  # 就新加1層
            else:  # 層數夠的話，就更新這層的「總合」
                levelSum[level] += root.val
            helper(root.left, level+1)  # 函式呼叫函式，往下處理
            helper(root.right, level+1)  # 函式呼叫函式，往下處理

        helper(root, 0)  # 函式呼叫函式，從頭開始，往下處理
        levelSum.sort(reverse=True)  # 全部從大到小排好
        if k>len(levelSum):  # 如果層數不夠，就 return -1 (k 是 1-index)
            return -1
        return levelSum[k-1]  # 找到第k大的數（改成 0-index）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
