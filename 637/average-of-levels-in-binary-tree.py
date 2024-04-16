# 計算「每一層」總和後的平均
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = [] # ans[i] 對應 level i 的全部的數
        def helper(root, level): # 用 helper 來累積 ans
            if root==None: return # 結束
            if len(ans)<=level: # 還差這一層
                ans.append([root.val]) # 只好 append 新的一層
            else: # 已經有這一層
                ans[level].append(root.val) # 就 append 在這層的後面
            helper(root.left, level+1) # 函式呼叫函式
            helper(root.right, level+1) # 函式呼叫函式

        helper(root, 0)
        # 再把 ans[i] 轉換成平均答案 = sum(ans[i])/len(ans[i])
        for i in range(len(ans)):
            ans[i] = sum(ans[i])/len(ans[i])
        return ans
