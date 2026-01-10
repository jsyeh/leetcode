# LeetCode 649. Dota2 Senate
# Dota2 兩個陣營 「Radiant / 聖輝」和「Dire / 魔魘」照 senate 字串的順序出現
# 從左到右輪，輪到的人，可把「後面任一個敵對陣營」除掉。
# 巡完一輪，繞到前面繼續，直到全部字母都相同，問最後「哪個陣營」得勝
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)  # 利用 double-ended queue 模擬
        counter = Counter(senate)  # 統計兩陣營的人數
        banList = Counter()  # 決定刪除的人
        while counter['R']>0 and counter['D']>0:  # 兩陣營「都還有人」
            now = queue.popleft()  # 現在出場的是 now
            if banList[now] > 0:  # 有被 ban 掉
                banList[now] -= 1  # 用掉1個 ban 的名額
                counter[now] -= 1  # 陣營少1人
                continue  # 繼續下一輪
            if now=='R': banList['D'] += 1  # 沒被 ban，就可反向 ban 掉對方陣營
            else: banList['R'] += 1
            queue.append(now)  # 再到「最後面」排隊
        if counter['R'] > 0: return 'Radiant'
        else: return 'Dire'
