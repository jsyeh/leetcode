# LeetCode 888. Fair Candy Swap
# Alice 和 Box 有很多盒糖果，每盒糖果數量是 aliceSizes[i] bobSizes[j]
# 兩人想交換「一盒」糖果後，讓兩人糖果數量相同。換的是「幾個糖果」的盒子？
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        S1, S2 = sum(aliceSizes), sum(bobSizes)  # 兩人的糖果數
        diff = S1 - S2  # Alice 比 Bob 多 diff 顆糖
        give = diff // 2  # Alice 要「多給」Bob 這麼多，即可平衡
        # 題目改成「以盒為單位」要交換哪一盒，Alice 的那盒，要比 Bob 多 give 個糖
        bob = set(bobSizes)  # 把 Bob 每個盒子的糖果數，記入 set() 裡
        for a1 in aliceSizes:  # 把 Alices 的每盒，逐一看看
            if (a1-give) in bob:  # 如果這盒 a1 給 bob，Bob 能否回送 a1-give 的盒子
                return [a1, a1-give]  # 可以的話，就成功了
