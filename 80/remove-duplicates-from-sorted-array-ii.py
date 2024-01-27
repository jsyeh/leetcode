# 最多「只能重覆2次」，要把 nums[i] 直接改，再回傳總數
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        i, k = 0, 0 # 從1開始，與前項相比
        repeat = 0 # 0:沒重覆，1:重覆1次（2個），2:重覆2次（3個）
        while i<N:
            if i==0 or nums[i-1]!=nums[i]: 
                repeat = 0 # 沒有重覆
            else: repeat += 1 # 有重覆

            if repeat<2: # 重覆在容許範圍內
                nums[k] = nums[i] # 照搬
                k += 1
                # 意思是，重覆兩個以上，就不搬
            i += 1
        return k # 順利搬了幾個數字
