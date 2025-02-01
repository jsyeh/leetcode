# LeetCode 3151. Special Array I
# 希望 nums 裡，每2個相鄰的數 parity 都不同（奇數、偶數交錯）
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # 突然想到，就相鄰2數加起來，一定要是奇數
        for i in range(len(nums)-1):
            if (nums[i]+nums[i+1])%2 == 0: return False  # 所以「偶數」就失敗
        # 都沒有失敗，就是成功
        return True
