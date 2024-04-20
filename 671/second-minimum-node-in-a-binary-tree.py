# 要找到 tree 裡「第2小的數」
# (1) 解法應該是「先找最小的數」，同時就會更新「第2小的數」
# 不過題目有個有趣的限制：root一定是最小的數
# (2) 另一種解法，是「只要與 root 不同，就是「第2小的數」
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.small1, self.small2 = -1, -1 # 一開始都沒有數
        def helper(root):
            if root==None: return
            if self.small1==-1 or root.val<self.small1: # 最小
                self.small2 = self.small1
                self.small1 = root.val
            elif root.val!=self.small1 and (self.small2==-1 or root.val<self.small2): # 次小
                self.small2 = root.val
            helper(root.left)
            helper(root.right)
        helper(root)
        return self.small2 # 第2小的數
# case 12/39: [5,8,5]
