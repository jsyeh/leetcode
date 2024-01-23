# 有一堆短字串，可接成「字母都不能相同」的最長長字串
# 可能還是要DP來解：每次多考慮1個短字串。
# 總共有16個短字串，排列組合共2^16種組合，暴力算即可
# 但是 lee215 竟然利用 set()想到一個很帥的解法
# 把「不重覆字母」的短字串，給成集合後，再暴力for迴圈逐一試「能不能結合」
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        table = [set()] # 最基礎的1個 empty空集合，暴力for迴圈可結合別人
        for a in arr: # 每次取出1個短字串a
            # 如果裡面有重覆的字母，就跳掉這筆
            if len(a) != len(set(a)): continue 
            # 沒有重覆的話，就暴力for迴圈，逐一看「能否與table裡現有的做結合」
            a = set(a)
            for c in table: # 目前已有的集合
                if a&c : continue # 若有重覆的，就跳掉不做
                table.append(a|c) # 把結合的交集，加入table
        ans = 0
        for c in table:
            ans = max(ans, len(c))
        return ans

