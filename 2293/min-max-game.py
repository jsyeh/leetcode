class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        p2 = 1 # 跳躍的距離 power of 2 將會慢慢長大 1 2 4 8 16
        N = len(nums)
        while p2<N: # 用來算距離的p2有沒有超過範圍N
            for i in range(0,N,p2*2): # 照著跳躍的距離走的迴圈
                if (i//p2//2)%2==0: # 偶數用 min
                    nums[i] = min(nums[i], nums[i+p2])
                else: # 奇數用 max
                    nums[i] = max(nums[i], nums[i+p2])
            p2 *= 2 # 跳躍的距離變成2倍
        return nums[0]
# case 20/96: [70,38,21,22]
