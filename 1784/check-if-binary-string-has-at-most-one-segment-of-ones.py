# 「最多只能有1堆」的 ones 所以若有第2堆ones的話，就False
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        nowOne = 0
        contOne = 0
        for c in s:
            if c=='1':
                nowOne += 1
                if nowOne==1: # 剛開始連續
                    contOne += 1 # 只計算這次哦！
                    if contOne > 1: return False
            else: # 現在不是 '1'
                nowOne = 0 # 歸0
        return contOne == 1
# case 129/181: "1" # 只能有1堆1，沒錯哦！
