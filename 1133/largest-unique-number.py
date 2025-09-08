# LeetCode 1133. Largest Unique Number
# nums 裡，最大的「只出現一次」的數字
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True) # 先由大到小排好
        counter = Counter(nums) # 全部統計一次
        for num in counter: # 針對每個數字，查看其統計結果
            if counter[num]==1: return num # 由大到小，找到「只出現一次」的數
        return -1 # 但前面都沒找到的話，就 return -1
