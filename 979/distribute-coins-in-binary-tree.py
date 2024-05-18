# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def helper(root):  # 把它之下的金幣總數 及 以下node數
            if root == None: return (0,0)  # 終止條件
            leftCoin, leftN = helper(root.left)
            rightCoin, rightN = helper(root.right)
            self.ans += abs(leftCoin-leftN) + abs(rightCoin-rightN)
            # 如果金幣總數 vs. node不符時，這層樓就有金幣要「移轉」。資訊也都要回傳。
            return (leftCoin+rightCoin+root.val, leftN+rightN+1)

        self.ans = 0
        helper(root)
        return self.ans
# case 11/148: root = [1,0,0,null,3]
