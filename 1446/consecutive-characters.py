# LeetCode 1446. Consecutive Characters
# 字串 s 裡，相同字母連續最長的長度
class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        prevC, prevN = s[0], 1  # 前一個字母是誰？已連續幾個相同字母？
        for i in range(1,len(s)):
            if s[i] == prevC:  # 持續相同
                prevN += 1  # 就加長
                ans = max(ans, prevN)
            else:  # 不相同
                prevC, prevN = s[i], 1  # 就新的開始
        return ans
