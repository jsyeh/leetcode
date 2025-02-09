# LeetCode 2364. Count Number of Bad Pairs
# 在 nums 陣列中，找出 i<j and j-i != nums[j] - nums[i] 的 bad 有幾組
# Hint 1:「反過來」思考：「相等」的 good 有幾組，減掉即可。
# Hint 2: j-i == nums[j]-nums[i] 移項，變 nums[i]-i == nums[j]-j
# 用 Counter 記錄 nums[i]-i 之前出現過幾次，再碰撞即可
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        counter = Counter()  # 記錄曾出現過的 i+nums[i]
        good = 0  # 請問 nums[i]-i == nums[j]-j 這麼巧的組合「有幾組」
        for i,num in enumerate(nums):  # 逐項「往右」處理
            good += counter[num-i]  # 若剛好「之前出現過」，出現幾次，就加幾次
            counter[num-i] += 1  # 隨手記錄 nums[i]-i 又出現1次，看幾後「會不會碰撞」
        N = len(nums)
        total = N*(N-1)//2  # 全部的 i<j 總共有幾組，用「直角三角形公式」算出來
        return total - good
