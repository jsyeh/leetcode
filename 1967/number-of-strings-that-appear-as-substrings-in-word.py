# LeetCode 1967. Number of Strings That Appear as Substrings in Word
# 問 pattern 裡，有幾個是 word 的子字串
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for p in patterns:
            if p in word:
                ans += 1
        return ans
        
