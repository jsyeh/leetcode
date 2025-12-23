# LeetCode 2054. Two Best Non-Overlapping Events
# events[i] 裡有 [startTime, endTime, value] 3 個值
# 挑不重疊的「兩個事件」參加，value相加「最有價值」
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()  # 照startTime 開始時間（小到大）排序
        ans = 0  # 「兩個事件」 加起來的最大值
        heap = []  # 將照 endTime 排好，便能取出「不重疊」的「舊事件」
        prevMaxValue = 0  # 「已結束」事件中「最大的價值」
        for start, end, value in events:  # 現在的「事件」
            while heap and heap[0][0] < start:  # 「已結束」的舊事件，依序取出
                end0, value0 = heappop(heap)  # 重點在「已結束」的舊事件的價值
                prevMaxValue = max(prevMaxValue, value0)  # 更新價值
            ans = max(ans, prevMaxValue + value)  # 更新答案
            heappush(heap, (end, value))  # 現在「事件」也塞入 heap 變「舊事件」
        return ans
