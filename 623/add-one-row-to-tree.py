# 要將某個數字val，插入tree的第depth行
# 應該還是「函式呼叫函式」來解
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if root==None: return None
        if depth==1: # 特殊狀況，要新建更上面一層
            root = TreeNode(val, root, None) # 舊的接在左邊
        elif depth==2: # 測試結果，發現要設2才能正確（設1就會太低）因為是1-index開始
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else: # 層數還沒到，就再往下「函式呼叫函式」
            self.addOneRow(root.left, val, depth-1)
            self.addOneRow(root.right, val, depth-1)
        return root
