# LeetCode 1353. Maximum Number of Events That Can Be Attended
# events 有活動開始、結束的日子，每天只能參加1個活動，問你最多能參加幾個活動
# 處理原則很簡單：(1)活動依序「開始」，放入heap (2)每天參加活動時，選「快結束」的那個
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()  # 先針對活動「開始時間」排序
        ans = 0  # 能順利參加「幾個活動」
        i = 0  # 現在處理的事件是 event[i]
        heap = []  # 某天能參加的活動，都即時在heap裡「可依活動結束時間」取出來
        for day in range(1,100001):  # 活動的日子範圍 1...100000
            while i < len(events) and events[i][0] <= day:  # 活動在 day 之前開始
                heappush(heap, events[i][1])  # 記下活動的結束時間
                i += 1  # 將看下一個活動
            # 現在「所有能參加的活動」都放在heap裡，並標示它的結束時間
            while heap and heap[0] < day:  # 若heap裡「活動已結束」
                heappop(heap)  # 就丟掉
            # 今天要挑什麼活動呢?
            if heap:  # 今天還有活動可以參加，太好了
                heappop(heap)  # 參加最早結束的活動、用掉它
                ans += 1  # 多參加1個活動、真開心
        return ans  # 照此規則「能參加最多的活動」
