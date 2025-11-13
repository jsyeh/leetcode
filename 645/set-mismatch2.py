# LeetCode 645. Set Mismatch
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0]*2
        N = len(nums)
        counter = Counter(nums)
        for num in range(1,N+1):
            if counter[num]==2:
                ans[0] = num
            if counter[num]==0:
                ans[1] = num
        return ans
