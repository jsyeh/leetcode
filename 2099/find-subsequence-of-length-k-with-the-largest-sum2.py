# LeetCode 2099. Find Subsequence of Length K With the Largest Sum
# nums 陣列照順序（可漏掉一些數）挑 k 個數的 subsequence，希望「加起來最大」
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # 值「從大到小」先排好（附對應的index）挑k個，再照index排好，即是答案
        v_i = [ (v,i) for (i,v) in enumerate(nums) ]  # (值,index)
        big = sorted(v_i)[-k:]  # 排好後，把右方較大 k 項取出來
        index = sorted([big[i][1] for i in range(k)])  # 取 index 再排
        return [nums[i] for i in index]  # 照著 index 挑出答案
