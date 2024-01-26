# 很多 arrays 找交集。用 set() 就搞定了
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        set1 = set(nums[0])
        for i in range(1,len(nums)): # 後面的 set
            set1 = set1 & set(nums[i])
        return sorted(list(set1)) # 要照數字大小排好
# case 47/151: [[7,34,45,10,12,27,13],[27,21,45,10,12,13]]
