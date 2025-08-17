# LeetCode 837. New 21 Game
# 很像「21點」遊戲，改成「新21點(k)」。每次發牌會拿到 1..maxPts 之間的點數
# 一直發牌「直到 k點 或以上」為止，問「拿到 n點 或以下」的機率
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0: return 1  # 先例外處理「特殊的值」
        if n >= k + maxPts: return 1  # 先例外處理
        # 使用 Bottom-Up Dynamic Programming 的方法來解
        table = [1] + [0] * n  # 先建表格，table[i] 將對應發牌的機率
        P = 1 / maxPts  # 總共有 maxPts 種牌，發其中一種牌的機率是 1/maxPts
        winSum = 0  # 為節省迴圈，照 1...maxPts 範圍建 sliding window sum
        ans = 0
        for i in range(1,n+1):  # 想知道「拿到 n點 或以下」的機率
            if i <= k:  # 在湊齊「21點」前，要累積sliding window +新頭
                winSum = winSum + table[i-1]
            if i > maxPts:  # 湊齊「1...maxPts」完整範圍後，便可「滑動」 -舊尾
                winSum = winSum - table[i-maxPts - 1]
            table[i] = P * winSum  # 由前10項的結果，更新 table[i]
            if i>=k:  # 達到「新21點(k)」便可更新 ans
                ans += table[i]
        return ans
