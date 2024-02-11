# 想找出 k 個數「加起來要最大。所以從大到小sort()好，再把前k項就是答案
# 等等，不對！必須照原本的sequence順序來呈現，所以要先合併index 排序
# 最後再照 index 順序，將數字放回來
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_and_i = [(nums[i],i) for i in range(len(nums))] # 合併
        nums_and_i.sort(reverse=True) # 照 nums[i] 來排序 大到小
        ans = nums_and_i[:k] # 裁切前k項
        ans.sort(key = lambda x : x[1]) # 再照 index 排序
        return [ans[i][0] for i in range(k)] # 列出對應的 nums[i]
