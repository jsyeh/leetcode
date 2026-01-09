# LeetCode 392. Is Subsequence
# 找一下 s 是否為 t 的 subsequence，也就是「照順序出現」（可跳過一些）
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # s[i] vs. t[j]
        for c in t:  # 逐一比對，看 s[i] 是否相同
            if i<len(s) and s[i]==c:  # 還沒走完，巧遇到符合的
                i += 1  # 就再走一步
        return i==len(s)  # 是否走到最後面
