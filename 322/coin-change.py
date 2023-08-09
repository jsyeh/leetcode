class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [-1]*(amount+1) # table[i] 達到i元, 答案是 table[amount]
        table[0] = 0 # 0個銅板，便能達到0元
        coins = sorted(coins) # 希望從小到大的順序來做
        for k in range(len(coins)):
            c = coins[k]
            for i in range(amount+1):
                if i>=c and table[i-c]!=-1: # 能更新，且前面有值，
                    if table[i]==-1 or table[i-c]+1<table[i]: 
                        # 還沒有任何值 or 有更好的值
                        table[i] = table[i-c]+1
        print(table)
        return table[amount]
# case 99/189: [186,419,83,408] 6249
