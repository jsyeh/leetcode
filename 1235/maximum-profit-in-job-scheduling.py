# 每個工作有 startTime[i], endTime[i], profit[i]
# 工作不能重疊，最多能賺多少 profit (結束時可馬上開始另一工作)
# 看起來可以用 DP 解，但是到底大問題、小問題的「關係」是什麼呢？
# 看了 Editorial 的解法，程式有夠複雜的
# 看了 lee215 解法，是用endTime做排序，程式太精簡，且與Editorial差太多
# 最後看 hiepit 解法，很適合理解。但它方法1竟然超時，只好用方法2 bisect_left()加速
# 所以本題我學會了新的解法，也學了一些精簡的程式碼，收穫很多。
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(profit) # 有N個工作
        # 下面將資料聚合在一起，以便一起排序
        #job = [[startTime[i],endTime[i],profit[i]] for i in range(N)] 
        #job.sort(key=lamba a:a[1]) # 本想模仿 leet215 照第2項endTime排序
        # 不過最後改用 hiepit 的解法，以 startTime 排序
        job = sorted(zip(startTime,endTime,profit)) # 學到這寫法，好帥
        startTime = [job[i][0] for i in range(N)] # 排序後取出 startTime 供bisect_left()用

        @cache
        def dp(i): # 左邊i會問右邊j的小問題。從右到左邊累加出max profit
            if i==N: return 0 # 超過右邊界，從i到右的 profit 是 0
            ans = dp(i+1) # 如果不使用 job[i] 跳過，暫時的答案是 dp(i+1)
            # 下面是巧妙的一行，利用binary search 找到 i+1...N 最適合的接的位置
            j = bisect_left(startTime, job[i][1]) 
            # 所以 job[i][1]結束 可接 job[j][0] 開始，利潤是 job[i][2] + dp(j)
            return max(ans, dp(j)+job[i][2]) # 不用job[i] or 用job[i]，最佳利潤
        return dp(0) # 從頭開始，好好的問下去（Top-Down Dynamc Programming)

