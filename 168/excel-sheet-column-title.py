# 在 Excel 裡面，上方的 A, B, C ... AA, AB, ... 對應數字
# 現在給個數字，要算出英文字。就26進位為基礎即可算出來
# 0-index vs. 1-index 不同。我熟0-index但這題是1-index
# 把數字-1 可以將 A...Y 都正確處理，但Z比較麻煩，所以另外處理。
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        N = columnNumber # N比較短，程式碼較易理解
        
        ans = ""
        while True:
            if N%26==0: # 處理 Z 的部分
                ans = "Z" + ans # 高位數在左邊、低位數在右邊
                N -= 26 # 因為 Z 對應 26, 所以要另外扣掉它
            else: # 處理剩下 A...Y 的部分
                ans = chr(N % 26 + ord("A") -1) + ans # 高位數在左邊
                # chr() 把ASCII值變成字元。 ord()把字元變成ASCII值
            N //= 26 # 因為 26個字母，以26為循環
            if N==0: break
        return ans
