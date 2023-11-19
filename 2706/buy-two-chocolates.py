# 要買最便宜的2個巧克力，看能剩多少錢。如果不夠錢，就不要買
# 其實就是在迴圈裡，找最小的2個數，便知答案
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        ans1, ans2 = inf, inf # ans1是最小值，ans2是次小值
        for price in prices:
            if price <= ans1: # 比最小值更小（含相等）便能更新遞補
                ans2 = ans1 # 第1名的值變第2名
                ans1 = price # 更新第1名
            elif price < ans2: # 比第2名還小
                ans2 = price # 更新第2名
        # 巡完後，ans1是最小值，ans2是次小值
        if ans1+ans2 <= money: # 如果夠買，就買
            return money-ans1-ans2 # 回傳剩下的錢
        else: # 不夠買的話
            return money # 就不要買，剩全部的錢
