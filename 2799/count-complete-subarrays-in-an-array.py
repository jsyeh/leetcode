# LeetCode 2799. Count Complete Subarrays in an Array
# 整個陣列若有 K 種不同的數，那有幾個 subarray 剛好 K 種不同的數
# 可用「毛毛蟲」sliding window 來解這題
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        K = len(set(nums))  # 先分析，整個陣列，有 K 種不的數
        counter = Counter()
        ans = 0
        tail = 0  # 左邊的尾巴，會吐出數
        for head in range(len(nums)):  # 右邊的頭，會吃入數
            counter[nums[head]] += 1
            while len(counter)>=K:  # 只要數字足夠多
                counter[nums[tail]] -= 1
                if counter[nums[tail]]==0:  # 某數若吐為0
                    del counter[nums[tail]]  # 就無此數
                tail += 1
            # 現在 tail...head 的值，「剛好不足 K 種」
            ans += tail  # 那尾巴放 0... tail-1 都是合理的
        return ans
