# 本來沒什麼頭緒，在想「是不是要排列組合」全部試過
# 但是看了 Discussion 裡，只有2個人留言，都覺得這題很糟
# 也就是只要印出 nums[0]/(nums[1]/nums[2]/...) 即可
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        N = len(nums)
        if N==1: return str(nums[0])
        if N==2: return str(nums[0]) + '/' + str(nums[1])
        ans = str(nums[0])+'/('+str(nums[1])
        for i in range(2, N):
            ans += '/' + str(nums[i])
        return ans + ')'
# case 2/92: [2] 也就是數字太少的話，例外處理
