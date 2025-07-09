# LeetCode 3439. Reschedule Meetings for Maximum Free Time I
# 0...eventTime 間要開 n 個會議 startTime[i]...endTime[i]
# 你有權限「稍微調整 k 個會議」，前後平移，想擠出「最大的空檔」
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # 換個問法，會更簡單：調整k個會議，就可把(k+1)個空檔「併起來」
        N = len(startTime)  # 共有 N 個會議，會有 N+1 個空檔
        space = [startTime[0]] + [startTime[i]-endTime[i-1] for i in range(1,N)] + [eventTime - endTime[N-1]]
        # 接下來，找「連續k+1個數相加」的最大值
        runningSum = 0  # k+1 個數的和
        for i in range(k+1):  # 先將前 k+1 個數「加起來」
            runningSum += space[i]
        ans = runningSum  # 找最大的 runningSum
        for i in range(k+1, N+1):  # 用滑動法，找到 N+1 裡 (k+1) 個數加起來
            runningSum = runningSum + space[i] - space[i-k-1]  # 加頭去尾
            ans = max(ans, runningSum)  # 更新最大值
        return ans
