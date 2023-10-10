# 數字倒過來時，還是可以看的數字，且值會不同（會看錯）
# 0,1,6,8,9 有潛力 confusing
class Solution:
    def confusingNumber(self, n: int) -> bool:
        # 先確認數字「不能倒著看」就先Fase
        table = {0:0, 1:1, 6:9, 8:8, 9:6} # 對照表
        n0, n2 = n, 0 # 將 n 備份成原數字 n0, n2 將放倒轉後的數字
        while n>0:
            n2 *= 10
            if n%10 in table:
                n2 += table[n%10] # 轉換成上下倒像的數字
                n //= 10
            else: # 中間發現不對，就提早False結束
                return False
        if n0 == n2: # 相同的話，無法構成 confusing number 
            return False
        else:
            return True # 是 confusing number

