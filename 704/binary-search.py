class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left, right = 0, N
        while left<right:
            mid = (left+right) // 2
            if nums[mid]<target:
                left = mid+1
            else:
                right = mid
        
        if left >= N: return -1

        if nums[left]==target:
            return left
        else:
            return -1
# case 15/47: [-1,0,3,5,9,12] 13 答案會超過範圍
