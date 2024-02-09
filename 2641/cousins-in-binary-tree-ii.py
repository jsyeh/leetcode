# 每個node的值，改存「堂兄弟」的和（堂兄弟，表示「父node不同」但在同一層。
# 把問題改成：先算「同一層」的全部sum，再由father來決定children的值，即
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        allLevelSum = defaultdict(int)
        def findAllLevelSum(root, level):
            if root==None: return
            allLevelSum[level] += root.val
            findAllLevelSum(root.left, level+1)
            findAllLevelSum(root.right, level+1)
        def findCousinsSum(root, level) -> int:
            if root==None: return 0
            v1 = findCousinsSum(root.left, level+1) # 處理完 left child 後，得到child 值
            v2 = findCousinsSum(root.right, level+1) # 處理完 left child 後，得到child 值
            # 有了 v1, v2，便可以更新它們的值
            if root.left!=None: root.left.val = allLevelSum[level+1] - v1 - v2
            if root.right!=None: root.right.val = allLevelSum[level+1] - v1 - v2
            return root.val # 把自己的值，交給上一層來處理
            
        findAllLevelSum(root, 0) # 先全部都算一次
        root.val = 0 # root一定是0，因為它沒有堂兄弟
        findCousinsSum(root, 0) # 再扣除 brother的值，填回root中
        return root
