# return 連續1 > 連續0
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        oneMax = zeroMax = 0
        oneNow = zeroNow = 0
        for c in s:
            if c=='1':
                oneNow += 1 # 加一
                zeroNow = 0 # 歸零
                oneMax = max(oneMax, oneNow)
            else: # 現在是 '0'
                zeroNow += 1
                oneNow = 0
                zeroMax = max(zeroMax, zeroNow)
        return oneMax > zeroMax
