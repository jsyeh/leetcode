# LeetCode 107. Binary Tree Level Order Traversal II
# 從下到上，把 tree 每層建出來
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def helper(root, level):
            if root==None: return
            if len(ans)<=level:
                ans.append([root.val])
            else:
                ans[level].append(root.val)
            helper(root.left, level+1)
            helper(root.right, level+1)

        helper(root, 0)
        return ans[::-1]  # 把建出來的list 反過來
