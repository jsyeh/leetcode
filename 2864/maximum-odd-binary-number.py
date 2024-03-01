class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        N = len(s) # 總共有幾個字母
        one = 0 # 有 0 個 1
        for c in s:
            if c=='1': one += 1
        return '1'*(one-1)+'0'*(N-one)+'1' # 奇數, 代表最後1位是'1'
        # 前面先有'1', 中間要有'0', 後面再補1個'1'
