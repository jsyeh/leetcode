# LeetCode 144. Binary Tree Preorder Traversal
# 將 tree 以 preorder 的方式走訪，也就是「中間」先，再左邊、再右邊
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(root):
            if root==None: return
            ans.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

