class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len = 0
        for n in nums:
            if n != val:
                nums[len] = n
                len+=1
        return len
