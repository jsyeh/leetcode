# 本題是要計算 Subtree 的 average, 找最大的 average
# 但不是找最大的 Node value，因為leaf如果值很小，就會影響到
# 所以要持續算 sum 及 count 以便做除法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.ans = 0
        def helperSumAndCount(root) -> (int,int): # 回傳Sum 及 Count
            if root==None: # 空的 subtree
                return (0,0) # Sum是0、Count也是0

            leftSum, leftCount = helperSumAndCount(root.left) # 函式呼叫函式
            rightSum, rightCount = helperSumAndCount(root.right)

            # 先判斷目前的「平均」是否更大
            totalSum = leftSum+rightSum+root.val
            totalCount = leftCount+rightCount+1
            if totalSum / totalCount > self.ans: # 若更大，就更新
                self.ans = totalSum / totalCount

            return (totalSum, totalCount)

        helperSumAndCount(root)
        return self.ans
