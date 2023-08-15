class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        N2 = N // 2 # N 的一半，也就是 
        # 為簡化程式，就浪費記憶體吧
        pos = [0]*N2
        neg = [0]*N2

        i0, i1 = 0, 0 # pos[i0] vs. neg[i1]
        for i in range(N):
            if nums[i] > 0:
                pos[i0] = nums[i]
                i0 += 1
            else:
                neg[i1] = nums[i]
                i1 += 1
        # 題目保證「正負各一半」，接下來要接起來
        for i in range(N2):
            nums[i*2+0] = pos[i]
            nums[i*2+1] = neg[i]
        return nums
