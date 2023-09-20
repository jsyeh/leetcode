# 要把 x 減為 0 的最小步驟, 其實等價於, 陣列最左邊、最右邊加起來的sum, 要最少的elements數
# 我就先建好 runSum[i] 及 runSum2[j] 兩個, 對應 "左端挑i個" + "右端挑j個"
# 最後再把最小的 i+j 值找出來。
# 有個陷阱, 像 [1,1,1,1,1] 要組出 8 不可能, 但誤得到 3+5=8, 所以 i+j > N 就是錯的(不能用)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        runSum, runSum2 = [0]*(N+1), [0]*(N+1) # 製作 running Sum
        for i in range(1,N+1):
            runSum[i] = runSum[i-1] + nums[i-1] # runSum[i] 代表 左邊挑i個的和
            runSum2[i] = runSum2[i-1] + nums[N-i] # runSum2[j] 代表 右邊挑j個的和
        # print(runSum)
        # print(runSum2)
        # 接下來試著巡看看,任何可能的組合
        ans = 2*N
        j = N # runSum[i] + runSum2[j], j從小到大巡過去, j從大到小巡回來
        for i in range(N+1):
            while runSum[i]+runSum2[j] > x and j>=1: # 太大的話, j要變小
                j -= 1 # j還能變小
            if runSum[i] + runSum2[j] == x:
                if i+j<ans: # 如果使用的數字更少
                    ans = i+j # 更新
        if ans==2*N or ans >N: # 不合理的狀況
            return -1
        else:
            return ans
# case 89/94: [5,2,3,1,1] 答案只要左邊5, 所以我的 runSum2[j] 要走到 j=0的那格
