class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a=="0": return b
        if b=="0": return a

        M, N = len(a), len(b)
        i, j = M-1, N-1
        carry = 0
        ans = []
        while i>=0 or j>=0:
            # binary bit of a[i], b[j]
            b1, b2 = 0, 0 # 預設為0， 以免太短時無法算值
            if i>=0 and a[i]=="1": b1 = 1 # 字元轉成數字
            if j>=0 and b[j]=="1": b2 = 1 # 字元轉成數字
            now = b1 + b2 + carry
            ans.append(now%2) # 用來倒著存每一位數的值
            carry = now//2 # 整數除法、進位
            i, j = i-1, j-1 
        if carry==1:
            ans.append(1) # 最高位，多1個進位
        # 最後算出答案
        ans = reversed(ans)
        ansLine = ""
        for bit in ans:
            ansLine += str(bit)
        return ansLine

        
