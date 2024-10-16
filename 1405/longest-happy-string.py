# LeetCode 1405. Longest Happy String
# 必須由 a,b,c 三種字母組成、不能重覆3個相同字母(要適時交錯)
# 給你 a,b,c 的數量, 讓你使用, 能組出的最長字串。直覺作法：優先處理數量多的字母, 要把它交錯出來, 塞字母進去
# 這裡使用 votrubac 的「函式呼叫函式」解法，增加3個預設參數，讓程式碼可任意調整參數的意思
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int, aa='a', bb='b', cc='c') -> str:
        # 調整順序的終止條件：正常是 a>=b>=c 但不合理時
        if b>a: return self.longestDiverseString(b, a, c, bb, aa, cc) # b更大時，改放b在前面，就調順序
        if c>b: return self.longestDiverseString(a, c, b, aa, cc, bb) # a還是最大，但c卻在中間，就調順序
        if b==0: return aa*min(a,2)  # 如果「二當家」沒了，就要結束了，就最多2個aa 或1個a 或什麼都沒了，結尾

        # 走到這裡，代表 a>=b>=c 也就是要優先把 aa 接 bb 再接 剩下的函式呼叫函式的部分
        useA = min(2,a)  # 這輪能放幾個 'a' 也就是 字串aa*數量useA 
        if a-useA >= b: useB = 1  # 這輪能放幾個 'b' 也就是 字串bb*數量useB
        else: useB = 0  # 如果剩下的 'a' 數量比 'b' 還少，那下一輪 b 會被抬到前面，所以不能放 'b'
        return aa*useA + bb*useB + self.longestDiverseString(a-useA, b-useB, c, aa, bb, cc)
