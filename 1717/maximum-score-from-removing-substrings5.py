# LeetCode 1717. Maximum Score From Removing Substrings
# 原本程式有 4 段，重覆的部分「變成函式」，就可以簡化成2段哦！
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s = list(s)
        def doAB(s):  # 進行 'ab' 的化簡
            i, j = 0, 1
            ans = 0
            for j in range(1,len(s)):
                if i>=0 and s[i]+s[j] == 'ab': # 消掉 'ab'
                    ans = ans + x
                    i = i - 1
                else:
                    i = i + 1
                    s[i] = s[j]
            del s[i+1:]  # 消掉後，只有 s[0]..s[i] 有效，刪後面
            return ans
        def doBA(s):  # 進行 'ba' 的化簡
            i, j = 0, 1
            ans = 0
            for j in range(1,len(s)):
                if i>=0 and s[i]+s[j] == 'ba':
                    ans = ans + y
                    i = i - 1
                else:
                    i = i + 1
                    s[i] = s[j]
            del s[i+1:]
            return ans
        if x > y:  # 若 'ab' 比較貴，就「先處理 'ab'」
            return doAB(s) + doBA(s)
        else:
            return doBA(s) + doAB(s)  # 反過來「先處理'ba'」
