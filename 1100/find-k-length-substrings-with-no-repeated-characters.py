# LeetCode 1100. Find K-Length Substrings With No Repeated Characters
# 有幾個長度為 k 的 substring，裡面「相鄰」的字母「都不相同」，用毛毛蟲
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k>26: return 0  # 怎麼可能有 27 以上的字母？一定失敗
        counter = Counter(s[:k])  # 利用 Counter 統計「字母出現狀況」
        ans = 0
        diff = len(counter)  # 前 k 個字裡，有 diff 個「不同」的字母
        if diff==k:  # 若剛好 有 k 個不同的字母， ans += 1
            ans += 1

        for i in range(len(s)-k):  # 接下來「毛毛蟲」往右爬
            counter[s[i+k]] += 1  # 右邊吃1個字母
            if counter[s[i+k]] == 1: diff += 1
            counter[s[i]] -= 1  # 左邊吐1個字
            if counter[s[i]] == 0: diff -= 1
            if diff==k:  # 若剛好 有 k 個不同的字母， ans += 1
                ans += 1
        return ans
