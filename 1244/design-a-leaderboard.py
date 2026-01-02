# LeetCode 1244. Design A Leaderboard
# 實作 addScore(playerId, score), top(K), reset(playerId)
# 難在 top K 要怎麼加總？因為 score <= 100 可用 Counter() 累計「同分的人數」
# 但不幸的是「分數會越加越高」超過100，所以迴圈可能「越跑範圍越大」
class Leaderboard:

    def __init__(self):
        self.counter = Counter()
        self.score = {}  # 「分數對照表」

    def addScore(self, playerId: int, score: int) -> None:
        oldScore = 0
        if playerId in self.score:
            self.counter[self.score[playerId]] -= 1  # 舊成績少1人
            oldScore = self.score[playerId]
        self.counter[oldScore + score] += 1  # 新成績多1人
        self.score[playerId] = oldScore + score  # 更新「分數對照表」

    def top(self, K: int) -> int:
        ans = 0
        values = sorted(self.counter.items(), reverse=True)  # 分數「從大到小」排好
        for score, people in values: #for score in range(100,0,-1):
            ans += min(people, K) * score #ans += min(self.counter[score],K) * score
            K -= people  # K -= self.counter[score]
            if K<=0: return ans

    def reset(self, playerId: int) -> None:
        self.counter[self.score[playerId]] -= 1
        self.score[playerId] = 0
        #del self.score[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
