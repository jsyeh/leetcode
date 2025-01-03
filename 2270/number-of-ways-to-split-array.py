# LeetCode 2270. Number of Ways to Split Array
# 要將 nums 切成2段，左邊 i+1個加起來 >= 右邊剩下的。有幾種切法？
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        preSum = [0]  # 事先建立 prefix sum 資訊，可快速找到「某段和」
        for num in nums:  # preSum 會比 nums 多一項哦！
            preSum.append( preSum[-1] + num )
        total = preSum[-1]  # 最後一項 prefix sum 剛好是「全部總和」
        N = len(nums)
        ans = 0
        for i in range(1,N):  # preSum[i+1] 對應 nums[i] 所以歪一格，去試題目的範圍
            if preSum[i] >= total - preSum[i]:  # 左半 >= 右半
                ans += 1  # 找到 1種 合理的切法
        return ans
