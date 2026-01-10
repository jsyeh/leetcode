# LeetCode 700. Search in a Binary Search Tree
# 在 Binary Search Tree 裡，找出 val 的 node
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(root, target):
            if root == None: return None
            if root.val==target: return root
            if root.val < target:
                return helper(root.right, target)
            else: return helper(root.left, target)
        return helper(root, val)
