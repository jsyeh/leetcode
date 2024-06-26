# LeetCode 1382. Balance a Binary Search Tree
# 要把 binary search tree 變 balance 左右深度最多差1
# 可先把 binary search tree 變成 array, 再二分法變回tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        array = []
        def helper(root): # 先把 tree 變成 array
            if root==None: return
            helper(root.left)
            array.append(root.val)
            helper(root.right)
        helper(root)  # 先把 tree 變成 array
        
        def buildTree(i, j): # 給左右邊界的 i:left, j:right
            if i>j: return None # 左右邊界不合理
            if i==j: return TreeNode(array[i]) # 左右邊界夾擊
            mid = (i+j)//2 # 挑正中間
            left = buildTree(i, mid-1) # 切左半
            right = buildTree(mid+1, j) # 切右半
            return TreeNode(array[mid], left, right) # 再合起來

        return buildTree(0, len(array)-1)
