class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0] # 先假裝現在最好的是 nums[0] 當基礎
        ansCount = 1 # 有1個
        count = {}
        for num in nums:
            if num in count: # 之前有出現過
                count[num] += 1
                if count[num] > ansCount:
                    ansCount += 1
                    ans = num
            else: # 之前沒出現過
                count[num] = 1
        return ans
