# 給一堆字母，想知道「能湊出最長的迴文」的長度是多少。
# 其實就看有多少「偶數」兩兩一數的字母，再配1個單數的字母即可
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        odd = False
        ans = 0
        for c in counter:
            ans += counter[c] // 2 * 2  # 看有多少兩兩一數的字
            if counter[c]%2==1:
                odd = True
        if odd: return ans + 1  # 有奇數的話，可再 + 1
        else: return ans  # 沒有偶數，直接就有答案
