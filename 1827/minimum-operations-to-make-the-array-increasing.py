# 希望array能嚴格增加，問「要加幾次」
# 因為只能加、不能減，所以從左到右巡，便能知道怎麼增加
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(1,N):
            if nums[i-1]>=nums[i]: # 右邊不夠大
                ans += nums[i-1]+1 - nums[i] # 要增加的次數
                nums[i] = nums[i-1]+1 # 變成更大的數
        return ans

