# LeetCode 2134. Minimum Swaps to Group All 1's Together II
# 有一堆數字（繞成圓形），可交換「任2個位置」的數值。
# 要「交換」幾次，可把1放在一起。數字好多 10^5 不能暴力做。
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        counter = Counter(nums)  # 先統計「有幾個0、有幾個1」
        N, W = len(nums), counter[1] # 總共有N個數，裡面有W個1 (最後希望寬度W裡都是1)
        ones = Counter(nums[:W])[1] # 一開始，前面寬度W裡，有幾個1
        maxOnes = ones # 在寬度W裡，最多會有幾個1呢？目前是 ones 這麼多
        for i in range(N): # 開始滑動「寬度是W」的 sliding window
            if nums[i]==1: ones -= 1 # 左邊吐出1個1
            if nums[(i+W)%N]==1: ones += 1 # 右邊吃到1個1（圓形，所以用%N接到前面）
            maxOnes = max(maxOnes, ones) # 看寬度W範圍內，最多有幾個1
        return W - maxOnes  # 答案，就是「在W寬度範圍內」還差幾個1，就能「全部都變1」
