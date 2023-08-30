# 可把數字拆換成2個數 ex. 6 拆成 2+4
# 目標是讓 array變成慢慢增加
# 已經排好的就不用動，只要把沒排好的數拆解
# Editorial 裡介紹的方法，是把「逆序」的大數字拆解，且最小值要儘量大，最好是 nums[i]-1
# for迴圈則是從右到左
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(N-1,0,-1):
            if nums[i-1] > nums[i]: # 逆序
                # 讓數字nums[i-1]變 <= nums[i]
                if nums[i-1]%nums[i] == 0: # 整除
                    e = nums[i-1]//nums[i] # 拆成這麼多個
                    ans += e - 1 # 要切 e-1 刀
                    nums[i-1] = nums[i]
                else: # 有餘數
                    e = nums[i-1]//nums[i] + 1 # 拆成這麼多個
                    ans +=  e - 1 # 要切 e-1 刀
                    nums[i-1] = nums[i-1] // e # 平均每份有這麼多，餘數平均分給大的數
        return ans
                
