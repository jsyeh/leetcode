# 要逐步把 root 的葉子砍下來，依序存起來
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def findAndCutLeaves(root): # 砍一輪葉子
            if root==None: return False # 無法砍，放棄
            if root.left==None and root.right==None: # 剛好是葉子
                ans[-1].append(root.val) # 砍下來，保存葉子
                return True # it is leave node 告訴上一層 caller 說我要被砍，提早結束

            if findAndCutLeaves(root.left)==True: # 左邊是 Leaf node 要被砍
                root.left = None # 就砍了它
            if findAndCutLeaves(root.right)==True: # 右邊是 Leaf node 要被砍
                root.right = None # 就砍了它
            return False # 因為不是葉子/沒有提早結束，所以這層不用被砍

        while root.left!=None or root.right!=None: # 只要還有樹葉可以砍
            ans.append([])
            findAndCutLeaves(root)
        ans.append([root.val]) # 最上面的 root 沒辦法在函式裡被砍，所以在最後砍它
        return ans
