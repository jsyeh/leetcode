# 本題可用 greedy 來解，看「能裝滿幾個包包」
# 所以先把 bag 剩餘空間算出來，從小到大排好，再依序裝滿
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        bags = [capacity[i]-rocks[i] for i in range(len(rocks))]
        # print(bags)
        ans = 0
        for b in sorted(bags): # 將袋子空間從小到大排好
            if additionalRocks >= b: # 能裝滿就裝滿
                additionalRocks -= b
                ans += 1
            else: # 不夠裝，就到了盡頭，該結束了
                return ans
        return ans
