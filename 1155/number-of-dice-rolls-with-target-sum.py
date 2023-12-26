# n個dice, k面, 希望加總是 target, 有多少種可能, 要 % (10**9+7)
# k面, 代表數字是 1..k
# 可用動態規劃 DP 來解, table[n][sum] 前面 n個dice,加總是 sum 的可能
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        table = [[0]* 1002 for _ in range(n+1)]  # table[n][sum] 的可能性
        table[0][0] = 1 # 0個dice, 加總為0 的可能是1種
        for nn in range(1,n+1): # 如果現在考慮 nn 個 dice
            for now in range(1, target+1): # 想要加總結果是 now 的可能性
                table[nn][now] = 0 # 迴圈前面是0
                for nowFace in range(1,k+1): # 現在dice面向上的值如果是 nowFace
                    table[nn][now] += table[nn-1][now-nowFace] 
                    # 從nn-1個dice的各種結果,逐一加起來
                table[nn][now] %= MOD # 迴圈後面,要取 MOD 避免太大

        return table[n][target] # 題目想問 n 個 dice 要加總成 target 的可能性
