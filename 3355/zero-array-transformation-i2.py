# LeetCode 3355. Zero Array Transformation I
# 照著 queries 每次的範圍 [left, right] 將 nums[left]...nums[right] 減1
# 問最後「nums 是否全變成0」。因數字很多，不能真的「減1」，可利用「增減量」來加速
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        diff = [0] * (N+1)  # 要多1格，供最右邊界使用
        for left, right in queries:  # 逐一操作
            diff[left] -= 1  # 從 left 開始，會減1
            diff[right+1] += 1  # 到 right 之後，要加1（恢復原狀
        diffSum = 0  # 用來累積 diff 的量
        for i in range(N):
            diffSum += diff[i]  # 目前的 diff 累積量
            nums[i] += diffSum  # 用「diff 累積量」調整 nums[i]
            if nums[i] > 0: return False  # 只要還有剩，「扣得不夠」，就失敗
        return True  # 都沒有失敗，就是成功
