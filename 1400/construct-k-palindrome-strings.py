# LeetCode 1400. Construct K Palindrome Strings
# 能用字串 s 的字母，調整順序後，切成 k 個 palindrome 迴文嗎？
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False  # Hint 1: 如果長度不夠，就一定失敗

        # 每個迴文，最多只能有1個奇數。所以要數一下有幾個「奇數」
        freq = Counter(s)  # 先統計「字母出現次數」
        odd = 0
        for f in freq.values():# 只看字母的「出現次數」
            if f%2==1: odd += 1
        if odd > k: return False  # 奇數太多，就沒辦法湊出迴文，失敗
        return True  # 一定可以湊出來
