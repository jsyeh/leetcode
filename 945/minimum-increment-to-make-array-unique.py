# 每次只能「increase」，要讓全部的數字都不同。問要做幾次「加大」。
# 可以利用 heap 找出最小的數，當成 prev。接著「逐個取出次大」看是需increase
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        heapify(nums) # 先改成 heap 結構
        prev = heappop(nums) # 取出 prev
        ans = 0 # 要加幾次，才能成功
        while len(nums)>0:
            now = heappop(nums) # 取出目前最小數
            if prev>=now: # 不夠大的話，需要「加大」
                ans += prev+1 - now # 要加大多少？
                now = prev+1 # 便會更大
            prev = now # 更新 prev
        return ans
