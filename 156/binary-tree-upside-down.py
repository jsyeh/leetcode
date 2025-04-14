# LeetCode 156. Binary Tree Upside Down
# 左邊 node 變成「新root」，原本root變成「右邊」，右邊變「左邊」
# 題目保證「右邊最多1層」且「不會有小孩」。所以簡單了
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):  # 用「函式呼叫函式」來旋轉
            if root.left==None: return  # 左邊沒有，就終止、不用再旋轉了
            self.ans = TreeNode(root.left.val, root.right, self.ans)
            helper(root.left)  # 往左邊「繼續做」
        
        if root==None: return None
        self.ans = TreeNode(root.val)
        helper(root)
        return self.ans
