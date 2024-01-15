# 奇數放「奇數位置」，偶數放「偶數位置」
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N
        oddN, evenN = 0, 0 # 奇數、偶數 目前填入的數量
        for num in nums: # 逐一判斷
            if num%2==0: # 偶數，放偶數位置
                ans[evenN*2] = num
                evenN += 1
            else: # 奇數，放奇數位置
                ans[oddN*2+1] = num
                oddN += 1
        return ans
