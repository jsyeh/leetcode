# 題目計算每個 worker 要對應哪台 bike
# 依距離（近到遠）依序處理。相同時，worker index小的先
# 若同個 worker 有多台 bike 同距離，bike index 小的先
# 1000*1000種（可能的）距離
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        W, B = len(workers), len(bikes)
        def dist(w:int, b:int)->int:
            return abs(workers[w][0]-bikes[b][0])+abs(workers[w][1]-bikes[b][1])
        # 先算出距離對照表（暴力完整的對照表）
        distPair = [[dist(w,b), w, b] for w in range(W) for b in range(B)]
        # 希望依照題目要求的優先處理的順序來排序
        distPair.sort(key=lambda d : d[0]*1001*1001+d[1]*1001+d[2])

        ans = [-1]*W # 每個 worker 對應的 bike
        usedBike = set() # 被騎走的 bike, 一開始是空的
        for d, w, b in distPair: # 照優先順序 來挑車
            if ans[w]==-1 and b not in usedBike:
                # 若 work w 還沒騎車&& bike b沒被騎走
                ans[w] = b # worker w 就騎 bike b
                usedBike.add(b) # 記錄 bike b 被騎走
        # 全部巡完，就知道答案了
        return ans
