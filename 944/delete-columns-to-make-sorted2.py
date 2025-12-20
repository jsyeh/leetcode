# LeetCode 944. Delete Columns to Make Sorted
# 在字串組成的 100 x 1000 字母陣列裡，有些 col 沒排序好
# 把「col沒排序好」的刪掉，要刪掉幾個？
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        M, N = len(strs), len(strs[0])  # 陣列的長、寬
        ans = 0
        for j in range(N):  # 現在要處理 col j
            for i in range(M-1):  # 要檢查「上下層」
                if strs[i][j] > strs[i+1][j]:  # 沒排序好   
                    ans += 1  # 多1組 col 沒排序好
                    break  # 這個 col j 沒救了，離開迴圈
        return ans
