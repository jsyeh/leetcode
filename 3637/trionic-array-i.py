# LeetCode 3637. Trionic Array I
# 判斷 nums 是不是「升、降、升」陣列
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if nums[0]>=nums[1]: return False  # 開始方向錯
            
        state = 1  # 1:升 2:降 3:升
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]: return False  # 不能相等
            if state==1 and nums[i-1] > nums[i]:
                state = 2  # 從狀態1（升）變狀態2（降）
            elif state==2 and nums[i-1] < nums[i]:
                state = 3  # 從狀態2（降）變狀態3（升）
            elif state==3 and nums[i-1] > nums[i]:
                return False  # 沒有狀態4哦！失敗了
        return state==3  # 順利走完
