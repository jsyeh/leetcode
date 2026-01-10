# LeetCode 649. Dota2 Senate
# Dota2 兩個陣營 「Radiant / 聖輝」和「Dire / 魔魘」照 senate 字串的順序出現
# 從左到右輪，輪到的人，可把「後面任一個敵對陣營」除掉。
# 巡完一輪，繞到前面繼續，直到全部字母都相同，問最後「哪個陣營」得勝
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        counter = Counter(senate)
        R, D = counter['R'], counter['D']
        banR = banD = 0
        while queue:
            now = queue.popleft()
            if now=='R': 
                if banR==0:  # 沒有被 ban
                    banD += 1  # 就 ban 對方
                    D -= 1  # 對方少1人
                    queue.append(now)  # 自己再回去排隊
                else: banR -= 1
            else:
                if banD==0: 
                    banR += 1
                    R -= 1
                    queue.append(now)
                else: banD -= 1
            if R<=0: return 'Dire'
            if D<=0: return 'Radiant'
