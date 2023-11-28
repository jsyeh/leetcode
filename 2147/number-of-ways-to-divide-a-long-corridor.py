# lee215 分享很帥的解法，先記得 seat的座標
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat = [] # 把 S 的 index 記起來
        for i, c in enumerate(corridor):
            if corridor[i]=='S': seat.append(i)
        # print(seat)
        if len(seat)%2!=0 or len(seat)==0: return 0
        # 奇數椅子：失敗，0個椅子：失敗

        MOD = 10**9+7
        ans = 1 # 答案會一直乘起來
        for i in range(2, len(seat), 2): # 2個椅子為1組
            ans = ans * (seat[i]-seat[i-1]) % MOD
            # 中間的距離，可以挑1個位子來放隔板，組合數一直乘
        return ans
