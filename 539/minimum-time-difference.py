# LeetCode 539. Minimum Time Difference
# 給一堆字串，內含 24小時制的時間，問「它們間最小的時間差多少?」
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        a = []
        for time in timePoints:  # 就用簡單的迴圈
            hh, mm = time.split(':')  # 把字串斷成數字
            a.append(int(hh)*60+int(mm))  # 算出「00:00到hh:mm差幾分鐘」
        a.sort()  # 再排序就好了
        ans = inf  # 答案一開始「無限大」
        for i in range(len(a)-1):  # 用迴圈, 兩兩比較
            ans = min(ans, a[i+1]-a[i])  # 計下最小值
        ans = min(ans, a[0] + 24*60 - a[-1])  # 跨午夜 24:00 再和 a[0]比較
        return ans
