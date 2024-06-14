# 想要讓數字都不一樣，題目說，可以慢慢 +1 來讓數字都不一樣
# 所以，可以先把 nums 從小到大排好。接下來，逐一挑數字
# 如果挑出來的數字比前一個數prev大，很好，就簡單更新 prev=num
# 如果不夠大，只好把不夠大的部分加起來 ans += prev + 1 - num
# 就做完了
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        prev = -1
        ans = 0
        nums.sort()
        for num in nums:  # 逐一挑數字
            if num <= prev:  # 數字不夠大
                ans += prev + 1 - num  # 要付出的代價
                prev = prev + 1  # 就讓數字比前一個數+1
            else:  # 數字夠大的話，很好
                prev = num  # 簡單更新 prev
        return ans
