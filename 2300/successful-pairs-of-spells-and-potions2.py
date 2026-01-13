# LeetCode 2300. Successful Pairs of Spells and Potions
# 魔法師「施咒spell」配合「藥水potion」要乘起來
# spells[i] vs. potions[j] 希望乘起來後 >= success 值
# 但陣列很大, 不能暴力「全部都試乘一次」, 可 potions 先 sort 後, 再binary searcch 
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # 先把「藥水」小到大排序，以方便 binary search
        N = len(potions)
        ans = []  # ans[i] 對應題目 pairs[i] 也就是 spells[i] 能配幾種「藥水」
        for spell in spells:  # 逐項檢查
            now = bisect_left(potions, success/spell )
            ans.append(N - now)  # 超過的這些，都是「達到標準」的藥水
        return ans
