class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        N = len(candies)
        ans = [False]*N
        max = 0
        for i in range(N):
            if candies[i] > max:
                max = candies[i]
        for i in range(N):
            if candies[i]+extraCandies >= max:
                ans[i] = True
        return ans
