# 原本題目看不太懂，就用 Example 1 來理解
#  前一次跳距離k, 下一次跳 k-1 or k or k+1
#  第1次跳必須距離1
# 原本想到 dp[i][k] 表示到達 stone[i] 用距離k跳到，但會超時
# 參考 quencyhehe 解法後，視野開闊 -- 原來可反過來想
#  利用 dict 減少考慮範圍、加速，了解「能到的步數」
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # if stones[1] != 1: return False # 這步可省下來
        # 第一步只能跳1，且stones[0]==0，故stones[1]必須是1

        possible = {} # possible[pos] move at position pos
        for stone in stones:
            possible[stone] = [] # 一開始還不知能否走到
        possible[stones[0]].append(1) # 一開始能走1 from stone[0]

        for now in stones: # 每一顆石頭(在位置now)，都嘗試出發
            if len(possible[now])==0: continue
            # 之前沒走到本石頭，就不要從本石頭往下走

            for k in possible[now]: # 現在能走的步(位置now出發)
                if now+k==stones[-1]: # 恭喜到達目的地
                    return True;

                if now+k in possible: # 能到新石頭(位置now+k有石頭)
                    if k-1>0: # 小心，不要往回走，不然迴圈會走不完
                        possible[now+k].append(k-1)
                    if k not in possible[now+k]:
                        possible[now+k].append(k)
                    if k+1 not in possible[now+k]:
                        possible[now+k].append(k+1)
                    # 上面可加速，因重覆數字不用append
        return False

