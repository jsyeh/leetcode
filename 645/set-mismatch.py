# 本來 nums 裡面，1-n 每個數字都剛好出現一次
# 但出了點錯，有個地方有問題：多1個數、少1個數。請把問題找出來。
# 直覺想法：從小到大排好，看多了什麼、漏了什麼。
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        ans = [-1, -1]
        found = 0 # 加速用，希望能提早結束
        if nums[0]!=1: # 漏了1
            ans[1] = 1
            found += 1
        if nums[N-1]!=N: # 漏了N
            ans[1] = N
            found += 1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]: # 相同
                ans[0] = nums[i] # 重覆的數
                found += 1
            if nums[i]==nums[i-1]+2: # 差2數
                ans[1] = nums[i]-1 # 漏的數
                found += 1
            if found==2: return ans # 湊齊2個數，就提早結束
        # 若漏的數字發生在最前面 or 最後面，另外處理
        return ans
        
