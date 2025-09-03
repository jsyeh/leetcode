# LeetCode 3027. Find the Number of Ways to Place People II
# 和昨天 3025 很像，但測資從 50筆 變成 1000筆，題目變難，不能三層迴圈暴力解
# 空間的問題，可照位置排序 Hint 1: 照位置排序，讓Alice優先在左上角、Bob在右下角
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        N = len(points)  # 總共有 N 個點，供 for 迴圈使用
        ans = 0  # 有幾組 points[i] points[j] 合乎規定（左上、右下，方塊間沒有其他點）
        points.sort(key=lambda p:(p[0],-p[1]))  # Hint 1: 照位置排序：先x座標，再-y座標
        # Hint 2 因排序好，所以 左邊 points[i] vs. 右邊 points[j]
        for i in range(N):
            x1, y1 = points[i]  # 左邊的 Alice: points[i]
            prevY = -inf  # 關鍵技巧：夾於 points[i]...points[j] 間「曾出現的點 Y 座標」
            for j in range(i+1, N):  # 從 i+1 開始，才能確保 i,j 兩點的「左右關係」
                x2, y2 = points[j]  # 右邊的 Bob: points[j]
                # points[j] 有幾種可能：在 points[i] 之上(bad)、一樣高(可能)、之下(可能)
                # 同時我們記錄「兩點之間的點的 y 座標」， 是否「卡在y1...y2中間」
                if y1 >= y2 > prevY:  # 關鍵技巧：「曾出現的點 Y 座標」「沒卡在中間」
                    ans += 1
                    prevY = y2  # 關鍵技巧：y2變成「曾出現的點 Y 座標」、抬高了
        return ans
