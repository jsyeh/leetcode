# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # 想到可用「函式呼叫函式」的方法，來找 tree的最大值、最小值
        def helper(root): # 會 return 最大值、最小值
            M1 = m1 = root.val # 自己本身是最大值、最小值
            M2 = m2 = root.val # 自己本身是最大值、最小值
            if root.left != None: # 如果左邊的樹有東西
                M1, m1 = helper(root.left) # 算出它的最大、最小值
            if root.right != None: # 如果右邊的樹有東西
                M2, m2 = helper(root.right) # 算出它的最大、最小值
            self.ans = max(self.ans, M1-root.val, root.val-m1) # 最大最小，與我的差距
            self.ans = max(self.ans, M2-root.val, root.val-m2) # 最大最小，與我的差距
            print(root.val, M1,m1, M2,m2)
            return max(root.val, M1,M2), min(root.val, m1,m2) # 最大最小值
        
        self.ans = 0
        helper(root) # 求答案，會更新 self.ans
        return self.ans
# case 27/28: [7,5,12,11,0,2,null,4,17,6,19,null,16,18,null,null,null,null,9,14,10,null,null,null,null,null,null,null,null,3,1,null,null,8,null,13,null,null,15]
