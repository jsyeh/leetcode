# 找出兩兩之間的 Hamming Distance, 再全部加起來
# 共有 10^4個數，暴力排列組合（再加起來）就太慢了。
# 觀察規則，與排列組合公式有關 1100 就 ones * zeros 即答案
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ones = [0]*32 # ones[i] 用來統計i-bit有幾個 1
        zeros = [0]*32 # zeros[i] 用來統計i-bit有幾個 0
        N = len(nums)
        ans = 0
        for i in range(32): # 第i-bit
            for k in range(N): # nums[k]
                if nums[k]%2==0: zeros[i] += 1
                else: ones[i] += 1
                nums[k] //= 2
            # 統計距離 ones[i] * zeros[i]
            ans += ones[i] * zeros[i]
        return ans
