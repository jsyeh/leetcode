# LeetCode 2300. Successful Pairs of Spells and Potions
# 魔法師「施咒spell」配合「藥水potion」要乘起來
# spells[i] vs. potions[j] 希望乘起來後 >= success 值
# 但陣列很大, 不能暴力「全部都試乘一次」, 可 potions 先 sort 後, 再binary searcch 
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        M, N = len(spells), len(potions)
        potions.sort()  # 先排序好, 等待 spells[i] 來乘
        ans = [0] * M  # 準備好答案「對應 spells[i] * ?? 可成功」
        for i in range(M):  # 針對「每一種 spells[i] 咒語」
            energy = success / spells[i]  # 需要的藥水能量
            ans[i] = N - bisect_left(potions, energy)  # 有哪些藥水,達到標準
        return ans
