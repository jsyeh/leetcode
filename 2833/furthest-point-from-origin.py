# 左走L 右走R 隨便走_，問「離0」最遠的距離
# 其實把 _ 都設成R 或 都設成L 其中一個是答案
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        ans = 0 # 用 R 或 L 會走到哪裡
        _ = 0 # 遇到幾個底線 _ 之後全部灌成 R 或 L
        for c in moves:
            if c=='R': ans += 1
            elif c=='L': ans -= 1
            else: _ += 1
        
        return max(abs(ans+_), abs(ans-_))
