# LeetCode 3169. Count Days Without Meetings
# 總共有 1..n天，有些天需要開會 meetings（有開始、結束的範圍），剩幾天「不用開會」？
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # 先照開會時間排序好，「開始時間」排序
        p = [0,0]  # 會移動的「前一筆」的開會時間
        ans = 0  # 「答案」慢慢累積「不用開會」的日子
        for a, b in meetings:  # 照「開始時間」取出來
            if p[1] < a:  # 前一筆「結束時間」，結束得比「後一筆」更早，就有空閒
                ans += a - p[1] - 1  # 便能更新「答案」
                p[0] = a  # 更新「前一筆」資料
                p[1] = b  # 更新「前一筆」資料
            else:  # 不小心重疊了
                p[1] = max(p[1], b)  # 更新「結束時間」
        ans += days - p[1]  # + 最後一段有空「不用開會」的時間
        return ans
