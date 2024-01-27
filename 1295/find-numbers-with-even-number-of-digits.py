# 想問 nums[i] 有幾個是even位數，像2位數、4位數等
# 想到可轉成 str()後，用 len()即可算出來
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums: # 每次挑個數字
            # 先轉成字串，再看它的長度「是不是2的倍數」
            if len(str(num))%2==0: ans += 1
        return ans
