# LeetCode 1740. Find Distance in a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def findPath(root, p):
            if root == None: return False # 沒找到
            if root.val == p: return True # 找到
            path.append('L')
            if findPath(root.left, p): return True
            path[-1] = 'R'
            if findPath(root.right, p): return True
            path.pop()
            return False
        path = []
        findPath(root, p)
        path0, path = path, []
        findPath(root, q)
        
        L0, L = len(path0), len(path)
        for i in range(max(L0, L)):
            if i<L0 and i<L and path0[i]==path[i]:
                continue
            else:
                return L0-i + L-i
        return 0
