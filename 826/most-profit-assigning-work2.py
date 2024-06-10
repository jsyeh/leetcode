# LeetCode 826. Most Profit Assigning Work
# 每種工作，有不同的 difficulty[i] 及 profit[i]
# 想讓工人合計賺最多錢。工作可重覆做，每個人只能做1個工作。工人的能力值在 worker[i]裡
# 每位 work[w] 有不同的能力等級，work[w]>difficulty[i]才能做工作i
# 所以每個工人都要在「能得到的陣列裡」找最多錢的。陣列要排序一下
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        N = len(profit)
        jobs = [(difficulty[i],profit[i]) for i in range(N)]  # 將工作「組合起來」
        jobs.sort()  # 照（左邊的）難度來排序
        worker.sort()  # 工人也照「能力」排序

        heap = []
        ans = 0
        i = 0  # 對應 jobs[i] 以便查 difficulty
        for w in worker:  # 每位工人，逐一查「適合的工作」，並在裡面「挑最高Profit的工作」
            while i<N and jobs[i][0]<=w:  # 有機會把工作i加入
                heappush(heap, - jobs[i][1])  # 把工作i對應的profit加入 （加負號）
                i += 1
            if i>0: ans += - heap[0]  # 將「能做的工作中」利潤最大的那個，給工人做。（加負號）
        return ans
