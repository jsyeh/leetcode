# LeetCode 2463. Minimum Total Distance Traveled
# 機器人在 robot[i] 位置，要進工廠 factory[j] 維修
# 工廠 factory[j] 有它的位置、容量，不能超過維修容量。
# 問機器人進廠維修「移動」的「最小距離和」是多少
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()  # 左到右排序
        factory.sort()  # 左到右排序
        R, F = len(robot), len(factory)  # 機器人數量、工廠數量（終止條件會用到）
        @cache # 利用 Dynamic Programming 動態規劃來解，使用「函式呼叫函式」配合 cache 記憶功能
        def helper(i, j, k):  # 考慮機器人i、工廠 j，其中工廠 j 已用掉 k 個維修容量，問移動的「最小距離和」
            if i==R: return 0  # 終止條件：機器人全部處理完，最簡單的終止條件，距離是0
            if j==F: return inf  # 終止修條件：工廠不夠用，沒正常結束，就失敗

            if k == factory[j][1]: # 抱歉，工廠 j 維修容量不足（已用掉 k 個維修容量，工廠滿了，無法再維修）
                return helper(i, j+1, 0)  # 只能再開新工廠 j+1
            else:  # 工廠 j 的維修容量還夠，那就有2種可能：
                # (1) 使用工廠 j 的第 k+1 個維修容量。機器人 i 在工廠 j 維修，計算距離
                ans1 = helper(i+1, j, k+1) + abs(robot[i]-factory[j][0])
                ans2 = helper(i, j+1, 0)  # (2) 不管舊工廠，再開新工廠 j+1 加入維修行列，繼續問
                return min(ans1, ans2)  # 以上2種可能，看誰的距離最小
        return helper(0, 0, 0)  # 從 robot 0, factory 0 開始處理
