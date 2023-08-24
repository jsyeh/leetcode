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
        N = len(words)

        # 先照著 maxWidth 來斷句。
        lines = [] # 每一行的字
        line = [] # 最後一行的字
        count = -1 # 斷行用的累積字母數（因第1個字不加空格，用-1補償）
        # 最後一行不會用到字母數
        for i in range(N):
            after = count + len(words[i]) + 1 # 加完新字後的長度
            if after == maxWidth: # 字剛好切齊（若加新字後的長度剛剛好）
                line.append(words[i]) # 剛好可以加上這個字
                lines.append(line) # 把這行加入成果中
                line = [] # 要準備新的一行
                count = -1 # 清空，下次重來（因第1個字不加空格，用-1補償）
            elif after < maxWidth: # 若加新字後的長度沒超過
                line.append(words[i])
                count += len(words[i]) # 長度可更新
                count += 1 # 空格加到後面，沒超過的話就可以
            else: # 若字會超過，先別加這行字。斷行。新的一行
                lines.append(line) # 把舊的line 加入 lines 裡
                line = [ words[i] ]# 新的一行的第1個字
                count = len(words[i]) # 長度就是你的長度
        # if lines == []: # 若最後一行是空的，要把lines最後一行移到line裡
        #     line = lines.pop()
        print(lines) # 前面要左右切齊的行
        print(line) # 最後一行（不要左右切齊）

        # 接下來開始組句
        ans = [] 
        for i in range(len(lines)): # 前面各行，是「左右對齊」
            wordN = len(lines[i]) # 這行有幾個字。wordN-1則是空格間隔
            if wordN == 1: # 如果只有1個字的話，後面全部補空格
                spaces = maxWidth - len(lines[i][0]) # 後面補空格
                ans.append(lines[i][0] + " "*spaces)
                continue
            charLen = sum(len(w) for w in lines[i])
            spaces = maxWidth - charLen
            # spaces = maxWidth - charLen[i] # 這行的全部空格
            space1 = spaces % (wordN-1) # 前面 space1 個空間，各要多1個空格
            space2 = spaces // (wordN-1) # 每個空間的基礎是 space2 個空格
            # print(wordN, charLen, space1, space2)

            ansLine = lines[i][0] # 第一個字，前面不加空格
            for k in range(1,space1+1): # 第2個字之後，前面都加個空格, 左群再多空格
                ansLine += " "*(space2+1) + lines[i][k]
                # print(ansLine)

            for k in range(space1+1, wordN): # 右群正常空格
                ansLine += " "*space2 + lines[i][k]
                # print(ansLine)

            ans.append(ansLine)
        # 處理最後一行，是「左邊對齊」
        if line==[]: return ans # 最後一行沒東西，就不要跳行

        ansLine = ""
        for w in line: # 最後一行的處理
            if ansLine == "": # 第1個字，前面不加空格
                ansLine += w
            else: # 第2個字之後，前面都加個空格
                ansLine += " " + w
        ansLine += " "*(maxWidth-len(ansLine)) # 補最後的空白
        ans.append(ansLine)
        return ans
# case 5/27: ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
# 16 最後一行切齊
