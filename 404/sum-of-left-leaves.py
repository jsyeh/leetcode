# 找出 tree 裡的「左邊葉子」加起來的值
# 直接用「函式呼叫函式」，就能完成了
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root==None: return 0
        # 如果你已經到「葉子」這層，就無法知道自己「在左or在右」
        # 所以要在前一層做判斷
        if root.left!=None and root.left.left==None and root.left.right==None: 
            # 左邊的root.left 且它沒任何小孩（它的左右都沒有小孩），那便確定它就是左邊的葉子，可拿值
            return root.left.val + self.sumOfLeftLeaves(root.right)
        # 不確定是不是左邊葉子的，都再「函式呼叫函式」下去做，看有沒有機會遇到「左邊的葉子」
        return self.sumOfLeftLeaves(root.left) +self.sumOfLeftLeaves(root.right)
# case 55/100: [0,2,4,1,null,3,-1,5,1,null,6,null,8]
