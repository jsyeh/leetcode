# 兩兩對決比賽 [勝,負] 
# 回傳 ans 其中 ans[0] 是「沒輸過的人」，ans[1]是「只輸1場」
# 想知道有哪些人比賽過，可用 set()來收集。另用字典記「誰輸過」
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        lose = defaultdict(int)
        for winner,loser in matches:
            players.add(winner) # 多個人
            players.add(loser) # 多個人
            lose[loser] += 1 # 輸的人，多一場敗績
        # 統計完後，逐個去查「有沒有敗績」
        lose0 = [] # 都沒有輸過
        lose1 = [] # 只輸1場
        for player in players:
            if lose[player]==0: lose0.append(player)
            elif lose[player]==1: lose1.append(player)
        return [sorted(lose0), sorted(lose1)]
# case 27/127: 數字很多，需要將結果排序
