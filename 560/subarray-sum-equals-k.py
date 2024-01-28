# 遇到Hard題目 1074. Number of Submatrices That Sum to Target
# 它的簡化版，就是這題 560. Subarray Sum Equals K
# 所以重寫這題看看，重點(1) running sum 可簡化加總的迴圈
# (2) Hash Map 可簡化找到「是否有重覆出現需要的數字」
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 先做 running sum 簡化加總的問題
        N = len(nums)
        for i in range(1,N): # 因為nums[0]不用加，從1開始
            nums[i] += nums[i-1] # 變成 running sum
        # 到這裡為址 nums[i] 便成為 running sum 了
        # 也就是原本 nums[i]+...+nums[j] 會變成 nums[j]-nums[i-1]
        counter = Counter() # 可計數的 hash map
        counter[0] = 1 # 最左邊會 running sum 0出現1次
        ans = 0 # 數數看有多少可能
        for i in range(N):
            # nums[i] - prev 會得到 k 嗎？
            prev = nums[i] - k # 想問之前有沒有出現 prev
            if counter[prev]>0: # 有幸出現過，可加出k
                ans += counter[prev] # 就增加對應的可能
            counter[nums[i]] += 1 # 多發明一個數字哦
        return ans
