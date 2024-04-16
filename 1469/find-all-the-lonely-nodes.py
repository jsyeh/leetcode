# lonely node 獨生子
# 關於tree的題目，大部分都用「函式呼叫函式」即可
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(root):
            if root==None: return # 沒有東西
            if root.left==None and root.right!=None: # 右邊的獨生子
                ans.append(root.right.val)
                helper(root.right)
            elif root.left!=None and root.right==None: # 左邊的獨生子
                ans.append(root.left.val)
                helper(root.left)
            else: # 兩邊都有小孩，那就兩邊都繼續做下去
                helper(root.left)
                helper(root.right)
        helper(root)
        return ans
