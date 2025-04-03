# LeetCode 2874. Maximum Value of an Ordered Triplet II
# 題目和 2873 非常相似：在陣列中找三個數 (nums[i]-nums[j]) * nums[k] 要最大
# 但是，不一樣的地方，是「陣列有10^5個數字」無法暴力用3層迴圈來完成。
# 若能找到 nums[i]-nums[j] 的最大值，那 nums[k]再乘最大值，便可更新答案
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        first = max(nums[0], nums[1])  # 找最大的「第一個數」
        second = nums[0] - nums[1]  # 對應 乘法的「左邊」部分，越大越好
        ans = max(0, second * nums[2])  # 對應 最後的答案
        # 上面先算出最基礎款的答案，下面再用迴圈「持續更新」
        for i in range(2, len(nums)):  # 利用「1個迴圈」更新3個數
            ans = max(ans, second * nums[i])  # 「倒過來」先更新答案
            second = max(second, first - nums[i])  # 再更新「左邊」
            first = max(first, nums[i])  # 最後更新「第一個數」
        return ans
