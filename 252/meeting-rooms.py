# 每個 meeting 有 intervals[i] 時間, 問能否「全部」都參加
# 所以先以開始時間做排序，再看結束時間有無衝突
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False # 前一場還沒結束，下一場就開始
        return True
