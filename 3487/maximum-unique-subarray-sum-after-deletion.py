# LeetCode 3487. Maximum Unique Subarray Sum After Deletion
# nums 陣列裡「可任意刪除」，讓陣列裡「每個數都不同」而且「加起來最大」
# 其實等價於「有幾個不同的正整數」再加起來即可
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        theMax = max(nums)  # 解決全負數問題：如果全部都是負數
        if theMax < 0: return theMax  # 就把最大的那一個負數當答案

        nums = set(nums)  # 變成 set 後，便「不會重覆」每個數都不同
        ans = 0  # 加起來的答案放ans
        for num in nums:  # 針對每一個「不會重覆」不同的數
            if num > 0:  # 如果是正數
                ans += num  # 就加起來
        return ans
# 什麼？ testcase 808/927 是 [-100] 因為「不能都刪掉」只好被迫「留下1個負數」
