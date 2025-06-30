# LeetCode 594. Longest Harmonious Subsequence
# nums 陣列找到最長的 subsequence 且最大值-最小值「剛好是1」
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)  # 先統計數字出現次數
        ans = 0
        for c in counter:  # 依序檢查 c & 相鄰的 c+1
            if counter[c+1]>0:  # 只要有相鄰的 c+1
                # 相鄰的數字「加起來」就是答案。就持續更新答案
                ans = max(ans, counter[c] + counter[c+1]) 
        return ans
