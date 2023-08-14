# 想用coins(有重覆)做出 0, 1, 2, ... 等數，最多可組到多少
# 但 DP 不能用暴力for迴圈，因為 10^4*10^4超時
# lee215提出greedy解法：排序後，每次多用1個數a 
# (1) a>答案，跨太大步，沒辦法補齊ans...a 所以結束在ans
# (2) a<=ans，表示可以接起來 ans...ans+a中間部值，ans+=a
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort() # 從小到大排好
        N = len(coins)
        ans = 1 # 從0開始數，一定有0這組
        for a in coins:
            if a<=ans: # 可以接起來
                ans += a # 接起來後，能到的長度增加
            else: # 不能接起來的話
                return ans # 就只好結束了
        return ans

