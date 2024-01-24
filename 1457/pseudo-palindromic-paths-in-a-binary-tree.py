# 從root往leaf走，得到的數字「可組成Palindrome」迴文
# 也就是「字母出現次數」都會是偶數、最多只能有1個字母是奇數
# tree裡有 10^5個nodes，所以不能用暴力法「去試全部的tree path
# 但再想想，好像「暴力法」再配上 list 裡有9個數字去測「奇數<=1」又不會太慢。試吧！
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        used = [0]*10
        self.ans = 0

        def helper(root): # 會在 tree 裡逐一走過
            used[root.val] += 1 # 走進來，多現在的數字
            if root.left!=None: helper(root.left)
            if root.right!=None: helper(root.right)
            if root.left==None and root.right==None: # 現在是leaf node
                odd = 0
                for i in range(1,10):
                    if used[i]%2==1: odd += 1
                if odd<=1: # 合格、能做出 pseudo-palindrome
                    self.ans += 1
            used[root.val] -= 1 # 離開時，將數字數目還原
        
        helper(root)
        return self.ans
