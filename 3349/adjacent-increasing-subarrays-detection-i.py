# LeetCode 3349. Adjacent Increasing Subarrays Detection I
# nums 陣列裡，是否有2個相鄰的（長度都為k的）陣列，裡面都是遞增
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # 想到「利用正、反迴圈」，數「左到右遞增」及「右到左遞減」，記下「累積長度」
        N = len(nums)
        left, right = [1] * N, [1] * N
        for i in range(1,N):
            if nums[i-1] < nums[i]:  # 符合「遞增」
                left[i] = left[i-1] + 1  # 就比前一項 + 1
            if nums[N-i] > nums[N-i-1]:  # 符合「反過來」的「遞減」
                right[N-i-1] = right[N-i] + 1  # 就比右邊項 + 1

        for i in range(N-1):  # 最後巡一輪，看「左方」及「右方」是否都夠長
            if left[i]>=k and right[i+1]>=k:  # 長度都夠長
                return True  # 代表左右「2個相鄰、長度為k的陣列」符合條件
        return False  # 沒找到符合條件，就失敗
