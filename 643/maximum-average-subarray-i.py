# LeetCode 643. Maximum Average Subarray I
# nums 陣列「找長度k的小陣列」平均值最大。可用毛毛蟲來解。
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        now = total = sum(nums[:k])  # 先把前k項加好
        for i in range(k, len(nums)):  # 依序往右巡
            now = now + nums[i] - nums[i-k]  # 加、減
            total = max(total, now)  # 找 total 最大值
        return total / k  # 算出平均
