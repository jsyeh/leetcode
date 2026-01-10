# LeetCode 1161. Maximum Level Sum of a Binary Tree
# binary tree 橫向分析「同一層的 level sum」，問「最大的 level sum」在哪一層
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSum = [-inf]  # 各層放在陣列裡，最後會避開-inf，只看 levelSum[1:]
        def helper(root, level):  # 用「函式呼叫函式」找答案
            if root==None: return  # 末端「什麼都沒有」結束
            if len(levelSum)<=level:  # 如果 levelSum 陣列不夠長
                levelSum.append(root.val)  # 就多一層、增長陣列
            else:
                levelSum[level] += root.val  # 已經有，就「加進去」
            helper(root.left, level+1)  # 左邊的「下一層」
            helper(root.right, level+1)  # 右邊的「下一層」
        # 定義好 helper() 函式後，就可以「函式呼叫函式」更新 level sum
        helper(root, 1)  # 從「第1層」開始找
        target = max(levelSum)  # 找到「最大的 level sum」
        for level in range(len(levelSum)):  # 逐層找「最大的 level sum」在哪一層
            if levelSum[level]==target: return level  # 找到就回傳 level 層

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right        
