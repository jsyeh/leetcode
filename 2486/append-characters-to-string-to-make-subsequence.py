# LeetCode 2486. Append Characters to String to Make Subsequence
# 要將幾個字母加到 s 的後面，可讓 t 成為它的 substring ?
# 可先在 s 裡，逐字母找看看 t 的 prefix 能收齊幾個字母
# 沒有收集到的字母有幾個，就是答案。
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # s[i] vs. t[j]
        j = 0
        for c in s:  # 想像 c 就是 s[i]
            if c == t[j]:  # 又找到1個符合的字母
                j += 1
                if j==len(t): return 0  # 提早收齊全部字母
        return len(t) - j  # 收集到j個字母，全長len(t)
        # 所以相減，就是「還缺幾個字母」
