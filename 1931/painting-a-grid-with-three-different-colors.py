# LeetCode 1931. Painting a Grid With Three Different Colors
# 用3種色彩為 m x n 的 grid 著色，相鄰不能同色，「有幾種著色法」
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9+7  # 用來計算「餘數」
        # m<=5筆，可用 bitmask 標示「直行5格的色彩」，每格0，1，2，3共4色對應 2 bit
        @cache  # 看起來就像 DP 的問題，用「函式呼叫函式」來解，再左到右逐一「往右推過去」
        def checkCol(prev, j):  # 左邊是 prev 圖案，現在「走到col j」，答案是多少
            return checkIJ(0, j, prev, 0)  # 問 helper2() 找答案，並記下答案
        # 上面用 cache 可減少大量計算。下面還在零星計算中，不使用 @cache 的記憶功能
        def checkIJ(i,j, prev, now):  # 現在處理到 (i,j) 這格, 上往下、左往右走
            if i==m: return checkCol(now, j+1)  # 撞到下面，一直行完整，換到「右邊最上面」
            if j==n: return 1  # 右邊走到盡頭，全部走完，得到1個解，算1次
            left = prev >> (i*2) & 3  # 由 bitmask prev bitwise 算出「左邊格」的「色彩代碼」
            if i==0: up = 0  # 最上面那排，沒有 up 的格子
            else: up = (now >> (i-1)*2) & 3  # 由 bitmask now bitwise 算出「上面格」「色彩代碼」
            ans = 0
            for c in range(1,4):  # 現在想填的可能「色彩代碼 1,2,3」都試過一次（原本沒填的代碼是0）
                if c != left and c != up:  # 與「左邊」「上面」都不相同，就可「函式呼叫函式」再深入研究
                    ans += checkIJ(i+1, j, prev, now + (c<<(i*2)))  # 填入 c 算出新的 bitmask
                    ans %= MOD  # 怕數字太大，要計算「餘數」
            return ans
        return checkCol(0, 0)  # 上到下、左到右，依序找答案
