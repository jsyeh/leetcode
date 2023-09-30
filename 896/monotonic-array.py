class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dir = 0 # 方向分成: 0:平，+1往上，-1往下
        for i in range(1,len(nums)): # 要少1格
            diff = nums[i] - nums[i-1] # 現在的方向
            if diff>0: # 現在是正的
                if dir<0: # 但之前是負的
                    return False # 就錯了
                dir = +1 # 不管如何，記下現在正的方向
            if diff<0: # 現在是負的
                if dir>0: # 但之前是正的
                    return False # 就錯了
                dir = -1 # 不管如何，記下現在負的方向
        # 經過全部檢查，都沒有錯的話，就是正確的囉
        return True
