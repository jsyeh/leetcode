# 用奇怪的排列方式，把原本的 s 字串，排成 ZigZag 的走法(上到下、斜上，繼續)
# 再橫著重組回答案。
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<=numRows: return s # 全直行，不夠「斜上」，提早結束
        if numRows==1: return s # 沒辦法「斜上」的1列，提早結束 case 7/1157
        rows = [[] for _ in range(numRows)] # 用來存答案，有 numsRows
        loopSize = numRows*2-2 # 一輪是 numsRow＊2-2 個字
        for i,c in enumerate(s): # 逐字處理
            if i%loopSize <  numRows: # 上到下
                rows[i%loopSize].append(c) # 上到下，簡單塞入
            else: # 斜上，要算一下對應的 row 並塞入
                rows[numRows - (i%loopSize-numRows) -2].append(c)
        ans = []
        for row in rows: # 每個橫行
            ans.append(''.join(row)) # 都先接成字串，放入ans
        return ''.join(ans) # ans 再接成1個大字串
# case 7/1157: s = "AB", numRows = 1 在斜上時會出錯
