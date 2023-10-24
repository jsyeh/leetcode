# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = [] # 用來放「每層的最大值」的答案
        def helper(root, level): # 請小幫手幫忙
            if root==None: # 空的node
                return # 就是終止條件

            N = len(ans) # 現在ans的長度
            if N<=level: # 因為從0開始，所以level如果與N相同，就要加層
                ans.append(root.val) # 把現在的值放在新的一層
            elif ans[level]<root.val: # 如果層數足夠的話，看是否值更大
                ans[level]=root.val # 更大的值，就可以更新
            helper(root.left, level+1) # 函式呼叫函式，左半樹
            helper(root.right, level+1) # 函式呼叫函式，右半樹
        
        helper(root, 0) # 就請小幫手幫忙，函式呼叫函式，全部去測
        return ans # 答案就出來了

        
