# 糖果買二送一，送的那個價錢不能太高，要<=你買的便宜的那個
# 可以先排序後，再由大到小、買兩個、送一個
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ans = sum(cost) # 全部都要花錢買，要多少錢
        
        # 買cost[N-1] 買cost[N-2] 送 cost[N-3] 依序下去
        for i in range(len(cost)-3, -1, -3): # 要送的那個
            ans -= cost[i] # 錢就可以省下來
        return ans
