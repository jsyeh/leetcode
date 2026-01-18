# LeetCode 1372. Longest ZigZag Path in a Binary Tree
# 在 Binary Tree 裡，找到「左、右、左、右」這樣走動的 Path，最長的長度
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helper(root):  # 回傳2個方向的長度、答案
            if root==None: return 0, 0
            ans1, ans2 = helper(root.left)
            ans3, ans4 = helper(root.right)
            self.ans = max(self.ans, ans1, ans2+1, ans3+1, ans4)
            return ans2+1, ans3+1 

        helper(root)
        return self.ans - 1
# case 38/58: [2,8,6,1,1,7,9,8,9,3,1,4,8,null,5,3,4,10,10,2,null,5,null,3,7,null,3,null,4,6,2,8,4,5,null,null,9,null,6,null,6,null,null,2,2,null,3,2,null,null,8,1,9,8,8,5,10,null,9,null,8,null,null,null,null,5,7,2,10,null,null,null,null,null,null,3,null,2,null,null,null,8,7,null,null,3,1,null,3,null,null,null,7,1,null,3,null,null,null,null,2,null,2,null,4,7,4,null,null,null,9,null,null,null,null,8,8,null,null,null,null,7,2,1,4,null,4,7,null,5,9,null,7,9,7,null,10,9,6,null,null,7,2,3,null,2,null,9,5,9,null,null,5,null,5,9,null,null,null,null,9,null,null,null,null,null,7,null,null,null,null,null,null,null,9,null,4,1,null,null,null,null,4,4,null,null,4,null,null,null,4]
