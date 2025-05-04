# LeetCode 1128. Number of Equivalent Domino Pairs
# 骨牌 dominoes[i] 裡有兩個值 [a,b]，另一個骨牌 dominoes[j]
# 若裡面有 [a,b] 或 [b,a] 那可以說兩個骨牌相同。數一數「有幾對」相同
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 先把骨牌「轉向」成「先小、再大」，再數一下，各組的數量
        table = [0] * 100  # 利用陣列，統計「各種骨牌的數量」
        for (a,b) in dominoes:
            if a<b: table[a*10+b] += 1  # 小的放前面中，大的放後面
            else: table[b*10+a] += 1  # 小的放前面，大的放後面
        # 接下來，利用「排列組合」，每組「挑2個」的可能挑法「加起來」
        ans = 0
        for v in table:  # 針對 table 裡，大於1個的骨牌，做「排列組合」
            if v>1: ans += v * (v-1) // 2  # C(v,2) C(v 取 2)對應的公式
        return ans
