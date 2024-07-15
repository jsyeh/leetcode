# LeetCode 2196. Create Binary Tree From Descriptions
# 題目給一堆 [parent, child, isLeft] 請建出 Tree
# 可使用 dict 對應到 TreeNode。可使用 set() 來找到 root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        table = {}  # 一開始 dict 是空的，table[p] 將對應 p 的 TreeNode 
        roots = set((d[0] for d in descriptions))  # 有出現過、可能的 root
        for p,c,isLeft in descriptions: # parent, child, isLeft
            if c not in table: table[c] = TreeNode(c) # 建立 child 的 TreeNode
            if p not in table:  # 要建立 parent 的 TreeNode，內含 child 的 TreeNode
                if isLeft: table[p] = TreeNode(p, table[c], None)
                else: table[p] = TreeNode(p, None, table[c])
            else:  # 已有 table[p] 的 TreeNode，就更新 left 或 right 即可
                if isLeft: table[p].left = table[c]
                else: table[p].right = table[c]
            if c in roots: roots.remove(c)  # child 不可能是 root，所以拉掉
        return table[list(roots)[0]] # 把 set() 轉成 list，裡面唯一的那個，就是 root，找對應的 TreeNode
