# LeetCode 448. Find All Numbers Disappeared in an Array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        numSet = set(nums)
        N = len(nums)
        for i in range(1,N+1):
            if i not in numSet:
                ans.append(i)
        return ans
