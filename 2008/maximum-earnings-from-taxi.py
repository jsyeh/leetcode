# rides 裡有一堆 [start,end,tip] 的資料
# 載一位乘客可賺到 end-start+tip 的值
# 一次只載1位乘客。旅客下車end後，另一位可上車start
# 不過，如果範圍有重覆，就需要取捨，以賺最多錢
# 先排序，再用 DP 配合 bisect_left() 來解
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        N = len(rides)
        rides.sort()
        start = [rides[i][0] for i in range(N)] # 供 bisect_left() 的陣列
        earn = [rides[i][1]-rides[i][0]+rides[i][2] for i in range(N)] # earn[i]: 載 rides[i] 能賺的錢，照公式寫
        @cache 
        def dp(i): # 考慮排序後第i個乘客+之後，能賺最多的解
            if i==N: return 0
            ans = dp(i+1) # 若不載 rides[i]乘客
            j = bisect_left(start, rides[i][1]) # rides[i][1] 結束後，可接 rides[j][0]開始
            return max(ans, dp(j) + earn[i]) # 不載或載 rides[i]，能賺最多的解
        return dp(0) # 從0開始，全部考慮
