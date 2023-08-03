# coins 慢慢增加
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        N = len(prob)
        table = [[0.0]*(N+1) for _ in range(N+1)]
        # table[f][i] 表示使用 i 個 coins, f 個人頭向上的機率

        table[0][0] = 1 # 0 個coin, 0個人頭向上的機率
        for i in range(1,N+1):
            table[0][i] = table[0][i-1] * (1-prob[i-1]) # 0個人頭向上
        for f in range(1,N+1):
            table[f][0] = 0 # 沒有丟 coins 就不會有 face向上
        
        for i in range(1,N+1):
            for f in range(1,N+1):
                table[f][i] = table[f-1][i-1] * prob[i-1] + table[f][i-1] * (1-prob[i-1])
        return table[target][N]
# case 22/28: [1,1,1,1,1,1,1,1,1,1] 有 10 個硬幣都要丟，機率都是頭向上
# 9 但怎麼可能得到 9 個頭向上呢？只會有10個頭向 上
