# LeetCode 838. Push Dominoes
# 推「骨牌」：有 n 個骨牌排成一線, 每個骨牌可「往右推 or 往左推」
# 每隔一秒, 鄰近的1個骨牌會受影響而倒下。若剛好「左右鄰居都向你倒」就會保持中立/站立。
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        N = len(dominoes)
        force = [0] * N
        energy = 0
        for i, c in enumerate(dominoes):  # 往右巡
            if c=='R': energy = N  # 遇到往右推，能量滿檔
            elif c=='L': energy = 0  # 遇到逆向推，能量歸零
            elif energy>0: energy -= 1  # 其他時候，能量慢慢減少
            force[i] += energy  # 往右的能量
        energy = 0
        for i in range(N-1, -1, -1):  # 往左巡
            c = dominoes[i]
            if c=='L': energy = N  # 順著推，能量滿檔
            elif c=='R': energy = 0  # 逆向推，能量歸零
            elif energy>0: energy -= 1  # 能量慢慢減少
            force[i] -= energy  # 往左的能量（負）
            # 接下來算帳，看能量是多少
            if force[i]>0: dominoes[i] = 'R'
            if force[i]<0: dominoes[i] = 'L'
            if force[i]==0: dominoes[i] = '.'
        return ''.join(dominoes)
