# LeetCode 3541. Find Most Frequent Vowel and Consonant
# 找到出現「最多次」的「母音」「子音」
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowelSet = set('aeiou')  # 利用 set() 快速判斷「母音」
        counter = Counter(s)  # 統計字串 s 裡的字母出現次數
        max1, max2 = 0, 0  # 出現最多次的「母音」「子母」一開始設成 0
        for c in counter:
            if c in vowelSet:  # 母音
                max1 = max(max1, counter[c])  # 更新「母音」最多次數
            else:  # 子音
                max2 = max(max2, counter[c])  # 更新「子母」最多次數
        return max1 + max2  # 把「母音出現最多次」+「子音出現最多次」
