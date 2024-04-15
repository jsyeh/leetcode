# 想將 binary tree 裡，從上到下的每個 path 都做出對應的字串
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = [] # 答案一開始是空的 list
        def helper(root, nowStr):
            if root.left==None and root.right==None: # 到達底端葉子
                ans.append(nowStr + '->' + str(root.val)) # 答案就插入累積的字串
                return # 提早結束
            if root.left!=None: # 左邊有東西的，就往左邊走
                helper(root.left, nowStr + '->' + str(root.val))
            if root.right!=None: # 右邊有東西的，就往右邊走
                helper(root.right, nowStr + '->' + str(root.val))

        # 左邊有，可往左邊走。右邊有，可往右邊走
        if root.right!=None: 
            print('right')
            helper(root.right, str(root.val))
        if root.left!=None: 
            print('left)')
            helper(root.left, str(root.val))

        if root.left==None and root.right==None: # 如果只有root本身
            ans.append(str(root.val)) # 就只存 root 的字串
        return ans
