# LeetCode 114. Flatten Binary Tree to Linked List
# 把 tree 用 pre-order 的方式，變成一顆歪斜的 tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None: return  # 遇到空的，就直接結束
        ans = []  # 把答案的 nodes 依序放在 ans list 裡
        
        def helper(root):
            if root==None: return
            ans.append(root)  # 先放中間
            helper(root.left)  # 再放左邊
            helper(root.right)  # 再放右邊

        helper(root)
        # 最後一個不用再接，其餘的，都接到下一格的node
        for i in range(len(ans)-1):
            ans[i].left = None
            ans[i].right = ans[i+1]


