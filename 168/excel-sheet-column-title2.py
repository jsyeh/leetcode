class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        N = columnNumber
        # 有一種作法，是製作一個超大的表格table，會對應字母
        # table = {1:"A", 2:"B", 3:"C", 4:"D", }
        # 另外，字串其實也能簡單使用。就用字串吧（Z要小心)
        s = "ZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""
        while N > 0:
            ans = s[N%26] + ans
            if N%26==0: N -= 26 # 遇到餘0時，其實是26的Z
            # 這時候要把數字扣掉26才不會殘留值
            N //= 26 # 剝皮法

        return ans
