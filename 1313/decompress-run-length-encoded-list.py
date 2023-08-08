class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        N = 0 # 事先計算結果ans的長度
        for i in range(0, len(nums), 2):
            N += nums[i+0] # 也就是把每個小長度都加起來
            
        ans = [0]*N # 開始足夠長度的陣列
        now = 0 # 這是等一下要填答案的 index
        for i in range(0, len(nums), 2):
            for k in range(nums[i+0]):
                ans[now] = nums[i+1]
                now += 1 # index++ 以便等一下要填下一格
        return ans
