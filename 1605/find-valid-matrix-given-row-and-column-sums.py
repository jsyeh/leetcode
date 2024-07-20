# LeetCode 1605. Find Valid Matrix Given Row and Column Sums
# 給你「每個row加總結果」及「每個col加總結果」，有點反過來，像填數字謎一樣
# 因數字範圍大（10^8）不能暴力亂試，「數字不為負」讓答案有機會出來。可能不只1組解。
# 沒頭緒，看 Solutions 的 lee215 說 "For each result value at A[i][j],"
# " we greedily take the min(row[i], col[j])." 就照著寫，就解出來了
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        M, N = len(rowSum), len(colSum)  # 找出對應的長度
        ans = [[0]*N for _ in range(M)]  # 照著2D陣列的長度，建出答案的矩陣
        for i in range(M):  # 逐格填寫答案
            for j in range(N):  # 逐格填寫答案
                now = min(rowSum[i], colSum[j])  # 把最小值，全部給ans[i][j]
                ans[i][j] = now  # 填入
                rowSum[i] -= now  # 用掉
                colSum[j] -= now  # 用掉
        return ans
