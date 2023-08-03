# 傷腦筋的問題，到底是誰要replace成平方數？
# 後來看了 msk200 的解法，就把2種可能都做運算即可
# 另外，我在做 DP 時，都會建 table[i] 不過 msk200 是直接用2個變數來存就好，比較厲害
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        N = len(nums)
        table1 = [0]*N # 還沒有任何平方數
        table2 = [0]*N # 已有1個平方數了

        table1[0] = nums[0]
        table2[0] = nums[0] * nums[0]
        ans = max(table1[0], table2[0])
        for i in range(1,N):
            table1[i] = table1[i-1] + nums[i]
            table2[i] = max(table2[i-1]+nums[i], table1[i-1]+nums[i]*nums[i])
            if nums[i] > table1[i]: table1[i] = nums[i] # nums[i]是新的開始
            if nums[i]*nums[i] > table2[i]: table2[i] = nums[i] * nums[i]
            # 兩種可能：之前就有平方數 vs. 現在 nums[i] 變平方數
            if table1[i]>ans: ans = table1[i]
            if table2[i]>ans: ans = table2[i]
        # print(table1)
        # print(table2)
        return ans
# case 56/57: [-44] 漏了在第1筆就更新 ans 
