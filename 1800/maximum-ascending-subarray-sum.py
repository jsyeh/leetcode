# LeetCode 1800. Maximum Ascending Subarray Sum
# nums 陣列裡，某一段「漸增」加起來希望最多。
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = now = nums[0]  # 一開始，先放「第1筆」
        for i in range(1,len(nums)):  # 逐筆「與前項比較」
            if nums[i-1] < nums[i]:  # 若「漸增」
                now += nums[i]  # 這段「漸增」數列變大
            else:  # 若沒「漸增」，就是「新的一段」
                now = nums[i]  # 「新的一段」的開始
            ans = max(ans, now)  # 隨時更新「答案」
        return ans
