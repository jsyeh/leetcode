# LeetCode 2054. Two Best Non-Overlapping Events
# events[i] 裡有 [startTime, endTime, value] 3 個值
# 挑「兩個事件」參加，value相加「最有價值」。但「兩個事件」不能重疊
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort() # Hint 1 建議照事件的 startTime 排序
        heap = []  # 用 Priority Queue (heap) 照 事件的 endTime 排好，便能取出「不重疊」的舊事件
        ans = 0  # 「兩個事件」 加起來的最大值
        maxPrevVal = 0  # 「目前時間」之前的「舊事件」value最大值
        for start, end, val in events:  # 考慮「新事件」
            while len(heap)>0 and heap[0][0]<start:  # 舊事件 與新事件不重疊（頭尾不相碰）
                prevEndTime, prevVal = heappop(heap)  # 取出 heap 裡不重疊的事件，更新 maxPrevValue
                maxPrevVal = max(maxPrevVal, prevVal)  # 更新之前不重疊的「舊事件」最大值
            ans = max(ans, maxPrevVal + val)  # 「舊事件」+「新事件」，更新「兩個事件」的價值
            heappush(heap, (end, val))  # 現在的「事件」也塞入 heap 變「舊事件」
        return ans
