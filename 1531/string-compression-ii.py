# 正常的 Run-length encoding 壓縮, 是 aabccc 變成 a2bc3
# 現在是不正常的 Run-length encoding, 竟然可以刪掉原字串的字母
# 請問「刪掉k個字母」後, 壓縮「最短」能多短。超難的。
# 刪掉k個字母, 最有利的,是單1字母的狀況,因為長度可以少1。再來是數字位數變少1位
# 但賺最多的, 是 aabbaa 刪2個,變成  aaaa 後, 可壓成 a4
# 超難的, 我也不知道要怎麼解。在 Solutions 裡, 有兩個人在吵架, 其中一位 MarkSPhilip31的解法,
# 是使用 DP來解， dp[i][k] 代表 字串前面i個字母,如果刪掉k個字母,最短能有多短
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # 首先, 我想要有個函式, 執行 Run-length encoding
        def runLenEncoding(s:str)->str: 
            ans, prevC, count = '', '', 0
            for c in s:
                if c==prevC:
                    count += 1
                else: # 如果字不同, 就是新的開始
                    if count>1: ans += str(count)
                    ans += c # 把之前的變出來
                    prevC = c
                    count = 1
            if count>1: ans += str(count) # 最後一個字母,要補上長度數字
            return ans
        # print(runLenEncoding(s)) # 但這題根本不需要模擬 Run-length encoding,可惡!

        N = len(s) # 字串長度
        @cache
        def dp(i, prevC, count, k)->int: # 前3個參數,都是 RLE 編碼過程中需要的
            if k<0: return inf # 照著 Editorial 的想法: 無法再刪下去, 就給很糟的分數
            if i==N: return 0 # 能走到最後,很好。最後沒有字母的部分, 編碼長度為0

            if_delete_now = dp(i+1, prevC, count, k-1) # 如果現在刪這個字母,算出來的長度
            if s[i]==prevC: # 字母有重覆, 可被編碼的話, 不刪的結果是多少呢?
                if_not_delete_now = dp(i+1, prevC, count+1, k)
                if count == 1 or count == 9 or count == 99: # 都可進位的話, 長度會+1
                    if_not_delete_now += 1 # 那個 count==1 的意思,是當它變成2時, 會多個數字
            else: # 字母沒有重覆, 不刪的結果, 要更新 RLE 的參數, 同時要編碼新字母,長度再+1
                if_not_delete_now = dp(i+1, s[i], 1, k) + 1 
            return min(if_delete_now, if_not_delete_now)

        return dp(0, '', 0, k) # dp(現在處理第i字母, 前個字母prevC, 累積多少count, 可再刪k)
