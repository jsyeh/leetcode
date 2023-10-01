class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for w in s.split(): # 外面的迴圈，先把長長的字「斷開」split()
            word = [] # 這裡要用來接字
            for i in range(len(w)-1, -1,-1): # 倒過來的迴圈
                word.append(w[i]) # 每個字母，倒著加入 word 的 list裡
            # print(word)
            x =  "".join(word) # 把分開的字母，用join()接成完整的字
            ans.append(x) # 先用 list 來逐一加入要加的字
        return " ".join(ans) # 以 " " 空格為主，來把分開的字join()接起來
