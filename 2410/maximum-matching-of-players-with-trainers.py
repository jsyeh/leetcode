# LeetCode 2410. Maximum Matching of Players With Trainers
# players[i] 對應「能力值」，trainers[j] 對應「訓練能力」
# 需要 players[i] <= trainers[j] 請問最多能找到幾組配對？
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()  # 小到大排好
        trainers.sort()  # 小到大排好
        ans = 0  # 能找到幾組
        M, N = len(players), len(trainers)
        i, j = 0, 0
        while i < M  and j < N:  # 逐一檢查配對
            while j < N and players[i] > trainers[j]:  # trainer 還不夠強
                j += 1  # 換更強的 trainer
            if j < N and players[i] <= trainers[j]:  # 現在 trainer 比 player 強
                ans += 1  # 找到一組配對
                j += 1  # 用掉這個 trainer
            i += 1  # 換下一個 player 
        return ans
