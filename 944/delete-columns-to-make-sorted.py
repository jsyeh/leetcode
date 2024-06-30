# 看有幾個 col 是沒有排序好的
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        M, N = len(strs), len(strs[0])
        ans = 0
        for j in range(N): # 每個 col 逐個檢查
            for i in range(M-1): # 很像泡泡排序法，相鄰去比較
                if ord(strs[i][j]) > ord(strs[i+1][j]):
                    ans += 1
                    break # 離開這層i
        return ans

