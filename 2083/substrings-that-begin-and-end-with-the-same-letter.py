# 到底「有幾種」可能的substrings, 是以相同的字母「開始、結束」
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        prefixN = defaultdict(int)  # prefixN['a'] 對應「目前為止，有幾個'a'開頭」
        ans = 0
        for c in s:
            ans += prefixN[c] + 1# 加上單1字母的可能
            prefixN[c] += 1
        return ans
