# LeetCode 1760. Minimum Limit of Balls in a Bag
# 每個袋子裡有 nums[i] 個球，每次可「挑1袋」分成「2袋」, 希望做完 maxOperations 次後，每袋的球的上限「最少」是多少？ 
# 袋子裝太多，會搬不動。給你 maxOperations 個空袋子，儘量讓每袋的球儘量平均，「最重的那袋」要最輕，才提得動。
# 暴力法是依序「挑最大袋」再分袋，但數字有 10^9 要做太多次。改用「猜數字」常用的 binary search。直接「預測最大值」再檢查「能不能做到」
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort(reverse=True)  # 把數量「大到小」排好，方便 helper()函式找「前幾項」
        def helper(maxVal):  # 直接「預測最大值」再檢查「能不能做到」。return 「預測 maxVal」 對應的 operations 數
            operations = 0
            for num in nums:  # 每個數「大到小」依序處理
                if num > maxVal:  # 數字太大超過，就分袋。-1 扣掉「原本那袋」，便是「要多出來幾袋」
                    operations += num // maxVal + (num % maxVal > 0) - 1  # 整數袋數 + 有餘數再1袋 - 原本那袋
                else: break  # 數字不超過 maxVal 的話，就不用再「分袋」，提早結束
            return operations  # 這次 maxVal 對應的「分袋」operations 要幾次
        left, right = 1, 10**14  # 最粗糙的範圍：最小值是 1，最大值 10^5 個數，數最大有 10^9，乘起來是 10^14
        while left < right:  # binary search 的作法：用 while 迴圈
            mid = (left+right) // 2  # binary search 的作法：切一半
            operations = helper(mid)  # 這次需要「再分幾袋」？
            if operations > maxOperations:  # 要「分袋」的次數，超過題目範圍，就失敗
                left = mid + 1  # 那 mid 這個數不行，範圍要再大一點，left 變 mid + 1
            else:  # 沒超過題目範圍，很好，把現在的 mid 當成「右界」，再挑戰看看「能不能更低」
                right = mid
        return left

