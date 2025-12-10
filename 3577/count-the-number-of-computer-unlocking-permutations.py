# LeetCode 3577. Count the Number of Computer Unlocking Permutations
# 電腦 i 要解鎖，需要「它左邊的電腦j 且 complexity[j] 更小」
# 問有幾種解鎖順序的方法
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        N = len(complexity)
        # 已先把電腦 0 解鎖，右邊電腦的密碼「會更高」
        for i in range(1,N):
            if complexity[i] <= complexity[0]:
                return 0  # 但反而更低，順序不對
        # 接下來（用乘法）算出答案
        MOD = 10**9 + 7  # 答案越乘越大，要取餘數
        ans = 1  # N-1台電腦，全部可能的解鎖順序「排列組合」是 (N-1)! 
        for i in range(1,N):  # 要算出 (N-1)! 階乘
            ans = (ans * i) % MOD
        return ans
