# LeetCode 1935. Maximum Number of Words You Can Type
# 鍵盤有些字母壞掉、不能按。在 text 裡，有幾個單字（用空白隔開）「能順利打出來」？
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bad = set(brokenLetters)  # 利用 set() 加速比對
        ans = 0  # 有幾個單字「能順利打出來」？
        for word in text.split():  # 把 text 斷成許多 words
            if set(word) & bad == set():  # 沒有交集、都沒有壞掉
                ans += 1  # 就代表「能順利打出來」
        return ans
        
