# LeetCode 364. Nested List Weight Sum II
# 有很多層、不同深度的 list，最大的深度maxd - 深度，當成「權重weight」
# 給你函式 isInteger() add() setInteger() getInteger() getList()，請把 weighted sum 加起來。
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # 先量「深度」
        def depth(nestedList):
            if nestedList == []: return 0
            # if nestedList.isInteger(): return 1
            ans = 0
            for nL in nestedList:
                if nL.isInteger(): ans = max(ans, 0)
                else: ans = max(ans, depth(nL.getList()))
            return ans + 1
        # 再算「加權後的答案」
        def helper(nestedList, weight):
            if nestedList == []: return 0
            ans = 0
            for nL in nestedList:
                if nL.isInteger(): ans += nL.getInteger() * weight
                else: ans += helper(nL.getList(), weight-1)
            return ans
        maxD = depth(nestedList)  # 先量「深度」
        #print(maxD)
        return helper(nestedList, maxD)  # 再算「加權後的答案」
