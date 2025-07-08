# LeetCode 1751. Maximum Number of Events That Can Be Attended II
# 活動有開始時間、結束時間、對應價值，需全程參與，最多參加 k 項活動
# 要「累積最高價值」。參加某個活動，就會罷佔某段時間，同時之後能參加的活動 -1
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()  # 先針對「活動開始時間」小到大排序
        start = [event[0] for event in events]  # 活動開始時間，再 binary search 用
        @cache  # 利用「函式呼叫函式」來解
        def helper(i, k):  # 考慮第i個活動，剩k個活動能參加，最高價值
            if k<=0: return 0  # 沒額度了，不能參加、沒有價值
            if i>=len(events): return 0  # 考慮完全部 events
            c1 = helper(i+1, k)  # 選擇1：不參加活動i
            # 選擇2：要參加活動i，用「活動結束」後 + 1 當成新活動開始時間，再 binary search 快速找到
            index = bisect_left(start, events[i][1] + 1)  # 如果選擇活動i、佔用時間後，能參加的活動
            #if index >= len(events): c2 = 0
            #else: c2 = events[index][2] + helper(index, k-1)
            c2 = events[i][2] + helper(index, k-1)
            return max(c1,c2)
        return helper(0, k)
