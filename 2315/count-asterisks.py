# LeetCode 2315. Count Asterisks
# 數一下有幾個星星*，但是夾在「兩兩一組」的 | | 裡面不算
class Solution:
    def countAsterisks(self, s: str) -> int:
        words = s.split('|')
        ans = 0
        for i,word in enumerate(words):
            if i%2==0: ans += Counter(word)['*']
        return ans
