# LeetCode 3005. Count Elements With Maximum Frequency
# 找到「出現次數最多」的數字 --- 有哪些數字「都是出現數字最多」的呢?
# ex. [1,2,3,4,5] 出現最多的次數是 1 次, 有 5 個數都出現 1 次, 答案是 5
# ex. [1,2,2,3,1,4] 出現最多的次數是 2 次。有 4 個數 [1,2,2,1] 是這一類, 答案是 4
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)  # 利用 Counter() 來統計「每個數的出現次數」
        M = max(counter.values())  # 出現最多的次數是 M 次
        ans = 0  # 準備累積答案
        for num in nums:  # 再巡一次, 針對出現次數是 M 的數
            if counter[num]==M: ans += 1  # 找到了 +1
        return ans
