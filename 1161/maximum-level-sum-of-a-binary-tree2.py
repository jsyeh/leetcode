# LeetCode 1161. Maximum Level Sum of a Binary Tree
# binary tree 橫向分析「同一層的 level sum」，問「最大的 level sum」在哪一層
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSum = []
        def helper(root, level):
            if root==None: return
            if len(levelSum) <= level: levelSum.append(root.val)
            else: levelSum[level] += root.val
            helper(root.left, level+1)
            helper(root.right, level+1)
        helper(root, 0)
        v = max(levelSum)
        return levelSum.index(v) + 1
