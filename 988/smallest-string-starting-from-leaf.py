# 0..25 對應 'a'..'z'
# tree 的結構裡，要從 Leaf往上組字，找「對應比較小」的字串
# 因從下往上組字，所以需要走到 leaf 再進行比對。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        table = [chr(ord('a')+i) for i in range(26)]
        def helper(root, nowStr): # 現在的字串 nowStr 會慢慢變長
            if root==None: return nowStr # 走到最下面，回傳「累積的字串」
            # 左邊空，回傳右邊； 右邊空，回傳左邊
            if root.left==None: return helper(root.right, table[root.val]+nowStr)
            if root.right==None: return helper(root.left, table[root.val]+nowStr)
            # 兩邊都有，回傳小的那個
            return min(helper(root.left, table[root.val]+nowStr), helper(root.right, table[root.val]+nowStr))
        return helper(root, '')
