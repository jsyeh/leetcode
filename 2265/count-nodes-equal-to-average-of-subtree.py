# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helper(root)->[]: # 回傳 sum 及 count
            if root==None: return [0, 0] # 沒有人
            sum1, count1 = helper(root.left) # 左半樹
            sum2, count2 = helper(root.right) # 右半樹
            if (sum1+sum2+root.val)//(count1+count2+1)==root.val: # 看 root 之下的樹的 sum // count 是否合格
                self.ans += 1 # 合格的話 +1
            return [sum1+sum2+root.val, count1+count2+1] # 再回報給樓上
        helper(root)
        return self.ans 
        
