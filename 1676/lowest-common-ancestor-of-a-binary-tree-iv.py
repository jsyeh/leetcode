# 想找出 nodes 裡的每個數字 「對應」tree裡的共同祖先
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        N = len(nodes) # 總共有N個不同的數字
        # 使用 set() 讓「比對」變快
        nodes = set([ node.val for node in nodes ])
        def helper(root)-> int: # 知道下面「有幾個」nodes 合格
            if root==None: return 0 # 遇到空的，就回傳0
            count1 = helper(root.left) # 左半
            count2 = helper(root.right) # 右半
            count3 = 1 if root.val in nodes else 0 # 本身
            total = count1 + count2 + count3
            if total == N: # 剛好達標
                self.ans = root # 記下答案
                return 0 # 設成0 之後才不會重覆達標（得到N）
            else:
                return total
        
        helper(root)
        return self.ans
