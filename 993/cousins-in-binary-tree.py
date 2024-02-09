# 想知道 x, y 對應的 node，是否是同一層，且「不同parent」
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def helper(root, x, path)->int: # 找「到達x」的整個路徑
            ans = 0
            if root==None:
                return 0
            if root.val==x: 
                ans += 1
            ans += helper(root.left, x, path)
            ans += helper(root.right, x, path)
            if ans>0: path.append(root.val)
            return ans
        pathX = [] # 用來存 root..x 的路徑
        pathY = [] # 用來存 root..y 的路徑
        helper(root, x, pathX)
        helper(root, y, pathY)
        print(pathX)
        print(pathY)
        if len(pathX)!=len(pathY) or len(pathX)<=2: return False
        if pathX[1]!=pathY[1]: return True
        else: return False
# case 97/105: [1,2,4,3,19,10,5,15,8,null,null,13,14,null,6,null,17,null,null,null,null,18,null,7,11,null,null,null,null,null,9,16,12,null,null,20] 11 17
