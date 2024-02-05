# 有問號的地方，對應有幾個可能的答案
# 因為總共只有 24*60 種可能，所以暴力試即可
# 不過因為速度排名有點後面，我決定重寫另一個版本
# 把幾種'?'的排列組合乘起來。mm分 比較簡單，最多*=60
# hh時 比較麻煩，就看'?'在哪一位，再把 2[0123] 及[01]?都考量過即可
class Solution:
    def countTime(self, time: str) -> int:
        hh, mm = time.split(':')
        ans = 1
        if mm[0]=='?': ans *= 6
        if mm[1]=='?': ans *= 10

        if hh[0]=='0' and hh[1]=='?': ans *=10
        if hh[0]=='1' and hh[1]=='?': ans *=10
        if hh[0]=='2' and hh[1]=='?': ans *= 4
        if hh[0]=='?' and hh[1]=='?': ans *= 24
        if hh[0]=='?' and '0'<=hh[1]<='3': ans *= 3
        if hh[0]=='?' and '4'<=hh[1]<='9': ans *= 2

        return ans
