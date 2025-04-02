# LeetCode 2873. Maximum Value of an Ordered Triplet I
# 針對所有的 i < j < k，計算 (nums[i]-nums[j]) * nums[k] 的「最大值」
# nums 裡只有 100 個數，用暴力三層 for 迴圈，就可以做出來了！
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        for i in range(N):  # 左邊的 i
            for j in range(i+1, N):  # 中間的 j （在i的右邊）
                for k in range(j+1, N):  # 右邊的 k（在j的右邊）
                    now = (nums[i]-nums[j]) * nums[k]  # 現在算出來的值
                    ans = max(ans, now)  # 更新「最大值」
        return ans
