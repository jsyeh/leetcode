# LeetCode 1230. Toss Strange Coins
# 有很多銅板，它們正面向上的機率是 prob[i]
# 每個銅板只丟一次，合起來「正面向上」剛好target的機率是多少
# 看起來是 DP 題目，慢慢將使用的 coins 增加，就可算出來了
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        N = len(prob)
        table = [[0]*(N+1) for _ in range(N+1)] # table[i][k] 使用前i個銅板 k個正面的機率
        table[0][0] = 1  # 0個銅板，0個正面的機率 是 1 （大家的基礎） 
        for i in range(1,N+1):  # 現在使用前 i 個銅板（增加使用的那個銅板，對應 prob[i-1]）
            for k in range(i+1):  # 要計算 k 個正面向上的機率，是 k 配 反面 + k-1 配 正面
                table[i][k] = table[i-1][k] * (1-prob[i-1]) + table[i-1][k-1] * prob[i-1]
        return table[N][target] # 題目問，N個銅板 target 個正面

