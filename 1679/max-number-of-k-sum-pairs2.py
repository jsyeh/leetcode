# LeetCode 1679. Max Number of K-Sum Pairs
# nums 陣列裡，每次挑2個數（加起來是k）然後刪掉。可以做幾次？
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        ans = 0
        for c in list(counter.keys()):
            if c == k-c:
                ans += counter[c]//2
            else:
                d = min(counter[c], counter[k-c])
                ans += d
                counter[c] -= d
                counter[k-c] -= d
        return ans
