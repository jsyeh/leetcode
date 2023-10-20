# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# 這題的任務有點難懂。它先準備好了 NestedInteger 的 3個功能：
# nestedList.isInteger()
# nestedList.getInteger()
# nestedList.getList()
# 要用這3個功能，做出「函式呼叫函式」的 helper() 把每個整數都append()到答案裡
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ans = []
        def helper(nestedList):
            for one in nestedList:
                if one.isInteger():
                    self.ans.append(one.getInteger())
                else:
                    helper(one.getList()) # 把 list 再丟到 helper()裡處理

        helper(nestedList)
        self.i = 0
    
    def next(self) -> int:
        ans = self.ans[self.i]
        self.i += 1
        return ans
    
    def hasNext(self) -> bool:
        if self.i < len(self.ans):
            return True
        else:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
