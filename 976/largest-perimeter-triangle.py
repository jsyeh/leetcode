# 如果能組出最大周長的三角形，把周長（3個邊長加起來）return
# 三角形3個邊的特質：a,b,c
# a+b>c 兩邊相加，大於第3邊
# 但無法暴力試 10^4的3次方，就超過了。所以不能這樣做。
# 技巧：就從大到小，反過來查看
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        for i in range(len(nums)-1,1,-1):
            # 就只看最大的連續3個邊，因為不成三角形的話，跳到更小也不行
            if nums[i]<nums[i-1]+nums[i-2]:
                return nums[i]+nums[i-1]+nums[i-2]

        return 0
