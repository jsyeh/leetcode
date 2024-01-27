# nums[i] 數字可增加 k 次，問「乘起來」最大值
# 因 10^5 個數，且 k 最大 10^5, 所以無法暴力試
# 參考 Solutions 裡 bitmasker 的解釋，「把最小的增大」可乘出最佳解
# 所以可建 heap，把最小的加大
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums) # 轉成 heap
        while k>0: # 只要k還能操作
            # 就取出「最小」的數，+1後，塞回 heap
            heappush(nums, heappop(nums) + 1)
            k -= 1
        ans = 1 # 再把數字逐個乘起來
        MOD = 10**9+7
        for num in nums:
            ans = ans * num % MOD
        return ans
# case 8/73: [24,5,64,53,26,38] k = 54
# 乘很大時，要記得 % (10**9+7)
