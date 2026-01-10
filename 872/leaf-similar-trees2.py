# LeetCode 872. Leaf-Similar Trees
# 想知道 binary tree 裡的 leaf 組出來，是否都相同
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findLeaf(root, ans):
            if root==None: return
            if root.left==None and root.right==None: ans.append(root.val)
            findLeaf(root.left, ans)
            findLeaf(root.right, ans)
        ans1, ans2 = [], []
        findLeaf(root1, ans1)
        findLeaf(root2, ans2)
        return ans1 == ans2
