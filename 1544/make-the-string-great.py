# 字串裡有大小寫的字母。相鄰字母如果是同一字母，且大小寫不同，就可以消掉
# 一直消、一直消，直到不能消為止。回傳字串。
class Solution:
    def makeGood(self, s: str) -> str:
        a = [] # 一開始是空的
        for c in s: # 把 s 裡，每個字母，逐個處理
            a.append(c) # 先加到 a 的後面
            # 下面判斷：如果 a 裡有2個以上的字母，且這兩個剛好在 ASCII表裡距離32，也就是剛好是同字母的大小寫
            if len(a)>=2 and abs(ord(a[-1])-ord(a[-2]))==32:
                a.pop() # 就最後2個字母一起消掉
                a.pop()
        return ''.join(a) # 最後的答案，就是把字母「串成」字串
