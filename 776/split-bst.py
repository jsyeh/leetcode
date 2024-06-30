# LeetCode 776. Split BST
# 給個 target 值，把 BST 分成左邊(含)、右邊 兩個 sub-BST Binary Search Tree
# 如果把 BST 先變成 array 再處理，好像也行。不行，因tree的結構需要儘量保持。
# 所以要邊做邊
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if root==None: return [None, None] # 終止條件

        if root.val==target: # 要將root歸在左邊
            right = root.right # 裁切到右邊的return值
            root.right = None # root是左邊的return值，但要記得把它的右邊裁掉
            return [root, right]
        elif root.val<target: # 還在左邊的區塊。答案要切在右半樹
            left, right = self.splitBST(root.right, target) # 右半樹再切
            root.right = left # 右半樹的左半，要接在左邊（也就是root左邊的右邊要接它）
            return [root, right]
        else: # 答案要切在左半樹
            left, right = self.splitBST(root.left, target) # 左半樹再切
            root.left = right  # root在右邊，它的左邊會拉「左半樹的右邊」
            return [left, root]

        '''
        # 以下方法，粗暴轉成array再轉回BST，不幸動到結構，但題目希望「保持結構」
        array = []
        def helper(root):
            if root==None: return
            helper(root.left)
            array.append(root.val)
            helper(root.right)
        helper(root)
        def buildBST(i, j): # 左右都包含
            if i>j: return None  # 逆反，無法建tree
            if i==j: return TreeNode(array[i]) # 夾擊1點，建它
            mid = (i+j) // 2
            print(i,mid-1, mid, mid+1, j)
            return TreeNode(array[mid], buildBST(i,mid-1), buildBST(mid+1,j))

        for i,now in enumerate(array):
            if now > target:
                return [buildBST(0,i-1), buildBST(i, len(array)-1)]
        
        return [root, None]
        '''
