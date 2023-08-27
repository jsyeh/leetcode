# 有多少 subseqnece 裡的 最大值+最小值 <=target 
# subsequence可不連續。可以排序後，每個最小值，binary search找到對應的最大值
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        N = len(nums)

        ans = 0
        for i in range(N):
            t2 = target - nums[i] # 要在 nums[i:N] 找到最大的值 t2
            left, right = i, N
            while left<right:
                mid = (left+right)//2
                if nums[mid] <= t2:
                    left = mid +1
                else:
                    right = mid
            # 最後找到的 left 會大一點點
            # print(nums[i:left], left-1, left-i)
            if left-i>0: # 有存在數字可以暴力排列組合的話
                ans += pow(2, left-i-1)  % 1000000007
        return ans % 1000000007
