# LeetCode 1717. Maximum Score From Removing Substrings
# 接下來，把 while 迴圈「改成 for 迴圈」，能少掉許多行 j = j + 1 
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s = list(s)
        ans = 0
        N = len(s)
        i, j = 0, 1
        if x > y:
            for j in range(1,N):
                if i>=0 and s[i]+s[j] == 'ab': # 消掉 'ab'
                    ans = ans + x
                    i = i - 1
                else:
                    i = i + 1
                    s[i] = s[j]
            N = i+1
            i, j = 0, 1
            for j in range(1,N):
                if i>=0 and s[i]+s[j] == 'ba':
                    ans = ans + y
                    i = i - 1
                else:
                    i = i + 1
                    s[i] = s[j]
            return ans
        else:
            for j in range(1,N):
                if i>=0 and s[i]+s[j] == 'ba':
                    ans = ans + y
                    i = i - 1
                else:
                    i = i + 1
                    s[i] = s[j]
            N = i+1
            i, j = 0, 1
            for j in range(1,N):
                if i>=0 and s[i]+s[j] == 'ab':
                    ans = ans + x
                    i = i - 1
                else:
                    i = i + 1
                    s[i] = s[j]
            return ans
