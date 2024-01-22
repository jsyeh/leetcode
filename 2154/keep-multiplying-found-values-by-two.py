# 奇怪的規則：把original乘2，直到nums裡找不到這個數
# ex. nums = [5,3,6,1,12] original = 3, 則 3,6,12,24時，找不到，ans=24
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums) # 把 list 轉成 set() 以加速「找有沒有在裡面」
        while original in nums: # 只要數字還有在裡面
            original *= 2 # 就照規則「乘2」
        return original # 離開迴圈後，就找到 ans 了
