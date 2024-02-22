# 這題是「每個人都要相信」法官，且法官「不相信任何人」
# a 相信 b, 所以a不是法官、b可得1票
# 最後查看有誰「可能是法官」同「得到n-1票」
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        possible = [True]*(n+1) # 如果放在a, possible[a] = False
        trustCount = [0]*(n+1) # trustCount[3]有幾個人相信3
        for a,b in trust: # a 相信 b
            possible[a] = False # a不是法官
            trustCount[b] += 1 # b得到1票信任票
        for i in range(1,n+1): # 最後再查一次
            # 可能是法官，同得到全部的 n-1 票
            if possible[i] and trustCount[i] == n-1:
                return i # 他就是法官
        return -1 # 沒有人是法官，哎！
