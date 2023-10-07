# 今天Hard難題：n,m,k 長度n，數字不超過m,只變動k次，便找到最大值
# 這是比較難的DP的題目，要逐一調整每一個變數
# 本來想用 table[n][m][k]來解，但想不起來，只好偷看答案
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # 改用 top-down DP 配合 @cache 再試試
        # 照著 Editorial 的解釋來思考，每個格子有兩種可能：不大or更大
        @cache
        def helper(nn, mm, remain)->int:
        # nn 是現在的陣列長度，mm是現在最大值，remain是剩幾次
            if nn == n: # 陣列大小湊齊了
                if remain == 0: # 也剛好算完
                    return 1
                else: # 失敗了
                    return 0
            
            # 接下來是重點關係式
            # 下一個位數「不比mm大」的可能性有 mm種，要乘
            ans = mm * helper(nn+1, mm, remain)
            ans %= 1000000007
            # 下一位數「比mm大」
            for next in range(mm+1, m+1):
                ans += helper(nn+1, next, remain-1)
                ans %= 1000000007
            return ans # 最後加總的全部可能性
        
        return helper(0, 0, k) # 從0,0開始跑，直到把k用完

        '''
        又解不出來了
        # table[n][m][k] 長度n,不超過m,if執行k次
        # 從 table[0][0][0] 走到 table[n][m][k] 要開大一點
        table = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
        # Python 的三維陣列寫法有點不漂亮

        for mm in range(m+1):
            table[n][mm][0] = 1 # base case
            # 長度為n，修改0次，用到的最大值隨便

        for nn in range(n):
            for mm in range(m):
                for kk in range(k):
                    table[nn][mm][]
        '''
