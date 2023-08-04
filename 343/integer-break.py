# 要把數字拆成任意2個數字，再看哪一組乘起來比較大
class Solution:
    def integerBreak(self, n: int) -> int:
        table = [0]*(n+1) # table[i] 表示 integerBreak(i) 的結果
        table[0] = 1 # 題目雖然不會有0，但乘法時要準備1讓它乘
        table[1] = 1 # 題目不會有1
        table[2] = 1 # 就是 1*1

        for i in range(3, n+1): # 想知道 table[i] 的值，從小到大去算
            table[i] = 1 * table[i-1] # 最簡單的拆法，是 1 * integerBreak(i-1)
            for k in range(1, i): # k 是 1, 2 ... i-1
                # 其實這個迴圈可以跑少一點，因為左右會對稱。不過 i/2 改 int(i/2) 不好看
                part1 = max(k, table[k])
                part2 = max(i-k, table[i-k])
                now = part1 * part2
                if now > table[i]: # 如果這種拆法，乘起來更大的話，就更新 table[i]
                    table[i] = now

        return table[n]
# case 47/50: 3 要小心 k 迴圈的範圍哦
# case 49/50: 4 要把數字拆兩邊後 max(k,table[k]) * max(i-k, table[i-k])
