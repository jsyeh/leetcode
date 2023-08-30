class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0

        for i in range(N-1,0,-1):
            if nums[i-1] > nums[i]: # 逆行
                b = nums[i-1] // nums[i] # 有幾瓶
                if nums[i-1] % nums[i] > 0:
                    b += 1 # 因為有餘數，多一瓶
                ans += b - 1
                nums[i-1] = nums[i-1] // b
        return ans
