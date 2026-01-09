# LeetCode 1431. Kids With the Greatest Number of Candies
# 小朋友糖果數量 candies，請逐一測試再給 extraCandies，他是否會最多
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        K = len(candies)  # 有 K 位小朋友，每人手上糖果數 candies[i]
        target = max(candies)  # 目前最多的糖果數，目標是要比它多(可相等)
        return [extraCandies+candies[i] >= target for i in range(K)]
