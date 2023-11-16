class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums) # 有N個數
        # nums 裡會有 0...N 裡面少1個
        used = [0]*(N+1) # 一開始都還沒用過
        for i in range(N): # 把 nums[i] 巡一輪
            used[ nums[i] ] += 1 # 對應項標示用過

        for i in range(N+1): # 再針對 used[i] 巡一輪
            if used[i] == 0: # 若沒過用
                return i # 就是缺的那個數
