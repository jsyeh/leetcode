# LeetCode 1833. Maximum Ice Cream Bars
# 悶熱的夏天，要吃冰淇淋。n個冰淇淋，價錢是 costs[i]，可買幾個冰淇淋？
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()  # 小到大排好
        ans = 0
        for cost in costs:  # 小到大去買
            if coins>=cost:
                ans += 1
                coins -= cost
            else: break
        return ans
