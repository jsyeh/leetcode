# LeetCode 3289. The Two Sneaky Numbers of Digitville
# nums 裡，有兩個數「重覆出現」，把它們找出來。
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)  # 利用 Counter 統計出現次數
        ans = []
        for c in counter:  # 逐一檢查
            if counter[c]>1:  # 找到「重覆出現」的數
                ans.append(c)  # 塞入 ans
        return ans
