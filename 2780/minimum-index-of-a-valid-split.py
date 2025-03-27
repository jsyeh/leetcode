# LeetCode 2780. Minimum Index of a Valid Split
# 要找到「過半」的數，而且切2段後，2邊都過半，要切在哪裡
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)
        counter = Counter(nums)  # 統計數字出現次數
        big = -1  # 「過半的數」將存這裡
        for c in counter:
            if counter[c] > N//2:
                big = c  # 找到「過半」的那個數了
                break
        if big==-1: return -1  # 沒找到「過半的數」，失敗
        total = counter[big]  # 「總共」有幾個 big
        left = 0  # 「左邊」有幾個 big
        for i, c in enumerate(nums):
            if i==N-1: continue
            if c==big: left += 1  # 「左邊」新找到1個 big
            # 接下來，算一下「是否切得好」，即「兩邊都過半」（左邊過半、右邊過半）
            if left / (i+1) > 0.5 and (total-left) / (N-i-1) > 0.5:
                return i  # 找到答案的位置了
        return -1  # 找不到答案
