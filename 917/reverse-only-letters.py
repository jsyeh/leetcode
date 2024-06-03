# 只有「連續的字母」要反過來，其他符號照舊
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        word = []
        for c in s:  # 第一輪：先把全部字母 append 起來
            if c.isalpha():
                word.append(c)  # 像 Stack 一樣push進word

        ans = []
        for c in s:  # 再做一次迴圈，建出答案
            if c.isalpha():  # 如果這格是字母，就放收集的字母
                ans.append(word.pop()) # word倒著將字母吐出來
            else:  # 如果是其他符號，就照舊放入答案
                ans.append(c)

        return ''.join(ans)
