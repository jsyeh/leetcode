# LeetCode 3010. Divide an Array Into Subarrays With Minimum Cost I
# 將 nums 切成 3 段，希望「這3段」的「第1個數」加起來最小。
# 一定用到 nums[0]，剩下的2個數，是「剩下的數裡面」最小的2個數
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # 方法一：先拆成2個 part1 是第1個數，part2 是剩下的數排好
        part1, part2 = nums[0], sorted(nums[1:])
        return part1 + part2[0] + part2[1]  # 把最小的2個數加進來

        # 方法二：（模仿方法一）只是把程式擠成1行
        return nums[0] + sum(sorted(nums[1:])[:2])

        # 方法三：用1層for迴圈，慢慢找出
        min1 = min2 = inf
        for i in range(1,len(nums)):
            if nums[i]<=min1:
                min1, min2 = nums[i], min1
            elif nums[i]<min2:
                min2 = nums[i]
        return nums[0] + min1 + min2

        # 方法四：利用 heap 資料結構，挑「剩下的數」裡最先跳出的2個數
        first, nums[0] = nums[0], inf  # 改塞入 inf 避免再度被用
        heapify(nums)
        return first + heappop(nums) + heappop(nums)
