# LeetCode 1513. Number of Substrings With Only 1s
# 有幾種 substring 裡面都是1。
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9+7  # 答案可能很大，需要「取餘數」
        ans = ones = 0  # 累積的答案、累積的連續1的數量
        for c in s:  # 每個字母「逐一處理」
            if c=='1':  # 遇到'1' 要累積
                ones += 1  # 累積'1'
                ans = (ans + ones) % MOD  # 更新答案
                # ones對應「到目前位置」的各種長度的「只有1」的數量
            else:
                ones = 0
        return ans
