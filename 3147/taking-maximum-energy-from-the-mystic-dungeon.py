# LeetCode 3147. Taking Maximum Energy From the Mystic Dungeon
# n 個魔法師可以給你 energy[i] （如果負的，表示「反過來」吸走你的能量）
# 魔法師 i 給你 energy[i] 後，你會瞬移到 魔法師 i+k 前面，得到 energy[i+k]
# 你可決定「一開始站在誰的前面」進行，希望得到 maximum Energy
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = -inf  # 最多能得到的能量，預設值「最小」
        N = len(energy)  # 有 N 個魔法師
        for end in range(N-1, N-1-k, -1):  # 反過來，決定「最後1位」是誰
            now = 0  # 這輪能得到的「累積能量」，從「後面」往前「累積」
            for i in range(end, -1, -k):  # 從「最後面」往前，每次跳 k 格
                now += energy[i]  # 累積得到能量值
                ans = max(ans, now)  # 隨時更新 ans 值
        return ans
