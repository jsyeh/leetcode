class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        length = [1]*N
        # length[i] 最後1位是 nums[i]時，最大 Wiggle Sequence length
        wiggle = [0]*N # 0 代表不是加+1 也不是減-1，可巧妙應用
        # wiggle[i] 對應最長 length[i] 發生時，與前面的差別是增加+1 還是減少-1
        ans = 1
        for i in range(1,N): # 現在處理的項
            for k in range(i-1, -1, -1): # i之前的項
                # print(k,i)
                if nums[i]-nums[k]>0 and wiggle[k]!=+1: # wiggle
                    if length[k]+1 > length[i]: # 而且更長
                        length[i] = length[k] + 1
                        wiggle[i] = +1
                if nums[i]-nums[k]<0 and wiggle[k]!=-1: # wiggle
                    if length[k]+1 > length[i]: # 而且更長
                        length[i] = length[k] + 1
                        wiggle[i] = -1
            if length[i]>ans:
                ans = length[i]
        # print(nums)
        # print(length)
        # print(wiggle)
        return ans

