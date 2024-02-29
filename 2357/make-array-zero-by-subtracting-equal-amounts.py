# 「挑個數值(比最小值小)」減掉全部的正數
# 問要做幾次, 才能把 nums 都變成0
# 其實等價於: 總共有幾個「不同」的正數
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        if nums[0]!=0: ans += 1 # 最小的數非零,就要再做1次

        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]: # 數字不同
                ans += 1 # 就要再多做1次
        return ans
