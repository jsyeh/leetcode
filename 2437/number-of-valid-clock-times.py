# 有問號的地方，對應有幾個可能的答案
# 因為總共只有 24*60 種可能，所以暴力試即可
# 不過速度82ms排行很後面，有點遜
class Solution:
    def countTime(self, time: str) -> int:
        ans = 0
        for hh in range(24):
            for mm in range(60):
                now = f'{hh:02}:{mm:02}'
                bad = False
                for i in range(5):
                    if time[i]=='?': continue
                    if time[i]!=now[i]: bad = True
                if not bad: ans += 1
        return ans
