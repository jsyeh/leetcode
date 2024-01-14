# 想找出總共有多少 pair nums[i] nums[j] 的距離==k
# 只有200個數，可用暴力法、全部去試
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):
            for j in range(i+1,N):
                if abs(nums[i]-nums[j])==k:
                    ans +=1
        return ans
