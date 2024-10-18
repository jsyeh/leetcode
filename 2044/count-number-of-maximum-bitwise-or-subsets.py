# LeetCode 2044. Count Number of Maximum Bitwise-OR Subsets
# 先知道「bitwise-OR 的最大值」target，再問「有多少種subset」剛好也是這個值
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0  # bitwise-OR 的最大值，是這次的目標
        for num in nums:
            target |= num  # 全部都 OR 起來b
        # 最多有16個數，可用暴力法試出來
        N = len(nums)  # N 個數，就對應 N-bits
        ans = 0
        for mask in range(2**N):  # 排列組合共2**N種，對應 bit mask
            now = 0  # 這個 mask 對應的 nums bitwise OR 結尾
            for i in range(N):  # 每個bit逐一檢查
                if mask & 2**i:  # 第 i-th bit 有用到
                    now |= nums[i]  # 就用 nums[i] 這個數
            if target==now: ans+=1  # 很好，符合目標，是一組解
        return ans
        
