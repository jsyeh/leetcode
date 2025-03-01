# LeetCode 2460. Apply Operations to an Array
# 如果 nums[i] == nums[i+1] 就把 nums[i] *= 2 並把 nums[i+1] = 0
# 巡一輪後，再把 0 移到 nums 右邊，就完成了！ 
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N  # 先放一堆 0
        k = 0  # 將放（非零項）的 nums[k]
        for i in range(N):  # 巡一輪
            if i != N-1 and nums[i] == nums[i+1]:  # 如果相鄰項相同
                nums[i] *= 2  # 放兩倍
                nums[i+1] = 0
            if nums[i] != 0:  # 有數字（非零）
                ans[k] = nums[i]  # 往左移
                k += 1  # 換下一格
        return ans
