# LeetCode 3440. Reschedule Meetings for Maximum Free Time II
# 你可調整「1個」Meeting時間（不用照順序），做出的「最大的空檔/空格」
# 有兩種可能: (1) 把某個 Meeting 平移「碰到另一個開會」也就是結合「兩相鄰空檔/空格」
# (2) 把某個 Meeting 搬到比較遠的空檔(如果放得下)，也就是「兩相鄰空檔+中間開會」
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        N = len(startTime)  # 有 N 個活動，對應下方 N+1 個空檔
        space = [startTime[0]] + [startTime[i]-endTime[i-1] for i in range(1,N)] + [eventTime - endTime[N-1]]
        space2 = sorted( [[space[i],i] for i in range(N+1)])  # 從小到大排好(對應)
        ans = 0
        for i in range(N):  # 針對 Meeting 逐一檢查
            ans = max(ans, space[i]+space[i+1])  # (1) 平移的話，可結合「兩相鄰空檔/空格」
            now = endTime[i]-startTime[i]  # 現在 Meeting 的長度
            index = bisect_left(space2, now, key=lambda x:x[0])  # (2) 能移到其他空格嗎?
            for k in range(3):  # 把 3 個if，用 for 迴圈改寫
                if index+k <= N and space2[index+k][1] != i and space2[index+k][1] != i+1:
                    ans = max(ans, space[i] + now + space[i+1])
        return ans
