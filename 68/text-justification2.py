# 1234567890123456 maxWidth:16
# This    is    an 
# example  of text 
# justification.

# 1234567890123456 maxWidth:16
# What   must   be 
# acknowledgement 
# shall be

# 12345678901234567890 maxWidth:20
# Science  is  what we 
# understand      well 
# enough to explain to 
# a  cmoputer.  Art is 
# everything  else  we 
# do
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = [] 
        line = [] # 用來存很多字
        total = -1 # 因為第1個字的前面不用加空格，所以預先用-1以便對消
        for w in words:
            total += len(w) + 1 # 每個字的前面有多「1個」空格
            if total > maxWidth: # 字如果超過最大長度的話
                total = len(w) # 清為0後，裡面放新的字的長度
                lines.append(line) # 在 line = [] 之前，把line備份lines
                line = []
            line.append(w) # line裡面加入 w 這個字

        ans = [] # 後面準備組字囉
        # 接下來，把字和空白「組起來」
        for ww in lines: # ww 是某一行裡的一堆字
            wordN = len(ww) # 這行有幾個大字，那麼 (wordN-1)就是間隔
            if wordN == 1: # 遇到剛好只有1個超長字時
                # 最後塞入 ans 裡
                ans.append(ww[0] + " "*(maxWidth-len(ww[0]))) ## 小心
                # 只有一個字：前面放ww[0]，後面放一堆空白，以湊齊 maxWidth
                continue # 回到for迴圈的前面，執行下一筆（不要跑下面程式）
            
            # 下面是算空白的神奇寫法 加總(每個字的長度用for迴圈湊起來)
            spaces = maxWidth - sum(len(w) for w in ww)
            space1 = spaces//(wordN-1) # 基本的空格數目
            space2 = spaces%(wordN-1) # 剩下的空格數目，讓前面每格都+1
            ansLine = ww[0]
            for i in range(1,space2+1):
                ansLine += " "*(space1+1) + ww[i]
                # 剩下的空格數目，讓前面每格都+1
            for i in range(space2+1, len(ww)):
                ansLine += " "*(space1+0) + ww[i]
                # 基本的空格數目 space1
            ans.append(ansLine) # 最後塞入 ans 裡
        
        # 最後一行的處理
        ansLine = line[0] # 先把沒有空格的第1個字放進去
        for i in range(1, len(line)): # 後面接著放
            ansLine += " " + line[i] # 每個字的前面都要補空格哦
        ansLine += " "*(maxWidth-len(ansLine)) # 也是補齊最後面的空格
        ans.append(ansLine) # 最後塞入 ans 裡

        return ans

