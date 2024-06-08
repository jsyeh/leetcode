# LeetCode 523. Continuous Subarray Sum
# 是否存在 good subarray, 也就是長度>=2 的連續subarray，它加起來是k的倍數
# 連續subarray加總的結果，可用 prefix 快速算出來。
# 但想更快，可用 Hash Table 快速確認「有沒有 mod k 相同的值」，即「對應k的倍數」。
# 因距離需要>=2，所以 Hash Table 使用 defaultdict() 來對應「第1次出現這個值」的index
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0  # prefix 對應 nums[0]...nums[i-1] 前幾項加總
        prefixDict = defaultdict(int)  # 可快速查「首次」出過某 prefix 的對應 index
        prefixDict[0] = -1  # 
        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % k  # 更新 prefix
            if prefix in prefixDict and i-prefixDict[prefix] >= 2:
                return True
            if prefix not in prefixDict:  # 本 prefix 之前沒出現過的話
                prefixDict[prefix] = i  # 記錄第一次出現 prefix 的 index
        return False

'''
以下測資容易出錯
[23,2,6,4,7]
13
[23,2,4,6,6]
7
[0]
1
[1,0]
2
[5,0,0,0]
3
'''
