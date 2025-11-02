# LeetCode 3731. Find Missing Elements
# 預期 nums 裡會有很多數，排序後應該要是連續的。不過呢，缺了一些數，請找出來。
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()  # 先排序
        ans = []  # 答案放這裡
        for i in range(1, len(nums)):  # 排好序的數字，依序檢查
            if nums[i-1] + 1 != nums[i]:  # 相鄰兩數「中間有空隙」
                for k in range(nums[i-1]+1, nums[i]):  # 就用迴圈
                    ans.append(k)  # 把缺的補齊
        return ans
