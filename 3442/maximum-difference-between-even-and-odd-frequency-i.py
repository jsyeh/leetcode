# LeetCode 3442. Maximum Difference Between Even and Odd Frequency I
# 字串 s 每個字母的出現次數，想找出freq(奇數次數)最大 - freq(偶數次數)最小
class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)  # 統計每個字母的出現次數
        odd, even = [], []  # 分別裝「奇數次數」及「偶數次數」
        for c in counter:  # 逐字母分析
            if counter[c]%2==1: odd.append(counter[c])  # 奇數次數
            else: even.append(counter[c])  # 偶數次數
        return max(odd) - min(even)  # 奇數次數最大 - 偶數次數最小
