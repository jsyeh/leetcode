# 找「最下面、最左邊」的值。
# 「最下面」，所以需要 depth 的資訊
# 可以使用 list left來存「每一層」最左邊的值
# 那 left[-1] 是最下面那層的最左邊的值，就是答案
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        left = [] # 會記每一層的「最左邊」的值
        def helper(root, level): # 會去查某個level的最左邊的值
            if root==None: return # 沒有值，就避開
            if len(left)<level: # 若層數不足，表示沒來過
                left.append(root.val) # 那這就是最左邊的值
            helper(root.left, level+1) # 先處理左邊「函式呼叫函式」
            helper(root.right, level+1) # 再處理右邊「函式呼叫函式」
        helper(root, 1) # 最上面一層，開始逐層往下處理
        return left[-1] # 最下面一層的答案
