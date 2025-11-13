# LeetCode 636. Exclusive Time of Functions
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        s = [[-1,0,0]]
        prevT = 0
        for log in logs:
            pid, state, t = log.split(':')  # id, 'begin' or 'end', time
            if state=='start':
                s.append([pid,t,0])  # 被別人用掉多少時間
            else:
                pid0, t0, p0 = s.pop()
                ans[int(pid)] += int(t) - int(t0) + 1 - p0
                s[-1][2] += int(t) - int(t0) + 1 
        return ans
