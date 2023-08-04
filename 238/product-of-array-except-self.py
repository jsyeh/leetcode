# 題目希望 O(n) 而且不用除法。那就不應該「全部乘來/nums[i]」
# 還好題目有暗示，就用 prefix 及 suffix 來做吧
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [0]*N # prefix[i] 表示 nums[0] * ... * nums[i]
        suffix = [0]*N # suffix[i] 表示 nums[i] * ... * nums[N-1]

        prefix[0] = nums[0]
        suffix[N-1] = nums[N-1]
        for i in range(1,N):
            prefix[i] = nums[i] * prefix[i-1] # 往右更新
            suffix[N-1-i] = nums[N-1-i] * suffix[N-1-i+1] # 往左更新
        # print(prefix)
        # print(suffix)

        ans = [0]*N
        ans[0] = suffix[1]
        ans[N-1] = prefix[N-2]
        for i in range(1,N-1):
            ans[i] = prefix[i-1] * suffix[i+1] # 就避開了 nums[i]
        return ans
