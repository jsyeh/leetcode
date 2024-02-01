# 要把 nums[i] 分到「大小為3」 的一堆 array 裡
# 每個數「剛好用1次」，且array裡任2數的diff <= k
# 只要 return 任一種分法。但做不出來，就 return []
# 其實，只要把 nums.sort() 從小到大排好，便能開始放答案
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        N = len(nums)
        if N%3!=0: return [] # 必須是3的倍數，才能「三三分群」

        nums.sort()
        ans = []
        for i in range(0,N,3): # 三三分群
            if nums[i+2] - nums[i] > k:
                return [] # 距離超過k的話，直接失敗
            ans.append(nums[i:i+3]) # 在合理範圍，就3個1組加入ans
        return ans
