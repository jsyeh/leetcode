class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in range(len(accounts)):
            total = 0
            for aij in accounts[i]:
                total += aij

            if total > ans:
                ans = total
        return ans
