# LeetCode 983. Minimum Cost For Tickets
# 坐火車有一日券、七日券、30日券，票價是 costs[0] cost2[1] costs[2]
# 不是每天都需要坐火車，days[i] 才要坐火車。問你怎麼買票「最便宜」
# 可能 Dynamic Programming 可解，但怎麼做呢？就試過 3 種買法
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def helper(i, passDay):  # 現在處理 days[i]，買的票足夠用到 passDay
            if i == len(days): return 0  # 終止條件：處理完全部資料，回傳基礎0

            if days[i]<passDay: return helper(i+1, passDay)  # passDay 夠用，不用買
            # 以下不夠用，要再買 N-day pass
            ans1 = helper(i+1, days[i]+1) + costs[0]  # 若買 1-day pass
            ans7 = helper(i+1, days[i]+7) + costs[1]  # 若買 7-day pass
            ans30 = helper(i+1, days[i]+30) + costs[2]  # 若買 30-day pass
            return min(ans1, ans7, ans30)  # 看哪一種買法「比較便宜」
        return helper(0, 0)  # 從頭開始測
