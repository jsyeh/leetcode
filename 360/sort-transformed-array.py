# 題目很簡單, 照著 f(x) = a*x*x + b*x + c 的公式轉換, 再排序後, 便是答案
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        N = len(nums)
        ans = [0]*N
        for i in range(N):
            ans[i] = a*nums[i]*nums[i] + b*nums[i] + c
        ans.sort()
        return ans
