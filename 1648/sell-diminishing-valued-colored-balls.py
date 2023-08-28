# 每個球的價值會慢慢減少，取決當時有幾個球 inventory存貨 及總共 orders訂單
# 找「最大的價值」
# 參考 lzl124631x 的解說，找「有幾種球」大於 k 加起來是多少
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        balls = inventory # 這個名字比較好懂，balls[i] 表示第i種球的數量

        def above(k: int) -> int: # 想統計「高於k」的球有幾個
            ans = 0
            for amount in balls:
                if amount>k: ans += amount - k
            return ans

        left, right = 0, 1000000001
        while left < right:
            mid = (left+right)//2
            print(left, right, mid, above(mid))
            if above(mid) > orders:
                left = mid + 1
            else:
                right = mid

        # 找到 left 是最適當的 k 值，接下來數數這些球價值多少錢
        profit = 0
        for i in range(len(balls)):
            if balls[i] > left:
                profit = profit + (balls[i]+left+1)*(balls[i]-left)//2
                orders -= balls[i] - left
        print("orders:", orders, "profit:", profit)
        if orders>0: # 不小心扣太多了
            profit += orders*left
        return profit % 1000000007

