# 一堆開會的時間，問「要幾間會議室」才夠開會
# 這類的題目之前寫過，有個是用 end time 做排序。
# 不過看了 Editorial 的 Video Solution 是用 start time排序
# 看了2分鐘後，猜可能用 heap 來標示「end time」會很適合
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0]) # 用 start time排序
        heap = [] # 用來標示會議室「能再度使用」的時間
        for start,end in intervals:
            if len(heap)>0 and heap[0]<=start: # 有房間能用
                heappop(heap) # 房間拿來用
                heappush(heap, end) # 標示新的結束時間
            else: # 房間不夠用
                heappush(heap, end) # 開新會議室，並標示結束時間
        return len(heap)
