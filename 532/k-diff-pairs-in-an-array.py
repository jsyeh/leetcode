# 找出：有多少 pair 的距離是 k
# 可利用 dict 來比對，把出現的數字加入 dict 裡，再逐項回去查
# 但 [1,3,1,5,4] k=0 有 (1,1) pair, 不能去除重覆的數字
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums) # 建字典對照表，對應出現次數
        ans = 0
        for num in counter: # 字典裡，每個數字都查一次
            if k==0 and counter[num]>1: ans += 1
            elif k>0 and num + k in counter: ans += 1
            # 只查 num + k 而不去查 num - k 以免重覆算
        return ans

