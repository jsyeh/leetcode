# LeetCode 2491. Divide Players Into Teams of Equal Skill
# 將N個數字，2個一組，分成 N/2 個團隊，每個團隊有均衡skill組合（加起來相同）。
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N = len(skill)  # 先知道有幾個人，將會分成 N//2 個團隊
        total = sum(skill)  # skill[i] 點數 加起來是 total 點
        average = total // (N//2)  # 每個團隊「平均」分到的點數
        if total%(N//2) != 0:  # 如果「點數」無法均分，就會失敗
            return -1
        skill.sort()  # 點數「從小到大」分好。左邊小的 配上 右邊大的

        ans = 0
        for i in range(N//2):
            if skill[i] + skill[N-1-i] != average:
                return -1  # 加起來的點數，不是每個團隊「平均」分到的點數，失敗
            ans += skill[i] * skill[N-1-i]  # 答案是「乘積」再加起來
        return ans  # 順利組隊完，回傳「乘積」再加起來的答案
