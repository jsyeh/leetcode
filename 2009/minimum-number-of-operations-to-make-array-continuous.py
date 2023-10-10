# 要改幾個數字，才能讓數字的集合的變成能連續的數字
# 最差的狀況，就是改 N-1 個數字
# 問題在，要挑哪個範圍來放數字？照著Editorial的解法：看有哪些是好的
# 先排序、去除重覆，之後把每個輪流當left,再用binary search看有幾個好的。減完後，便是答案
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums) # 一開始全部數字的數目
        nums = sorted(set(nums)) # 去除重覆、排序好

        ans = N - 1
        N2 = len(nums) # 去除重覆後的數目
        for i in range(len(nums)):
            start = nums[i] # 第i個是開始的數
            left, right = i, N2
            while left<right: # binary search 找剛好的範圍
                mid = (left+right)//2
                if nums[mid]<=start+N-1:
                    left = mid + 1
                else:
                    right = mid
            # binary search 後，left是找到的結果
            # i 開始位置，left 最適合的「右邊界」位置，長度是left-i
            # print(start, left-i)
            if N-(left-i)<ans:
                ans = N-(left-i)
        return ans
