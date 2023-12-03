# 要找「出現頻率最多」的偶數，用 dict字典，就能解
# 不過這題有個陷阱：如果次數一樣多，回傳最小的偶數
# 「需要even偶數」的頻率，如果沒有偶數的頻率，就回傳 -1
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = defaultdict(int)
        ans = -1 # 要回傳的 nums[i]: 偶數，且有最大的頻率
        freq = 0 # 最大頻率, 只考慮偶數
        for n in nums:
            if n%2!=0: continue # 只處理偶數
            d[n] += 1
            if d[n]>freq or (d[n]==freq and n<ans):
            # 題目要：頻率最大，或頻率相同時，最小的偶數
                ans = n
                freq = d[n]
        return ans
