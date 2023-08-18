class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        runSum = [0]*(N+1) # running sum
        for i in range(N): # 將差一格，nums[i] 對應 runSum[i+1]
            runSum[i+1] = runSum[i] + nums[i] 

        ans = 0
        for i in range(N): # sliding window
            left, right = 0, i+1
            while left < right: # binary search 找 左邊界
                mid = (left+right)//2 # 現在要測試 mid
                full = nums[i]*(i+1-mid) # 全滿，即 nums[i]...nums[i] 長方形加總
                nowSum = runSum[i+1] - runSum[mid] # nums[mid]...nums[i] 漸增加總
                if full - nowSum > k: # 洞太大，差太多了
                    left = mid + 1
                else:
                    right = mid
            # 離開迴圈時，便代表 runSum[left]...runSum[i] 剛好夠
            now = i - left + 1 # nums[left]...nums[i] 共有 i-left+1個數
            if now > ans:
                ans = now

        return ans

