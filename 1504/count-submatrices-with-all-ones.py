# LeetCode 1504. Count Submatrices With All Ones
# 數一數，有幾個 submatrix 方型的小矩陣，裡面都是1
# 題目 Hints 可使用 3 層迴圈 O(n^3) 的作法，依序累積更新答案
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        ans = 0
        # Hint 1 建議用 nums[j] = nums[j-1]+1 （其實需要用 2D 陣列）
        nums = [[0]*N for i in range(M)]  # 對應「連續」的1的數量
        for i in range(M):  # 第1層迴圈：針對每個 row i 進行分析
            for j in range(N):  # 第2層迴圈：累積 row i 到 i,j 的連續1
                if mat[i][j]==0: nums[i][j] = 0  # 不是1無法連續，歸零
                else: nums[i][j] = nums[i][j-1] + 1  # 持續combo連續
                # Hint 2: sum(min(nums[j,...idx])) 最小值決定(它寫得不好)
                now = nums[i][j]  # 現在 row i 累積到 mat[i][j]的長度
                # 目前已分析過的 row 0...i
                for k in range(i,-1,-1):  # 第3層迴圈：從row i 往上到 row k
                    now = min(now, nums[k][j])  # 往上到 row k 的最小值
                    ans += now  # 對應 now 個長方形，都是合法的答案
        return ans
