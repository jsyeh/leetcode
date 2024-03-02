# 「要花多少時間」才能在比賽中得勝。
# 一開始能量initialEnergy、一開始經驗值initialExperience
# len(energy) == len(experience) 是你要面對的 n 個對手，它們的能量、經驗值
# 照順序，每打完一場，會扣 energy, 並增加 experience
# 每次比賽前，等 x 小時，可用來增加 energy 或 experience
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans = 0 # 要花多少時間
        for i in range(len(energy)): # 逐一對付對手
            if energy[i] >= initialEnergy: # 能量不夠多
                ans += energy[i] - initialEnergy + 1 # 要多增加這麼多時間
                initialEnergy = energy[i] + 1 # 能量要更多
            if experience[i] >= initialExperience: # 經驗值不夠多
                ans += experience[i] - initialExperience + 1 # 要多增加這麼多時間
                initialExperience = experience[i] + 1 # 經驗值變夠多
            initialEnergy -= energy[i] # 比賽後，減少能量值
            initialExperience += experience[i] # 比賽後，增加經驗值
        return ans # 總共要花的時間
