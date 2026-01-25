# LeetCode 3819. Rotate Non Negative Elements
class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        nums2 = []
        for num in nums:
            if num>=0: nums2.append(num)
        if len(nums2)>0: k = k % len(nums2)
        j = k
        for i in range(len(nums)):
            if nums[i]>=0: 
                nums[i] = nums2[j%len(nums2)]
                j += 1
        return nums
