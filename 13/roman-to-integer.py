class Solution:
    def romanToInt(self, s: str) -> int:
        v = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        prev = 1000 # 為解決倒過來的問題，利用 prev 來記錄最後的值
        # 因為是由大到小，所以先放最大，第一筆就一定不會有逆轉
        ans = 0
        for c in s:
            if v[c] > prev: # 逆轉發生時，要倒扣回來
                ans = ans + v[c] - prev - prev # 還原，再倒扣
            else:
                ans = ans + v[c]
                prev = v[c]
        return ans
            
