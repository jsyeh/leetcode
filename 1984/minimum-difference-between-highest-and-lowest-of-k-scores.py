# 要挑k位同學，怎麼讓它們的「最高分」-「最低分」是最小
# 也就是要「儘量挑分數相近」的同學
# 可以排序後，去看 nums[i] 及 nums[i+k-1] 的距離最小
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0] # 先放最大的差距
        for i in range(len(nums)-k+1):
            ans = min(ans, nums[i+k-1] - nums[i])
        return ans
