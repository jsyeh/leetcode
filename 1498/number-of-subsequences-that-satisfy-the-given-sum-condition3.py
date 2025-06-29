# LeetCode 1498. Number of Subsequences That Satisfy the Given Sum Condition
# nums 陣列能挑幾種 subsequence 符合 max + min <= target
# 可針對排序 array 進行 binary search 「某個小的」有「哪些大的」可配對，取中間排列組合
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()  # 可針對排序 array 進行 binary search
        N = len(nums)
        MOD = 10**9+7  # 因答案會很大, 需要取餘數
        ans = 0
        for i in range(N):  # 先挑小的
            target2 = target - nums[i]  # 對應的最大值
            if target2 < nums[i]: break  # 大小開始倒過來, 就不用再算了
            bigI = bisect_right(nums, target2, i, N)  # 找出對應大的位置
            # 在 nums 裡, 找到 target2 適合插入的右邊界。這樣中間的部分, 就是缺的
            if i < bigI:  # 左右的邊界大小正確, 便能進行排列組合
                ans += pow(2, bigI-i-1)  # 中間 bigI-i-1 個數「能取、能不取」是2的次方
                ans %= MOD  # 隨時取餘數
        return ans
