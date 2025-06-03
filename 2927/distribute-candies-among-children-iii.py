# LeetCode 2927. Distribute Candies Among Children III
# 有 n 個糖，分給 3 個小朋友，每人的糖數「不能超過 limit」問有幾種分配法？
# 之前解 2929. Distribute Candies Among Children II 只有 10^6 測試
# 當時用「一層迴圈」（配合「移項變號」找不等式的上下界），雖可通過，但速度很慢。
# 今天這題 2927 是 10^8 不能用迴圈，可用高中教的「排列組合」來試試。
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def count_ways(candies): 
            if candies < 0: return 0  # 剩下負數的糖，就 0 種方法
            # 高中排列組合：將 candie 糖排成一列，中間「放2個分隔線」
            # 在 candie+2 個位置，挑2個「放分隔線」，有幾種放法？
            return comb(candies+2, 2)  #「分配法」是 C candie+2 取 2
        # 有了上面「排列組合」的公式，接下來用「加減法」把「不可能的」刪掉
        total = count_ways(n)  # n 個糖果，不限制數量，排列組合的分配法
        # 第1種，要減掉的，是「有1位以上小朋友，超過 limit 糖果」
        # 可想像「先讓1位小朋友拿了 limit +1 個糖」，再用 count_ways() 
        # 處理剩下的糖，那保證「至少有1位小朋友超標了」
        total -= 3 * count_ways(n - (limit+1) )  # 3個人都試一次

        # 但可能會「重覆扣到」的狀況，也就是「若2位小朋友超標」會重覆扣
        # 第2種，要加上的，是「補上」2位小朋友都超標的狀況
        # 先預留「limit+1個糖」給第1位、預留「limit+1個糖」給第2位，剩下再分
        total += 3 * count_ways(n - 2*(limit+1))  # 有3種預留法

        # 但可能會「重覆補回」的狀況，也就是「若3位小朋友都超標」這個
        # 第3種，要再減掉，也就是先預留「limit+1個糖」給3位小朋友，再分剩下的
        total -= count_ways(n - 3*(limit+1) )

        return total  # 最後的可能分配方法
