class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            row = [1]*(i+1) # 先放一堆1,這樣頭尾的1就準備好了
            ans.append(row)
            for j in range(1,i): # 把中間的數字補起來
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans
