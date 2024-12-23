# LeetCode 2471. Minimum Number of Operations to Sort a Binary Tree by Level
# 每次可在「同一層」挑2個 node 交換 val值。要交換幾次，才能「每一層」都排序好？
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levelArray = []  # 大陣列。第 level 層裡的值，都放入大陣列 levelArray 裡面的小陣列 levelArray[level]
        def buildLevelArray(root, level):  # 使用「函式呼叫函式」準備「各層」的陣列
            if root==None: return  # 走到末梢就結束
            if len(levelArray) <= level: levelArray.append([]) # 小陣列不夠時，就再加1層
            levelArray[level].append([root.val, len(levelArray[level])])  # 第level層的小陣列裡，放入(值,index)
            buildLevelArray(root.left, level+1)  # 函式呼叫函式
            buildLevelArray(root.right, level+1)  # 函式呼叫函式
        buildLevelArray(root, 0)  # 利用「函式呼叫函式」，先把 levelArray 裡，每一層的值都建好
        ans = 0  # 統計要交換幾次
        for array in levelArray:  # 針對每一層的小陣列
            array.sort()  # 先「照值」排序好
            ids = [ arrayIndex[1] for arrayIndex in array] # 取出舊 index 在「排序後」的新位置
            for i in range(len(ids)):  # 每一格，若要「還原」成「排序前」的位置，需要「交換」幾次呢？
                while ids[i] != i:  # Cyclic Sort 的技巧，裡面都是 0...N-1 的 index 時，直接放到該放的位置
                    i2 = ids[i]  # 最後的「目的地」（題目要問「交換幾次」，所以與目的地的 index做交換）
                    ids[i], ids[i2] = ids[i2], ids[i]  # 每次將「出發點」與「目的地」的值對調，便能將「1個index」放正確
                    ans += 1  # 用 while 迴圈持續做，直到「這一循環」做完
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
