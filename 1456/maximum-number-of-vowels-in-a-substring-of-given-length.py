# LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length
# s 字串裡，找長度 k 的子字串 substring，最多母音有幾個？
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set('aeiou')  # 利用 set() 快速比對「母音」
        now = 0  # 目前長度為k的「毛毛蟲」子字串，裡面有幾個母音
        for i in range(k):  # 先處理最前面、長度為k的子字串
            if s[i] in vowel: now += 1  # 統計裡面有幾個母音
        ans = now  # 最多的母音數，放在 ans 裡
        for i in range(k,len(s)):  # 後面的子字串
            if s[i] in vowel: now += 1  # 右邊吃字母，是母音嗎？
            if s[i-k] in vowel: now -= 1  # 左邊吐字母，是母音嗎？
            ans = max(ans, now)  # 更新 ans
        return ans
