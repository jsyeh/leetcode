class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        M = len(accounts)
        N = len(accounts[0])

        ans = 0
        for i in range(M):
            total = 0
            for j in range(N):
                total = total + accounts[i][j]
            print(total)

            if total > ans:
                ans = total
        return ans
