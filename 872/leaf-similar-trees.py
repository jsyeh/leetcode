# 本題有 tree 結構，問最下面的 leaf 是否「都相同」。
# 可利用 DFS 找到 leaf 的結果
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def TreeLeaf(root):
            if root==None: return [] # 空list
            if root.left==None and root.right==None: # leaf node
                return [root.val] # leaf 的值
            ans = TreeLeaf(root.left) # 左邊樹的 leaf
            ans.extend(TreeLeaf(root.right)) # 右邊樹的 leaf
            return ans

        # print(TreeLeaf(root1))
        #print(TreeLeaf(root2))
        return TreeLeaf(root1) == TreeLeaf(root2)
