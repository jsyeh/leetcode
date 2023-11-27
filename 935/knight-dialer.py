# 在電話數字鍵上面, 利用騎士的走法, 有幾種走法。看來又是 DP 題。
# 騎士可以在任何地方開始, 走n-1次, 也就是會按出 n 個數字。
# 每個位置,能往下走的地點是固定的, 可以用 array 來決定「能到哪裡」
class Solution:
    def knightDialer(self, n: int) -> int:
        table = [1]*10 # 一開始都有1種可能
        table2 = [0]*10 # 另一個用來交換的表格
        # 下面是個對照表，了解有 fromN[i] 代表「數字i」 可從哪裡過來
        fromN = {0:(4,6), 1:(6,8), 2:(7,9), 3:(4,8), 4:(3,9,0), 5:(), 6:(0,7,1), 7:(6,2), 8:(3,1), 9:(4,2)}

        MOD = 10**9+7
        for s in range(n-1): # 要走 n-1 步
            for i in range(10): # 數字鍵i
                table2[i] = 0
                for k in fromN[i]: # 可以從 k 走過來
                    table2[i] = (table2[i] + table[k]) % MOD
            # 完成後，要交換 table 及 table2
            table, table2 = table2, table
        
        return sum(table) % MOD

