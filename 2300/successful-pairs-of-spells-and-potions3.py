# LeetCode 2300. Successful Pairs of Spells and Potions
# 魔法師「施咒spell」配合「藥水potion」要乘起來
# spells[i] vs. potions[j] 希望乘起來後 >= success 值
# 但陣列很大, 不能暴力「全部都試乘一次」, 可 potions 先 sort 後, 再binary searcch 
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        N = len(potions)
        return [N - bisect_left(potions, success, key=lambda x:x*s) for s in spells]
