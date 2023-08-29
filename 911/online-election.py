# 投票時，即時了解「誰暫時第一」，最多有5000位候選人。
# 投票記錄最多有5000筆。時間範圍是 times[0]...10^9
# 可以在每筆投票後，更新目前完整得票數，並記錄「領先者」與時間
# In the case of a tie, the most recent vote (among tied candidates) wins.
# 意思是同票時，剛被投票的算領先
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        N = len(persons)
        table = [0]*N
        self.history = []
        maxVote = 0
        winner = -1
        for i in range(N):
            p = persons[i]
            t = times[i]
            table[p] += 1
            # print(table)
            if table[p]>=maxVote:
                maxVote = table[p]
                if winner!=p:
                    winner = p
                    self.history.append([t, p])
        # print(self.history)

    def q(self, t: int) -> int:
        H = len(self.history)
        left, right = 0, H
        while left<right:
            mid = (left+right)//2
            if self.history[mid][0]<=t:
                left = mid + 1
            else:
                right = mid
        return self.history[left-1][1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
