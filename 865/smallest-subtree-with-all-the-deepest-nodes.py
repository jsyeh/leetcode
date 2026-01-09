# LeetCode 865. Smallest Subtree with all the Deepest Nodes
# 找到最深的 deepest nodes 後，把全部包含的最小的 subtree 找出來
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelCount = []  # 用「陣列」記錄每一層的 nodes 數量
        def findDepth(root, level):  # 用「函式呼叫函式」更新「陣列」
            if root==None: return  # 終止條件，末端空的不計
            if len(levelCount) <= level:  # 若陣列不夠記錄
                levelCount.append(1)  # 新的一層開始，數量是 1
            else: levelCount[level] += 1  # 這一層多1個
            findDepth(root.left, level+1)  # 函式呼叫函式
            findDepth(root.right, level+1)  # 函式呼叫函式
        self.ans = None  # 用來放「最小的subtree」的root位置
        def findSubtree(root, level, deepest):  # 「函式呼叫函式」找 ans
            if root==None: return 0  # 終止條件，末端空的不計
            if level==deepest:  # 剛好是「最深的那層」
                if levelCount[-1]==1: 
                    self.ans = root  # 數量符合1個，剛好是答案
                return 1  # 找到 1 個最深的 node
            left = findSubtree(root.left, level+1, deepest)  # 函式呼叫函式
            right = findSubtree(root.right, level+1, deepest)  # 函式呼叫函式
            if self.ans == None and left+right == levelCount[-1]:  # 數量符合
                self.ans = root  # 數量符合，且還沒記錄，記下第1次符合的最小 subtree
            return left+right  # 層層往上回報
        findDepth(root, 0)  # 函式呼叫函式，更新 levelCount
        findSubtree(root, 0, len(levelCount)-1)  # 函式呼叫函式，找答案（最小subtree）
        return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
