# 題目想問「如果最多只能抬升k次」，可以出現最多重覆的數字，會出現幾次？
# 我前一次在寫時，在找左邊界時，不小心使用 binary search 而耗費太多時間 3377ms
# 所以我決定用 two pointers 的方式重寫
# 註：Editorial 裡有更快的寫法，不過我不想用它的解法，想照自己的思緒想法來寫
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort() # 先排序小到大
        runSum = [0]*(N+1) # running sum
        for i in range(N): # 將差一格，nums[i] 對應 runSum[i+1]
            runSum[i+1] = runSum[i] + nums[i] 

        ans = 0
        left = 0 # 左邊界從0開始，想知道 nums[left]...nums[right] 是否補k即可一樣高
        for right in range(N): # sliding window, 先決定右邊界
            # 因 nums[i] 對應 runSum[i+1] 多了一格，所以有下面的範圍
            while runSum[right+1]-runSum[left]+k < nums[right]*(right-left+1):
                # 樓梯漸增的總合+能補k個小格子 不夠(<) 最右邊的高*寬的方形
                left += 1 # 只好左邊界往右縮，讓k照顧短一點的範圍
            # 離開迴圈時，便代表 runSum[left]...runSum[i] 剛好夠
            now = right - left + 1 # nums[left]...nums[right] 共有 i-left+1個數
            ans = max(ans, now)

        return ans
