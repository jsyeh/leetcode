# LeetCode 1679. Max Number of K-Sum Pairs
# nums 陣列裡，每次挑2個數（加起來是k）然後刪掉。可以做幾次？
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)  # 利用 Counter() 計數
        ans = 0
        for c in counter:
            ans += min(counter[c], counter[k-c])
        if k%2==0: # 如果是偶數，有可能「重覆」計算
            ans -= counter[k//2]  # 所以先減掉
            ans += counter[k//2]//2 * 2  # 再折半。因後面//2 所以再*2
        return ans//2
