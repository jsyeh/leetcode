# LeetCode 2491. Divide Players Into Teams of Equal Skill
# 將N個數字，2個一組，分成 N/2 個團隊，每個團隊有均衡skill組合（加起來相同）。
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()  # 點數「從小到大」分好。左邊小的 配上 右邊大的
        target = skill[0] + skill[-1]  # 最小+最大，當「每隊的目標」
        ans = 0
        for i in range(len(skill)//2):
            if skill[i] + skill[-1-i] != target:
                return -1  # 加起來的點數，不是「每隊的目標」分到的點數，失敗
            ans += skill[i] * skill[-1-i]  # 答案是「乘積」再加起來
        return ans  # 順利組隊完，回傳「乘積」再加起來的答案
