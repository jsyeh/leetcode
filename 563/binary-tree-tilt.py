# 要將 tree 的 node tilt的總合，也就是全部的abs(左樹總和-右樹總和)
# tree本身的值，會變成它的 children 的差
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def childSum(root) -> int: # 會回傳「此樹的加總」 同時會把abs()答案加到 ans 裡
            if root==None: return 0
            left = childSum(root.left)
            right = childSum(root.right)
            self.ans += abs(left-right) # 同時會把答案加到 ans 裡
            return left + right + root.val
        
        childSum(root) # 計算加總，並把tilt abs()答案累積到 self.ans
        return self.ans
