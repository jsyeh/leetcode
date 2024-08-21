# LeetCode 664. Strange Printer
# 奇怪的印表機：一次印出一堆「相同的字母」，再換下個字母「蓋掉某範圍的字」
class Solution:
    def strangePrinter(self, s: str) -> int:
        N = len(s)
        # 答案對照表 table[left][right] 不合理的格子會先幫我填 0 ex. 左大 右小
        table = [[0]*(N+1) for _ in range(N+1)] 
        for i in range(N):  # 一切的基礎，要印1次
            table[i][i] = 1  # 只印1個字母，那 左界i 右界i 相同，答案是「要印1次」
            
        for dist in range(1,N):  # 左右界的距離，現在處理2字母、3字母...N字母
            for left in range(N-dist):  # 決定左邊界 (要為右邊界準備位置，要縮一些)
                right = left + dist  # 決定右邊界（兩個距離是 dist 所以 + dist 即可）
                table[left][right] = 1 + table[left+1][right]  # 最基礎的答案，左邊獨立印1次，右邊再印
                for k in range(left+1,right+1):  # 中間的格字 s[k] 可省下墨水嗎？
                    if s[left]==s[k]:  # 如果相同，就可以省下1次，因先印 s[left]...s[k] 再處理
                        now = table[left][k-1] + table[k+1][right]  # 扣掉s[k]後，左右兩半查表找答案
                        table[left][right] = min(table[left][right], now) # 答案更小，就更新
        return table[0][N-1]  # 最長範圍的答案算出來了，開心
