# 找出「第1個miss的正整數」
# 但因數字範圍很大，沒辦法開「超大陣列」去找數字。
# 可以用 hash set 來找
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        i = 1
        while True:
            if i not in s: return i
            i += 1
