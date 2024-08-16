# LeetCode 134. Gas Station
# 圓形的路上有許多加油站，gas[i]是能加的油量，cost[i]是從i到i+1加油站需花費的油量
# 問你要從「哪個」加油站出發，油量能成功繞完一圈。（無法成功繞一圈，return -1）
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        now, total = 0, 0  # 現在的油量、總共累積的油量
        ansI = 0  # 答案的 index
        # 能加的油量 - 到下一站的耗油量，代表「能多出來的油」
        # diff = [(gas[i]-cost[i]) for i in range(N)]
        for i in range(N):
            total += gas[i] - cost[i]  # 加 gas[i]，減 cost[i]
            now += gas[i] - cost[i]  # 油箱現在的油量
            if now<0:  # 不幸油箱耗盡，到不了下一站。只好改從下一站出發
                ansI = (i+1) % N  # 其實不需要 %N 因 ansI = 0 早就試過了
                now = 0  # 從新的加油站「重新開始」
        if total < 0: return -1 # 真慘，累積油量根本就不夠，不用玩了
        return ansI
