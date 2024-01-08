# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 在BST樹裡, 給low-high界, 把出 sum, 就用函式呼叫函式即可
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root==None: return 0 # 沒有任何值

        ans = 0
        if low <= root.val <= high: ans += root.val # 在範圍內, 就加

        if low <= root.val: ans += self.rangeSumBST(root.left, low, high) # 左邊在範圍內, 丟下去問
        if root.val <= high: ans += self.rangeSumBST(root.right, low, high) # 右邊在範圍內, 丟下去問
        return ans
