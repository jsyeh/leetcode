# LeetCode 494. Target Sum
# nums[i] 前面可放「正號」或「負號」，希望湊出target結果，有幾種湊法。
# 不能直接暴力試 2^1000 種可能。但可用 Dynamic Programming 找結果
# 使用 Top-Down DP 的方法，函式呼叫函式，把問題解掉。
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        @cache  # 這個 @cache 很重要，具有 memory 功能，節省時間
        def helper(i, total):  # 發明 helper()函式，參數是「加到第i筆」及「當時的total值」
            if i==N and total==target: return 1  # 走到最後，找到1種解法
            if i==N and total!=target: return 0  # 失敗
            # 下面有2種可能，一種是「減」、一種是「加」，都再去問答案
            return helper(i+1, total-nums[i]) + helper(i+1, total+nums[i])
        return helper(0, 0)
