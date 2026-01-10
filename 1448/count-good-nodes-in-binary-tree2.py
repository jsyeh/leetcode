# LeetCode 1448. Count Good Nodes in Binary Tree
# 「從root到node」的node是最大的值，叫 Good Node，有幾個？
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, big):
            if root==None: return 0
            ans = helper(root.left, max(big, root.val)) + helper(root.right, max(big, root.val))
            if root.val >= big: 
                return ans + 1
            return ans
        return helper(root, root.val)
