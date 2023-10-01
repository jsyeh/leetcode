# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = [] # 一開始是空的 list, 
        def helper(root, level: int): # 利用 helper()幫忙
            if root==None: return # 終止條件

            if len(ans)<=level: # ans沒有對應的那層
                ans.append([root.val]) # 就新增那層
            else: # 若有對應的那一層
                if level%2==0: # zigzag 的偶數層往右加
                    ans[level].append(root.val)
                else: # zigzag 的奇數層往左插入
                    ans[level].insert(0, root.val)
            helper(root.left, level+1) # 函式呼叫函式
            helper(root.right, level+1) # 函式呼叫函式

        helper(root, 0) # 請 helper 整個做一次
        return ans
