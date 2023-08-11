class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        combN = [0]*(amount+1)
        # combN[i] 表示合計i元，有多少種組合
        combN[0] = 1 # 完全不用任何coin的這種方法，就可得到0元
        for c in coins:
            for i in range(c, amount+1):
                combN[i] += combN[i-c] # 增加可能的組合
        
        return combN[amount]
        
