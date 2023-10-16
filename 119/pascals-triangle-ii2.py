# 題目Follow up: O(rowIndex) extra space
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]*(rowIndex+1)
        for i in range(2, rowIndex+1):
            for k in range(i-1, 0, -1): # 倒過來的迴圈, 剛好不用壓到下一格需要用的值
                ans[k] = ans[k] + ans[k-1]
        return ans
        '''
        pascal = [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(2,rowIndex+1):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]
        return pascal[rowIndex]
        '''
