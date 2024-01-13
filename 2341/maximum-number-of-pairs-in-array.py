# 能刪掉多少 pair？ 最後剩下幾個？
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums) # 先變成類似字點的 Counter
        ans = 0 # 有幾組 pair
        single = 0 # 剩幾個孤單的數
        for k in counter: # 每一個數
            v = counter[k] # 對應出現的次數
            ans += v//2 # 有幾組 pair
            if v%2==1: single += 1 # 孤單的數
        return [ans, single]
