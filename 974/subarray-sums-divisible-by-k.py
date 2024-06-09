i# LeetCode 974. Subarray Sums Divisible by K
# 與昨天的挑戰題很像，不過稍為簡單：只要確認之前有出現過「幾次」
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixMod = 0  # 累積「目前為止」的 prefix sum 的 mod k 值
        prefixModRepeat = defaultdict(int)  # 記錄曾出現 prefixMod 的次數
        prefixModRepeat[0] = 1  # 一定會有的1次：都沒有任何數字，mod k 為0
        ans = 0
        for i in range(len(nums)):
            prefixMod = (prefixMod + nums[i]) % k  # 現在對應 mod k 的值
            # （想像成捲尺，從左界往右拉：兩次拉出來的mod都相同，距離即為k的倍數）
            if prefixMod in prefixModRepeat:  # 若之前曾出現過
            # 找到一堆 mod 相同的prefixMod (若使用defaultdict()其實盲目加即可)
                ans += prefixModRepeat[prefixMod]  
            prefixModRepeat[prefixMod] += 1
        return ans
