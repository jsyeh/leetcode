# 有些數字可以變成負的，做k次後，加起來「最大值」是多少
# 先「小到大」排序。再把前k項中，負的都先變正的。
# 不夠k項時，再奇偶重覆「把最小的」一直變負數
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort() # 先由小到大排好
        nearZero = nums[0]
        N = len(nums)
        for i in range(k): # 想取前k項
            if i<N and nums[i]<0: # 因 i 可能超過 nums，所以要保護
                nums[i] = -nums[i] # 先把負的變正的
                nearZero = nums[i] # 可能最接近0的數
            else: # 一旦「都沒有負的」時，再把「目前前最小的數」看奇偶來決定
                if i<N: # 如果沒有超過範圍，才能挑「下個數」看是否 nearZero
                    nearZero = min(nearZero, nums[i])
                if (k-i)%2==0: return sum(nums) # 偶數：不動
                else: return sum(nums) - nearZero*2 # 奇數：把最接近0的數變負，即扣2次
        return sum(nums) # 如果做完k次都還沒有 return，那簡單sum()即可
# case 78/82: [-4,-2,-3] k=4 竟然 k比 len(nums)還大，所以要保護
