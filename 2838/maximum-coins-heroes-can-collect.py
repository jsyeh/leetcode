# LeetCode 2838. Maximum Coins Heroes Can Collect
# n 位英雄 heroes 要打 m 個怪物 monsters 各種排列組合
# 只要 hero >= monsters[i] 就可得 coins[i]，問 heroes 可得多少金幣
class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        n, m = len(heroes), len(monsters)
        # 數字很大，不能用兩層 for 迴圈暴力去試
        # 可將  monsters 與 coins 合在一起排序，用 binary search 找答案
        monstersCoins = sorted(zip(monsters, coins))  # 一起排序
        monsters, coins = list(zip(*monstersCoins))  # 再拆開
        prefixCoins = [0]  # 快速找答案的 prefix sum of coins
        for coin in coins:  # 為加速，將 coins 變成 prefix sum
            prefixCoins.append(prefixCoins[-1] + coin)
        for i in range(n): # 針對每個 heroes[i]
            ii = bisect_right(monsters, heroes[i])  # bisect 會到到「插入點」
            heroes[i] = prefixCoins[ii]  # 插入點「對應」的 prefixCoins[ii] 是全部能得的金幣
        return heroes  # 答案放裡面、回收再利用
