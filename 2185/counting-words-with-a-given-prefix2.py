# LeetCode 2185. Counting Words With a Given Prefix
# 給字串 pref，在 words 裡，找有幾個字串的字首與 pref 相同
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        L = len(pref)  # 字串的長度
        for word in words:  # 每個字都去測
            if pref == word[:L]:  # 如果符合
                ans += 1  # 就又找到1個字了！
        return ans
