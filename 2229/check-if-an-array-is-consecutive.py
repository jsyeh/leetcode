# LeetCode 2229. Check if an Array Is Consecutive
# 檢測 nums 是否是「一串連續的整數」
class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for i,c in enumerate(sorted(counter.keys())):
            if i!=0 and (c-1) not in counter:  # 不連續
                return False  # 失敗
            if counter[c] != 1: return False  # 出現不只一次，失敗
        return True
