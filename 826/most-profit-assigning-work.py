# 想讓工人合計賺最多錢。工作可重覆做，每個人只能做1個工作。工人的能力值在 worker[i]裡
# 所以每個工人都要在「做得到的陣列裡」找最多錢的。陣列要排序一下
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 先把 worker 照能力排序
        worker.sort()
 
        # 再把 jobs 照難度來排序
        jobs = []
        for i in range(len(profit)):
            jobs.append([profit[i], difficulty[i]])
        jobs.sort(key=lambda x:x[1]) # 照難度來排序
 
        # 接著照 work 能力，找到difficulty 適合的，並在過程中，找到最大的profit
        ans, currentBest = 0, 0
        jobI, workerI = 0, 0
        while workerI < len(worker): # 這個迴圈還沒走完，表示還有員工還沒輪上場
            if jobI >= len(jobs): # 工作都輪完了，直接目前最好的薪水吧
                ans += currentBest
                workerI += 1
            elif worker[workerI] >= jobs[jobI][1]: # 工作難度，還在可以勝任的程度
                if jobs[jobI][0] > currentBest:
                    currentBest = jobs[jobI][0]
                jobI += 1 # 可以換下一個工作試試
            else: # 不能勝任時，就把 currentBest 加到 ans 裡，並換下一位員工
                ans += currentBest
                workerI += 1
        print(jobI, workerI)
        return ans
# case 21/57: [13,37,58] [4,90,96] [34,73,45]

