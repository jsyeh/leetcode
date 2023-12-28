# words 裡, 有多少個 word 的 prefix 與 pref 相同
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        lenP = len(pref)
        for w in words:
            if len(w)<lenP: continue # 長度不夠, 就換下一筆
            if w[:lenP]==pref: ans += 1 # 找到一筆
        return ans
