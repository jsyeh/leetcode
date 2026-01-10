# LeetCode 236. Lowest Common Ancestor of a Binary Tree
# 在 Binary tree 裡，找到 p 和 q 的共同祖先
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if root==None: return 0, None
            count1, ans1 = helper(root.left, p, q)
            count2, ans2 = helper(root.right, p, q)
            if root==p or root==q:
                if count1 + count2==1: return 2, root
                else: return 1, root
            if count1>count2: return count1, ans1
            if count2>count1: return count2, ans2
            if count1==count2: return count1+count2, root
        count, ans = helper(root, p, q)
        return ans
