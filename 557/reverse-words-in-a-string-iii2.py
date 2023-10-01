class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for w in s.split(): # 外面的迴圈，先把長長的字「斷開」split()
            ans.append(w[::-1]) # 利用[::-1]把字串反過來，再加入ans list裡
        return " ".join(ans) # 以 " " 空格為主，來把分開的字join()接起來
