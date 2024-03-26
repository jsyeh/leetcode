# 找出「第1個miss的正整數」
# 但因數字範圍很大，沒辦法開「超大陣列」去找數字。
# 可以用 hash set 來找
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums) # 先把 nums 轉成 set()
        for i in range(1,len(s)+2): # 從1開始，到 len(s)+1
            if i not in s: return i # missing 時，找到答案
