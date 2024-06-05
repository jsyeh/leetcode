class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        counter = Counter(word)  # 先統計字母出現次數
        ans = 0
        for c in counter:  # 針對counter裡出現過的的小寫字母
            if c.islower() and c.upper() in counter: # 如果大寫也在
                ans += 1  # 就 +1
        return ans
