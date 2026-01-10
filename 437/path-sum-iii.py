# LeetCode 437. Path Sum III
# 想知道有幾條 path sum 加起來剛好是 targetSum
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        preSum = 0  # 利用 preSum 記錄 root 到 node 的 sum 值
        counter = Counter()  # 利用 counter 記錄「之前各種 preSum 出現的次數
        counter[0] += 1  # 最基礎的 case，讓 root 開始的 preSum 也有機會==targetSum
        def helper(root, preSum):  # 利用「函式呼叫函式」把 tree 全部走過一次
            if root==None: return 0  # 末端結束
            preSum += root.val  # 加入現在node的值
            ans = counter[preSum-targetSum]  # 到此 node 結束的 path 有幾種可能？
            
            counter[preSum] += 1  # 兩個小孩，都在「現在的基礎」出發
            ans += helper(root.left, preSum) + helper(root.right, preSum)
            counter[preSum] -= 1  # 算完後，再扣掉「現在的基礎」
            return ans
        return helper(root, 0)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# case 120/130: root = [1], targetSum = 0
