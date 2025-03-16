# LeetCode 2594. Minimum Time to Repair Cars
# 修車花的時間公式是 r * n * n 其中 r 是 rank 排名，n 修幾台車
# 把全部車一起送修，要等多久？總共有 10^6很多車，要分配給 10^5 個維修工
# 感覺很難。但如果用 binary search 就可很快「猜出答案」 
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def helper(m):  # 請問 m 分鐘，有沒有機會完成任務？
            repaired = 0  # m 分鐘內，可修幾台車
            for r in ranks:  # 每一位修車技士
                repaired += int((m/r) ** 0.5)  # 能在 m 分鐘修幾台車，加起來
            return repaired >= cars  # 修車能量足夠，就 True        
        M = min(ranks) * cars * cars  # 假設全部丟給修車最快那個，虐待他，要花的時間
        # M = 10**14  # 也可設很大很大的數，看題目是 10^6台車*10^6，r最大100，就10^14
        return bisect_left(range(M+1), True, key=helper)
