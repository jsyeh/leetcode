# LeetCode 790. Domino and Tromino Tiling
# 有兩種形狀的骨牌，傳統 1x2 及 L型 的骨牌，問 2xn 有幾種可能排法
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9+7
        table = [1, 1, 2, 5] + [0] * n
        for i in range(4, n+1):
            # 第1種 1x2，可以直放，可以橫放
            table[i] = (table[i-1] + table[i-2]) % MOD
            # 也可以用 L型的方法放（有兩種L型）
            # 第2種 對應「收尾的L型」
            for k in range(3, i+1, 2):  # 中間會放「橫的1x2」
                table[i] = (table[i] + table[i-k]*2) % MOD  # 上下鏡射, 有兩種
            # 第3種 對應「長邊對接的L型」
            for k in range(4, i+1, 2):  # 中間會放「橫的1x2」
                table[i] = (table[i] + table[i-k]*2) % MOD  # 上下鏡射, 有兩種
        return table[n]
