class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        N = len(dist)
        M = max(dist)
        def possible(speed: int) -> bool: # 速度speed可能達hour小時嗎？
            total = 0
            for i in range(N-1):
                total += math.ceil(dist[i]/speed) # 每一趟花幾小時(整數)
            total += dist[N-1]/speed # 最後一趟，用 float 加法（不用整數）
            if total<=hour: return True # 花的時間來得及，True
            else: return False # 來不及，False

        # binary search 用來推算 speed
        left, right = 1, 10000001 # 題目說最快是10^7（10^5加小數點下2位）
        while left<right:
            mid = (left+right) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        if left==10000001: return -1 # 不可能達成任務，回傳-1
        else: return left # binary search 的結果
# case 63/66: [1,1,100000] 2.01
