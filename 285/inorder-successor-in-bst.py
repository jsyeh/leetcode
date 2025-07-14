# LeetCode 285. Inorder Successor in BST
# 在「左邊小、右邊大」的二元搜尋樹 Bineary Search Tree 裡，給 p 找到 p 的下一個 node 的值
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # 可看 p 的值，了解「在左邊or在右邊」
        if root==None: return None  # 走到盡頭
        if root.val <= p.val: return self.inorderSuccessor(root.right, p)  # 在右邊
        # 如果答案在左邊，那可能會是 root 或是「左邊的答案」
        ans = self.inorderSuccessor(root.left, p)  # 試左半邊
        if ans == None: return root  # 左邊都沒有，那就是中間了
        return ans
