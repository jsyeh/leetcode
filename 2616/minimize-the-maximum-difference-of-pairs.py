# 要找到 p pairs, 請問max difference的min是多少？
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0 : return 0
        N = len(nums)
        nums = sorted(nums) # 排序
        left = 0
        right = nums[N-1] - nums[0] # 最大距離差
        while left < right: # 想找出最適合的距離
            mid = int((left+right)/2) # 如果距離是mid
            # 有多少 possible pairs 在範圍內
            pp = 0 # possible pairs
            skip = -1
            for i in range(1,N):
                if i-1 == skip: continue # 避開
                dist = nums[i] - nums[i-1]
                if dist <= mid: # 如果在距離範圍內
                    pp += 1 # 多找到1組 pair
                    skip = i # 等下要避開這個 i
            if pp >= p: # 有超過題目要求的 p pairs
                right = mid
            else:
                left = mid + 1
        return left

