# Gray Code 是「相鄰數字」只差1bit 的表示法
# ex. 0 1 3 2
# ex. 0 1 3 2 6 7 5 4
# 其實就是把 gray(n-1) 的結果反過來，最前面 bit 再加 1 即可
class Solution:
    @cache
    def grayCode(self, n: int) -> List[int]:
        if n==1: return [0, 1]
        now = self.grayCode(n-1)
        topbit = 2**(n-1) # 最高位數的 bit 變成 1
        for i in range(len(now)-1, -1, -1): # 反過來
            now.append(now[i]+topbit) # 倒著加進來
        return now
