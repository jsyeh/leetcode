# 題目: 有幾種「連續的subarray」總和是goal
# 看起來像是 DP 或是 HashMap 的題目
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap = collections.defaultdict(int) # 統計所有 prefix 出現的次數
        prefix = 0 # prefix sum
        hashmap[0] = 1 # 最一開始的prefix是0，對應的 hashmap 就是1開始的值
        ans = 0 # subarrays 加起來是 goal 的全部可能
        for num in nums: # 針對每個數字
            prefix += num # 更新 prefix sum
            ans += hashmap[prefix-goal] # 現在的 prefix - goal，即之前需要的數字，有幾種可能
            hashmap[prefix] += 1 # 又多了1項的加總是它
        return ans
