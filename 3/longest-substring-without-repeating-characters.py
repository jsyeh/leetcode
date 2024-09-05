# LeetCode 3. Longest Substring Without Repeating Characters
# 找到「最長」的substring,裡面不能用到重覆的字母
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()
        ans = 0
        k = 0  # 尾巴，用伸縮自如的「毛毛蟲法」來解即可
        for i, c in enumerate(s): # i 是頭
            counter[c] += 1
            while counter[c]>1: # 有重覆的話
                counter[s[k]] -= 1  # 尾巴「吐出來」
                k += 1  # 尾巴「往右縮」
            ans = max(ans, i-k+1)  # 更新「長度」
        return ans
