# LeetCode 2845. Count of Interesting Subarrays
# nums 陣列裡「數一數有幾組」小陣列 subarray, 符合以下條件
# 符合 nums[i] % module == k 的 nums[i] 若有 cnt 個, 且 cnt % module == k
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        table = Counter()  # table[r] 記錄「之前」累積「取餘數是r」有幾組
        table[0] = 1  # 有一種可能：都不取的話，餘數為0
        # 有了 Hash Table 方便「查表」，新的數「撞之前的數」就可推算出「合理的數有幾組」
        total = 0  # 統計 nums[0]...nums[i] 有幾個「符合條件/餘數為k」的數（與 cnt 有關）
        ans = 0  # 符合條件的 subarray 有幾組（即 cnt % module == k 的 subarray)
        for num in nums:  # 從左到右、逐一分析處理
            if num % modulo == k: total += 1  # 到目前為止「符合條件/餘數為k」的數有 total 個
            # 希望 cnt % module == k，但「目前」是 total，找「之前」是 total - k「有幾個」剛好可湊出 k
            ans += table[(total - k + modulo) % modulo] 
            # 現在是 total, 之前是 ???, (total - ???) 取餘數 == k，total 取餘數 == (k+???) 取餘數
            # (total-k)取餘數 == ??? 取餘數， 之前 ??? 是 (total - k + modulo) 取餘數
            table[total % modulo] += 1  # 記錄「符合條件/餘數為k」的數目（再「取餘數」）記錄數量
        return ans
