# LeetCode 696. Count Binary Substrings
# 連續的1、連續的0，要相等數目的各種 substring 小字串，共有幾種？
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prevCombo, combo = 0, 1  # 之前累積數、現在累積數
        for i in range(1, len(s)):  # 與前項（相鄰）兩兩比較
            if s[i-1]==s[i]:  # 相同，就累加
                combo += 1
            else:  # 不相同，就更新答案，並有新的開始
                ans += min(prevCombo, combo)  # 更新答案
                prevCombo, combo = combo, 1  # 新的開始
        ans += min(prevCombo, combo)  # 更新答案（最後一次）
        return ans
