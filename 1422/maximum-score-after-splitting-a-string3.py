# LeetCode 1422. Maximum Score After Splitting a String
# 字串 s 裡有一堆 0 和 1，把它分「左右」兩半，左半的0 + 右半的1，合起來要最多。
class Solution:
    def maxScore(self, s: str) -> int:
        counter = Counter(s)
        left, right = 0, counter['1']
        ans = 0
        for i in range(len(s)-1):
            if s[i]=='0':
                left+=1
            if s[i]=='1':
                right-=1
            ans = max(ans, left+right)
        return ans

