# LeetCode 1214. Two Sum BSTs
# 兩個 BSP tree，是否能挑出兩個 nodes 相加是 target
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        table = set()
        def buildTable(root):  
            if root==None: return 
            table.add(root.val)
            buildTable(root.left)
            buildTable(root.right)
        def findTable(root):  # 要找 target - node.val 是否在 table 裡
            if root==None: return False
            if target - root.val in table: return True
            return findTable(root.left) or findTable(root.right)
        buildTable(root1)
        return findTable(root2)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
