# LeetCode 145. Binary Tree Postorder Traversal
# 給你「二元樹」，照著課本 postorder 走法，走過一次
# 遇到 tree 的問題，用「函式呼叫函式」特別容易寫。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def visit(root):
            if root==None: return  # 終止條件
            visit(root.left)  # 先試左邊
            visit(root.right)  # 再試右邊
            ans.append(root.val)  # 最後 postorder 放自己
        visit(root)  # 整個 tree 從 root 樹根開始走
        return ans  # 累積的答案在這裡
