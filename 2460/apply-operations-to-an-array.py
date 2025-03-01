# LeetCode 2460. Apply Operations to an Array
# 如果 nums[i] == nums[i+1] 就把 nums[i] *= 2 並把 nums[i+1] = 0
# 巡一輪後，再把 0 移到 nums 右邊，就完成了！ 先照題目作法，很囉嗦的實作
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):  # 巡一輪
            if nums[i] == nums[i+1]:  # 如果相鄰項相同
                nums[i] *= 2  # 左邊 *2
                nums[i+1] = 0  # 右邊 變0
        k = 0  # 目前有幾個 non zero 項，開始搬動
        for i in range(len(nums)):  # 再巡一次，把「數字」往左移
            if nums[i]!=0:  # 有數字（非零）
                nums[k] = nums[i]  # 往左移
                k += 1  # nums[k] 有放值，就改變 index k 
        for i in range(k, len(nums)):  # 右邊剩下的項
            nums[i] = 0  # 都放零
        return nums
