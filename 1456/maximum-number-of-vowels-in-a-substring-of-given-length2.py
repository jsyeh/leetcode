# LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length
# s 字串裡，找長度 k 的子字串 substring，最多母音有幾個？
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = set('aeiou')  # 母音的 set 方便快速比對
        now = ans = sum([c in v for c in s[:k]])  # 前k項
        for i in range(k, len(s)):  # 往右依序找
            now = now + (s[i] in v) - (s[i-k] in v)  # 加、減
            ans = max(ans, now)  # 更新答案的數量
        return ans
