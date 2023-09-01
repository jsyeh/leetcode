# 公司在IPO前，要做projects，各有 profit[i] 及最小資本要求 capital[i]，
# 一開始資本只有w，要做 k 個專案（利潤讓資本慢慢增加），希望最後變最多資本
# profit: 1,2,3
# capital:0,1,1 一開始w=0 只能挑 i:0，賺到1（公司變大）便能做其他projects
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        N = len(profits)
        projects = [] # projects[i][0]是資本要求，projects[i][1]是能賺的錢
        for i in range(N):
            projects.append([profits[i], capital[i]])
        # 先針對 capital排序，便能（在資本的限制下）依序加入 heap，再挑最賺錢的做
        projects.sort(key = lambda x: x[1]) # 以資本來挑序
        # 將把資本夠/能做的專案，加到Heap裡
        heap = []
        # heapify(heap) 這行可以不用做，因為空空的
        i = 0  # i: projects[i]
        while k > 0:  # 還能做k個 projects 
            while i<N and projects[i][1] <= w: # 還有專案，且資本w夠執行它，就全加入heap
                heappush(heap, -projects[i][0]) # 賺錢的負數（因heap從小到大）
                i += 1 # 之後測下一筆

            if len(heap)<=0: # 不幸「能做的專案」沒有了
                break; # 就結束
            earn = - heappop(heap) # 負負得正，將賺到的錢變回正數
            w += earn # 賺到錢了
            k -= 1 # 還能做的專案變少了
        return w
