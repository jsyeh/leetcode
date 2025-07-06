# LeetCode 333. Largest BST Subtree
# 在 tree 裡，找「最大的BST tree」裡面有幾個 nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(root):  # 用「函式呼叫函式」檢查全部的 sub tree
            # 回傳「最佳答案, 本root為主答案, 左界, 右界」
            if root==None:  # 沒有東西，學 Stefan 巧妙技巧, 利用 inf 和 -inf
                return 0, 0, inf, -inf  # 無答案, 非BST, 反, 反
            ans1, now1, left1, right1 = helper(root.left)
            ans2, now2, left2, right2 = helper(root.right)
            left = min(left1, root.val)
            right = max(root.val, right2)
            if right1 < root.val < left2:  # 合理的 BST
                now = now1 + now2 + 1  # 加上自己本身
            else: now = -inf  # 學 Stefan 巧妙技巧, 利用 -inf
            return max(ans1, ans2, now), now, left, right
        print(helper(root))
        return helper(root) [0]
