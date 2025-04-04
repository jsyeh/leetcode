# LeetCode 1123. Lowest Common Ancestor of Deepest Leaves
# 在 Binary Tree 裡，找「最低葉子」，再找出「最低葉子」的LCA共同的祖先
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):  # 函式呼叫函式，幫忙找出「這個分支」的深度、對應的LCA共同的祖先
            if root==None: return 0, None  # 外面的外面，什麼都沒有
            depth1, LCA1 = helper(root.left)  # 函式呼叫函式
            depth2, LCA2 = helper(root.right)  # 函式呼叫函式
            if depth1 > depth2: return (depth1+1, LCA1)  # 左邊比較深，用左邊的
            if depth2 > depth1: return (depth2+1, LCA2)  # 右邊比較深，用右邊的
            return (depth1+1, root)  # 兩邊一樣深，恭喜「你」就是新的LCA共同的祖先
        depth, LCA = helper(root)  # 函式呼叫函式
        return LCA  # 共同的祖先
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

