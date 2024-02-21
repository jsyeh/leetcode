# 把 n 用 binary 顯示，想問 1 之間的「最大距離」
# 如果沒有相鄰的1，直接 return 0
class Solution:
    def binaryGap(self, n: int) -> int:
        line = bin(n)[2:] # 把 n 轉成2進位 0bXXXX 再把 '0b'去掉
        ans = 0
        zero = -1 # 目前連續幾個0 但擔心8（1000）誤判，初始值-1
        for c in line: # 逐字母分析
            if c=='1':
                ans = max(ans, zero+1) # 距離是 zero+1
                zero = 0 # 又歸零、重來
            else:
                zero += 1
        return ans
