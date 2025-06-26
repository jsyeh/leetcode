# LeetCode 2311. Longest Binary Subsequence Less Than or Equal to K
# 01 組成的 s 字串，取「長度最長」subsequence (可跳著選) 對應的數 <= k
# Hint 建議：刪掉最高位的1，照 Vlad 的解釋，其實就把「全部的0」全部收集，再逐步放1
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = 0  # 收集到的「長度」
        now = 0  # 現在收集的數
        shift = 1  # 「從右到左」收集時，會慢慢增加「位數」使得 1 對應的數變大
        for i in range(len(s)-1, -1, -1):
            if s[i]=='0':  # 全部的0都要收集起來
                ans += 1  # 多了一位
                shift *= 2  # 多了一位，之後的1對應的數會變大
            if s[i]=='1':  # 遇到 1 的話，從右到左、低到高位，逐漸加入 now 中
                if now + shift <= k:
                    now += shift  # 這個1對應的數
                    ans += 1  # 多了一位
                    shift *= 2  # 多了一位，，之後的1對應的數會變大
        return ans
