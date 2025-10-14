# LeetCode 3349. Adjacent Increasing Subarrays Detection I
# nums 陣列裡，是否有2個相鄰的（長度都為k的）陣列，裡面都是遞增
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # 剛想到「只要用1個陣列」「累積長度」即可
        N = len(nums)
        combo = [1] * N
        for i in range(1,N):
            if nums[i-1] < nums[i]:  # 符合「遞增」
                combo[i] = combo[i-1] + 1  # 就比前一項 + 1
        for i in range(N-k):  # 最後巡一輪，看「2個相鄰」長度為k的陣列是夠長
            if combo[i]>=k and combo[i+k]>=k:  # 「2個長度都是k的相鄰陣列」
                return True  # 代表左右「2個相鄰、長度為k的陣列」符合條件
        return False  # 沒找到符合條件，就失敗
