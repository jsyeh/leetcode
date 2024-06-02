# 題目是想要把字串反過來。但題目要求「不准」另外 return 答案。
# 要把 list 裡的字母，逐一反過來。因此，可善用「字母」交換的作法。
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        不可以 return s[::-1] 因題目要求「不能另外return」
        """
        N = len(s)  # 有list的長度，能找到 s[i] 的對手 s[N-1-i]
        for i in range(N//2):  # 迴圈要做一半，讓前半、後半交換
            s[i], s[N-1-i] = s[N-1-i], s[i]
            # 這是 Python 的語法，讓兩數交換
